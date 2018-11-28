// gcj11.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <fstream>
using namespace std;



int _tmain(int argc, _TCHAR* argv[])
{
	int testcases , i,j,k;
	string n;
	string temp;
	string s;
	ifstream inf;
	ofstream of;
	inf.open("A-small-attempt.txt");
	of.open("output.txt");
	map<char,char>m;
	getline(inf,n);
	testcases = atoi(n.c_str());
	
	  
    m['a'] = 'y';
    m['b'] = 'h';
	m['c'] = 'e';
	m['d']= 's';
	m['e']= 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i']= 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l']= 'g';
	m['m']= 'l';
	m['n']= 'b';
	m['o']= 'k';
	m['p']= 'r';
	m['q']= 'z';
	m['r']= 't';
	m['s']= 'n';
	m['t']= 'w';
	m['u']= 'j';
	m['v']= 'p';
	m['w']= 'f';
	m['x']= 'm';
	m['y']= 'a';
	m['z']= 'q';
	m[' '] = ' ';
	int nu = 0;
    while(testcases-- > 0)
	{
		getline(inf,temp);nu++;
		i = temp.length() -1;
		for(j=0;j <= i;j++)
		{
			temp[j] = m[temp[j]];
		}
		of<<"Case #"<<nu<<": "<<temp<<endl;
	}
	inf.close();
	of.close();
	return 0;
}

