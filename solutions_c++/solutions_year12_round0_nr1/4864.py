// codejam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream google("A-small-attempt2.in",ios_base::in);
	ofstream eng("output.txt",ios_base::out);
	string googlerese = "ejp mysljylc kd kxveddknmc re jsicpdrysi\nrbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\nde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string english = "our language is impossible to understand\nthere are twenty six factorial possibilities\nso it is okay if you want to just give up";
	map <char,char> dict;
	dict[' '] = ' ';
	dict['z'] = 'q';
	dict['q'] = 'z';
	int len = english.length();
	for (int i=0; i<len; i++){
		dict[googlerese[i]] = english[i];
	}
	char* temp= new char;
	google.getline(temp,100);
	string sen;
	int count =atoi(temp);
//	cout<<count;
	int cs = 0;
	for (int i = 0; i<count; i++){
		if(google.eof())
			break;
		cs++;
		eng<<"Case #"<<cs<<": ";
		google.getline(temp,200);
		sen = string(temp);
		if(sen.length()>100)
			sen.erase(100);
//		eng<<sen;
		for(int j = 0; j< sen.length(); j++){
			eng<<dict[sen[j]];
		}
		eng<<endl;
	}
	return 0;
}

