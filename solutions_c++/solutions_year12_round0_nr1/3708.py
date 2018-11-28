/*===============================================================
*   Copyright (C) 2012 All rights reserved.
*   
*   file: a.cpp
*   author: ivapple
*   date: 2012-04-14
*   description: 
*
*   update log: 
*
================================================================*/
#include <cstdlib>
#include <cstdio>
#include <cstring>

#include <iostream>
#include <fstream>

#define out(x) (cout<<#x<<": "<<x<<endl)

#define FOR(i,s,t) for(i=s; i<t; i++)

using namespace std;

template<class T>void show(T a, int n){int i; for(i=0;i<n;i++)cout<<a[i]<<" ";cout<<endl;}

template<class T>void show(T a, int r, int l){int i; for(i=0;i<r;i++)show(a[i],l);cout<<endl;}

const char *mapping="yhesocvxduiglbkrztnwjpfmaq";
char str[101];

int main()
{
	int T;
	int i,j;
	int len;
	char ch;
	ifstream fin("A.in");
	fin >> T;
	ofstream fout("A.txt");
	fin.getline(str,101);
	FOR(i,0,T)
	{
		fin.getline(str,101);
		len = strlen(str);
		FOR(j,0,len)
		{
			if (str[j] != ' ')
				str[j] = mapping[str[j]-'a'];
		}
		fout << "Case #" << i+1 << ": " << str << endl;
	}
return 0;
}
