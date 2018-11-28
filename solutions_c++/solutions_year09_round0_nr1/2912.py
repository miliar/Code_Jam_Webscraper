// alien_langg.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
string words[5200];
int L,D,N;
int count(string );
int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}
int count(string word)
{
	int counter=0;
	int index=0;
	int loc=0;
	string isolate[20];
	int y=0;
	while(word.length()!=0)
	{
		if(word[0]=='(')
		{
			loc=word.find(')');
			isolate[index]=word.substr(1,loc-1);
			word.erase(0,loc+1);
		}
		else
		{
			isolate[index]=word.substr(0,1);
			word.erase(0,1);
		}
		index++;
	}
	for(int loop=0;loop<D;loop++)
	{
		bool flag=true;
		for(int r=0;r<L;r++)
		{
			if(isolate[r].find(words[loop][r])==string::npos)
			{
				flag=false;
				break;
			}
		}
		if(flag)
			counter++;
	}

return counter;
}

void main()
{
	ifstream cin("large.txt");
    ofstream cout("largeres.txt");
	string word;
	cin>>L>>D>>N;
	for(int p=0;p<D;p++)
		cin>>words[p];
	for (int j=0;j<N;j++)
	{
		cin>>word;
		cout<<"Case #"<<j+1<<": "<<count(word)<<endl;
	}
}

