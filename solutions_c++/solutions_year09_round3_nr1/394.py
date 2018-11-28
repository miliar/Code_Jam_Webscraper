#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <deque>
#include <map>
#include <math.h>
#include "bigint.h"
using namespace std;

char *infilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round1c_1\\A-large.in";
char *outfilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round1c_1\\out.txt";

RossiBigInt analyze(string str)
{
	int base = 0; 
	map<char,int> nm;
	map<char,int>::iterator it;
	RossiBigInt number(0);
	int kind = 0;
	for(int j = 0; j < str.length(); j ++)
	{
		char c = str[j];
		if(nm.count(c) == 0)
		{
			nm[c] = ++base;
			kind++;
			if(kind == 2)
			{
				nm[c] = 0;
				base--;
			}
		//cout<<nm[c]<<endl;
		}
	}
	base++;

	for(int j = 0; j < str.length(); j++)
	{
		char c = str[j];
		number = number * base + nm[c];
		//cout<<nm[c];
	}
	//cout<<endl;

	return number;
}

int main()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}

	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}
	
	int T;
	infile>>T;
	string buffer;
	getline(infile, buffer);
	for(int i = 0; i < T; i++)
	{
		getline(infile, buffer);
		outfile<<"Case #"<<i + 1<<": "<<analyze(buffer)<<endl;
	}

	infile.close();
	outfile.close();
	return 1;
}
