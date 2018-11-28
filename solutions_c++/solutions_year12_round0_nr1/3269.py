// GCJ 2011 Qual 1.cpp : main project file.

// Test.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
#include <map>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("A-small-attempt2.in");
	ofstream outfile("A-small-attempt2.out");
	string str, input;
	int cases;
	if (infile.is_open()) {
		getline(infile,str);
		stringstream ss;
		ss << str;
		ss >> cases;
	}
	string after  = "a zooq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	string before = "y qeez ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	map<char,char> mapping;
	for(int i=0;i<before.size();i++) {
		mapping[before[i]]=after[i];
	}
	for(int i = 0; i < cases; i++) {
		string s;
		stringstream ss;
		getline(infile,s);
		ss >> s;
		for(int j=0;j<s.size();j++) {
			if(!mapping.count(s[j])) cout<<s[j]<<endl;
			s[j]=mapping[s[j]];
		}
		outfile << "Case #" << (i+1) << ": " << s << endl; 
	}
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}