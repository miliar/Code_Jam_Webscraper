// Speaking in Tongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int tc=0;
	int m[2];
	int v;
	
	string s="ejp mysljylc kd kxveddknmc re jsicpdrysi\
	rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
	de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string t="our language is impossible to understand\
	there are twenty six factorial possibilities\
	so it is okay if you want to just give up";
	char c[26] = "";
	for (int i = 0;i < s.length();i++) {
		c[s[i]-'a'] = t[i];
	}
	c['z'-'a'] = 'q';
	c['q'-'a'] = 'z';
	
	ifstream f("c:\\A-small-attempt0.in");
	ofstream o("c:\\result.txt");
	f>>tc;
	
	char sb[102]="";
	f.getline(sb,101);
	for(int i=1;i<=tc;i++){
		f.getline(sb,101);
		t = "";
		for (int k = 0;k < strlen(sb); k++) {
			if (sb[k] == ' ') {
				t.push_back(' ');
			} else {
				t.push_back(c[sb[k]-'a']);
			}
		}
		o << "Case #"<<i<<": " << t <<endl;
	}
	
	return 0;
}

