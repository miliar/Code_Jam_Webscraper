// a1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<memory>
#include<string>
#include<map>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("b.txt","w",stdout);
	int T;
	cin>>T;

	/*
	"ejp mysljylc kd kxveddknmc re jsicpdrysi";
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	"de kr kd eoya kw aej tysr re ujdr lkgc jv";
	"our language is impossible to understand";
	"there are twenty six factorial possibilities";
	"so it is okay if you want to just give up";
	*/
	map<char,char> mymap;
	int i;
	mymap['a']='y';
	mymap['b']='h';
	mymap['c']='e';
	mymap['d']='s';
	mymap['e']='o';
	mymap['f']='c';
	mymap['g']='v';
	mymap['h']='x';
	mymap['i']='d';
	mymap['j']='u';
	mymap['k']='i';
	mymap['l']='g';
	mymap['m']='l';
	mymap['n']='b';
	mymap['o']='k';
	mymap['p']='r';
	mymap['q']='z';
	mymap['r']='t';
	mymap['s']='n';
	mymap['t']='w';
	mymap['u']='j';
	mymap['v']='p';
	mymap['w']='f';
	mymap['x']='m';
	mymap['y']='a';
	mymap['z']='q';
	string s;
	getline(cin,s);
	for(int caseId=1;caseId<=T;caseId++)
	{
		cout<<"Case #"<<caseId<<": ";		
		getline(cin,s);
		for(i=0;i < s.length();i++)
		{
			if(s[i]!=' ')
			{
				cout<<mymap[s[i]];
			}
			else
			{cout<<' ';}
		}
		cout<<endl;
	}	
	return 0;
}

