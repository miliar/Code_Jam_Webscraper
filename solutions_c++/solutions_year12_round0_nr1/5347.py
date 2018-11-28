/*
 * first.cpp
 *
 *  Created on: 14-Apr-2012
 *      Author: dinesh
 */

#include<iostream>
#include<map>
#include<stdio.h>
#include<string>
#include<climits>

using namespace std;

int main()
{


	map<char,char> mapping ;
	string str = "zqejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string str1= "qzour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for(int i = 0;i<str.length();i++)
	{
		mapping[str[i]] = str1[i];
	}

	int t;
	cin>>t;
	string input_str ;

	fflush(stdin);
	cin.ignore(INT_MAX,'\n');
	for(int i = 0;i<t;i++)
	{

		getline(cin,input_str);

		cout<<"Case #"<<i+1<<": ";
		for(int j = 0;j<input_str.length();j++)
		{
			cout<<mapping[input_str[j]];
		}
		cout<<endl;
		fflush(stdin);

	}




}
