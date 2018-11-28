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

	string s1,s2,s3,s11,s22,s33;
	s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	s11="our language is impossible to understand";
	s22="there are twenty six factorial possibilities";
	s33="so it is okay if you want to just give up";

	map<char,char> mymap;
	int i;
	for(i=0;i<s1.length();i++)
	{
		if(s1[i]!=' ')
		{mymap[s1[i]]=s11[i];}
		
	}
	for(i=0;i<s2.length();i++)
	{
		if(s2[i]!=' ')
		{mymap[s2[i]]=s22[i];}
	}
	for(i=0;i<s3.length();i++)
	{
		if(s3[i]!=' ')
		{mymap[s3[i]]=s33[i];}
	}
	mymap['q']='z';
	mymap['z']='q';
	string s;
	getline(cin,s);
	for(int caseId=1;caseId<=T;caseId++)
	{
		cout<<"Case #"<<caseId<<": ";		
		getline(cin,s);
		for(i=0;i<s.length();i++)
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

