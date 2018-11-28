// Speaking in Tongues.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include<iostream>
#include<conio.h>
#include<map>
#include<string>
#include<fstream>
#include<stdlib.h>
using namespace std;
struct TestCase
{
	string str;
};
std::map<char,char> g_Conversion;
int main()
{
	g_Conversion['a']='y';
	g_Conversion['b']='h';
	g_Conversion['c']='e';
	g_Conversion['d']='s';
	g_Conversion['e']='o';
	g_Conversion['f']='c';
	g_Conversion['g']='v';
	g_Conversion['h']='x';
	g_Conversion['i']='d';
	g_Conversion['j']='u';
	g_Conversion['k']='i';
	g_Conversion['l']='g';
	g_Conversion['m']='l';
	g_Conversion['n']='b';
	g_Conversion['o']='k';
	g_Conversion['p']='r';
	g_Conversion['q']='z';
	g_Conversion['r']='t';
	g_Conversion['s']='n';
	g_Conversion['t']='w';
	g_Conversion['u']='j';
	g_Conversion['v']='p';
	g_Conversion['w']='f';
	g_Conversion['x']='m';
	g_Conversion['y']='a';
	g_Conversion['z']='q';
	ifstream in("A-small-attempt2.in",ios::in);
	if(in)
	{
          unsigned int _uT;
	char input[1024];
	//cin>>_uT;
	in.getline(input,1024);
	
	_uT=atoi(input);
	
	TestCase *_TC = new TestCase[_uT];
	for(unsigned int i=0;i<_uT;i++)
	{
                
	//	fflush(stdin);
		char txt[1024]={0};
		in.getline(txt,1024);
	//	cin.getline(txt,1024);
		_TC[i].str=txt;
	}
	in.close();
	ofstream output("outputfile.txt",ios::out);
	if(output)
	for(unsigned int i=0;i<_uT;i++)
	{
		char op[1024];
		sprintf(op,"Case #%d: ",i+1);
		output.write(op,strlen(op));
		cout<<"Case #"<<i+1<<": ";
		for(unsigned int j=0;j<_TC[i].str.length();j++)
		{
			if(_TC[i].str.at(j)==32)
			{
				output.write(&_TC[i].str.at(j),1);
				cout<<_TC[i].str.at(j);
			}
			else
			{
				output.write(&g_Conversion[_TC[i].str.at(j)],1);
				cout<<g_Conversion[_TC[i].str.at(j)];
			}
		}
		char ch='\n';
		cout<<endl;
		output.write(&ch,1);
	}
	output.close();
      
    }
    else
    {
        cout<<"input file not open";
    }
	
	getch();
	return 0;
}

