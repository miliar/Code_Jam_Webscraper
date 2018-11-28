#include<fstream>
#include<iostream>
#include"HashTable.h"

using namespace std;

ifstream fin;
ofstream fout;

class combiners
{
	public:
	HashTable list;
	combiners(void);
	void initialize(int table_length);
	void add(char*,char*);
	char* combine(char* elements);
};

combiners::combiners(void)
{
	// do nothing	
}

void combiners::initialize(int table_length)
{
	list.initialize(2*table_length);	
}

void combiners::add(char* elements,char* result)
{
	list.Insert(elements,result);
	char* swapedElements = new char[2];
	swapedElements[0] = elements[1];
	swapedElements[1] = elements[0];

	list.Insert(swapedElements,result);
}

char* combiners::combine(char* elements)
{
	return list.Search(elements);
}

class destructors
{
	public:
	HashTable list;
	destructors(void);
	void initialize(int);
	void add(char*,char*);
	bool destruct(char,char*);
};

destructors::destructors(void)
{
	// do nothing
}

void destructors::initialize(int table_length)
{
	list.initialize(2*table_length);
}

void destructors::add(char* d1, char* d2)
{
	list.Insert(d1,d2);
	list.Insert(d2,d1);
}

bool destructors::destruct(char c, char* elementList)
{
	char* result;
	result = list.Search(&c);
	if(result != NULL)
	{
		char* x;
		x = strchr(elementList,*result);
		if(x != NULL)
		{
			return true;
		}
		else	return false;
	}
}

class elementsList
{
	public:
	int noCombiners;
	combiners C;
	int noDestructors;
	destructors D;
 
	elementsList(void);
	void run(void);
};

elementsList::elementsList(void)
{
		fin>>noCombiners;
		int i;
		C.initialize(noCombiners);
		i = 0;
		char* Cstr = new char[3];
		char* elms = new char[2];
		char* res = new char[1];
		while(i<noCombiners)
		{
			fin>>Cstr;
			elms[0] = Cstr[0];
			elms[1] = Cstr[1];
			res[0] = Cstr[2];
			C.add(elms,res);
			i++;
		};

		fin>>noDestructors;
		D.initialize(noDestructors);
		i = 0;
		char* Dstr = new char[2];
		char* d1 = new char[1];
		char* d2 = new char[1];
		while(i<noDestructors)
		{
			fin>>Dstr;
			d1[0] = Dstr[0];
			d2[0] = Dstr[1];
			D.add(d1,d2);
			i++;
		}
}

void elementsList::run(void)
{
	char* givenStr;
	char* finalStr;

	int givenStrLen;
	fin>>givenStrLen;
	givenStr = new char[givenStrLen];
	finalStr = new char[givenStrLen];
	fin>>givenStr;

	int g = 0;
	int f = 0;
	int i;
	char* lasttwo = new char[2];
	char* CombResult = new char[1];
	while(g < givenStrLen)
	{	
		if(finalStr[f] == NULL)
		{
			finalStr[f] = givenStr[g++];
			continue;
		}

		
		lasttwo[0] = finalStr[f];
		lasttwo[1] = givenStr[g];
		CombResult = C.combine(lasttwo);
		if(CombResult != NULL)
		{	
			finalStr[f] = *CombResult;
			g++;			
		}

		else if(D.destruct(givenStr[g],finalStr))
		{	
			for(i=0;i<=f;i++)
				finalStr[i] = NULL;
			f = 0;
			g++;
		}
		else
		{	
			finalStr[++f] = givenStr[g++];
		}
	}
	
	if(finalStr[0] != NULL)
	{
		fout<<finalStr[0];
		for(i=1;i<=f;i++)
		{
			fout<<", ";
			fout<<finalStr[i];
		}
	}
}

int main()
{
	fin.open("B-small-attempt0.in");
	int noTests;
	fin>>noTests;
	fout.open("q2.out");

	int i=0;
	while(i<noTests)
	{
		elementsList l;
		fout<<"Case #"<<i+1<<": [";
		l.run();
		fout<<"]\n";
		i++;
	}
}
