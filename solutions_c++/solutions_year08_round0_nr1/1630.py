#include<iostream>
#include<cstring>
#include<stdlib.h>
using namespace std;

class EngineList
{
	char **engineList;
	int length;
public:
	EngineList(int);
	~EngineList();
	void populate();
	void display();
	int index(char*);	
	int getLength(){ return length; }
};
EngineList::EngineList(int count)
{
	length=count;
	engineList=new char*[length];
	for(int i=0;i < length;i++)
		engineList[i]=new char[100];
}
EngineList::~EngineList()
{
	for(int i=0;i < length;i++)
	 delete[] engineList[i];
	delete[] engineList;
}
void EngineList::populate()
{
	for(int i=0;i < length;i++)
		cin.getline(engineList[i],101);
}
int EngineList::index(char *str)
{
	for(int i=0;i < length;i++)
	 if(strcmp(engineList[i],str) == 0)
	 	return i;
	return -1;
}
void EngineList::display()
{
	for(int i=0;i < length;i++)
		cout<<endl<<engineList[i];
}
class QueryList
{
	int length;
public:
	char **queryList;
	QueryList(int);
	~QueryList();
	void populate();
	void display();
	int getLength(){ return length; }
};
QueryList::QueryList(int count)
{
	length=count;
	queryList=new char*[length];
	for(int i=0;i < length;i++)
		queryList[i]=new char[101];
}
QueryList::~QueryList()
{
	for(int i=0;i < length;i++)
	 delete[] queryList[i];
	delete[] queryList;
}
void QueryList::populate()
{
	for(int i=0;i < length;i++)
		cin.getline(queryList[i],101);
}
void QueryList::display()
{
	for(int i=0;i < length;i++)
		cout<<endl<<queryList[i];
}
class Counter
{
	QueryList *ptrQueryList;
	EngineList *ptrEngineList;
	bool *engineUsed;
	int count;
	int length;
public:
	Counter(EngineList*, QueryList*);
	~Counter();
	void setAllFalse();
	int minSwitch(int);
};
Counter::Counter(EngineList *ptrEL, QueryList *ptrQL)
{
	ptrEngineList=ptrEL;
	ptrQueryList=ptrQL;
	length=ptrEngineList->getLength();
	engineUsed=new bool[length];
	count=length;
}
Counter::~Counter()
{
	delete[] engineUsed;
}
void Counter::setAllFalse()
{
	for(int i=0;i < length;i++)
	 engineUsed[i]=false;
}
int Counter::minSwitch(int low)
{
	setAllFalse();
	count=ptrEngineList->getLength();
	int i;
	for(i=low;i < ptrQueryList->getLength(); i++)
	{
		int temp=ptrEngineList->index((ptrQueryList->queryList)[i]);
		if(temp != -1)
		 if(engineUsed[temp] != true) 
		 {
			engineUsed[temp]=true;
			count--;
		 	if(count <= 0)
				return 1 + minSwitch(i); 		
		 }
	}
	return 0;
}
			
class TestCase
{
	EngineList *ptrEL;
	QueryList *ptrQL;
	Counter *ptrC;
public:
	int output();
};

int TestCase::output()
{
	char no[5];
	
	cin.getline(no,4);
	ptrEL=new EngineList(atoi(no));
	ptrEL->populate();
	
	cin.getline(no,5);
	ptrQL=new QueryList(atoi(no));
	ptrQL->populate();
	
	ptrC=new Counter(ptrEL,ptrQL);
	
	int op=ptrC->minSwitch(0);
	delete ptrC;
	delete ptrQL;
	delete ptrEL;
	return op;
}
	
	
int main()
{
	char no[3];
	cin.getline(no,3);/* Max 20 test cases */
	int N=atoi(no);
	TestCase tc;
	for(int i=1;i <= N;i++)
	 cout<<"Case #"<<i<<": "<<tc.output()<<endl;	
	return 0;
}
