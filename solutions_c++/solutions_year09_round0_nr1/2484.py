// AlienLanguage.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <stack>
#include <math.h>
#include <fstream>
#include <regex> 
using namespace std;
using namespace std::tr1;

class AlienWords
{
public:
	int wordCount;
	string *word;
	AlienWords(){wordCount=0;}
	~AlienWords(){delete []word;}
	int AddWord(string wordtobeAdded);	
	void reSizeWordArray();
	int FindWord(string wordtobeSearched);
};

int AlienWords::FindWord(string wordtobeSearched)
{
	for(int x=0;x<wordCount;x++)
	{
		if(_stricmp(word[x].c_str(),wordtobeSearched.c_str())==0)
			return x;		
	}

	return -1;
	
}
void AlienWords::reSizeWordArray()
{
        string* temp = new string[++wordCount]; 
        for (int copyx=0; copyx<(wordCount-1); copyx++)
		{
            temp[copyx] = word[copyx];       
        }
        delete [] word;              
        word = temp;                
           
}

int AlienWords::AddWord(string wordtobeAdded)
{
	if(wordCount==0){word=new string[++wordCount];}
	else{reSizeWordArray();}
	word[wordCount-1]=wordtobeAdded;
	return 0;
}

struct patternString
{
	string text;
	bool isPattern;
};

class Pattern
{
public:
	int wordsFound;
	string rawPattern;
	int elementCount;
	patternString * elements;
	Pattern(){wordsFound=0;elementCount=0;}
	~Pattern(){if(elementCount>0) delete []elements;}
	void reSizeElements();
	void init();
	void AddElement(string tmpString,bool tmpisPattern);
	int SearchWords(AlienWords *dictionary);
};

void Pattern::reSizeElements()
{
        patternString* temp = new patternString[++elementCount]; 
        for(int copyx=0; copyx<elementCount-1; copyx++)
		{
            temp[copyx] = elements[copyx];      
        }
        delete [] elements;            
        elements = temp;             
           
}

void Pattern::AddElement(string tmpString,bool tmpisPattern)
{
	if(elementCount==0)	{elements=new patternString[++elementCount];}
	else{reSizeElements();}

	elements[elementCount-1].text=tmpString;
	elements[elementCount-1].isPattern=tmpisPattern;
}


void Pattern::init()
{
	string tmpString;
	int counter,stringAdded;
	counter=0;
	stringAdded=1;
	bool tempIsPattern=false;
	
	for(unsigned int x=0;x<rawPattern.length();x++)
	{		
		char ch=rawPattern.at(x);
		if(ch==' ')
		{
			continue;
		}

		if(ch=='(')
		{
			if(tmpString.length()>0)
			{
				AddElement(tmpString,false);
				tmpString="";
				continue;
			}
				
			continue;
		}

		if(ch==')')
		{
			if(tmpString.length()>0)
			{
				AddElement(tmpString,true);
				tmpString="";
				continue;
			}
				
			continue;
		}

		tmpString.push_back(ch);		
			
	}

	if(tmpString.length()>0)
	{
		AddElement(tmpString,false);
		tmpString="";
	}

}



int Pattern::SearchWords(AlienWords *dictionary)
{
	string myRegEx=rawPattern;
		
	for(unsigned int i=0;i<myRegEx.length();i++)
	{
		if(myRegEx[i]=='(')myRegEx[i]='[';
		if(myRegEx[i]==')')myRegEx[i]=']';
	}

	int found=0;
	do
	{
		found=0;
		int pos;
		pos=myRegEx.find(' ');
		
		if(pos!= myRegEx.npos)
		{
			myRegEx.erase(pos,1);
			found=1;
		}
	}while(found>0);

	regex rgx(myRegEx); 

	for(int k=0;k<dictionary->wordCount;k++)
	{

		if(regex_search(dictionary->word[k], rgx)==1)wordsFound++;

	}

	return wordsFound;
}


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFile;
	ofstream outputFile;
	string filename,filename2; 

	filename="input.txt";
	filename2="output.txt";

	inputFile.open(filename.c_str());  
	if(!inputFile)
	{
		cout<<"Error Opening File";
	}
	else
	{
		outputFile.open(filename2.c_str());
	
		int L,D,N;
		inputFile>>L>>D>>N;

		AlienWords words;
		
		for(int i=0;i<D;i++)
		{
			string tmpWord;
			inputFile>>tmpWord;
			words.AddWord(tmpWord);
		}

		for(int u=0;u<N;u++)
		{
			string tmpPattern;
			Pattern alienPattern;
			inputFile>>tmpPattern;
			alienPattern.rawPattern.assign(tmpPattern);
			outputFile<<"Case #"<<u+1<<": "<<alienPattern.SearchWords(&words)<<"\n";			
		}
		

		outputFile.close();

	}

	inputFile.close();	
		
	cout<<"\n";
	system ("pause");
	return 0;	
}

