#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<algorithm>
#include <map>
using namespace std;

#define MAX 100
int main()
{
	ifstream fin("A-small-attempt2.in"); //dualpal.in , dualpal.txt
	ofstream fout("A-small-attempt2.out"); // dualpal.out , dualpalout.txt
	int testCases = 0;
	string*arrays = NULL;
	map<char,char> mapping;

	mapping['e'] = 'o';
	mapping['j'] = 'u';
	mapping['p'] = 'r';
	mapping['m'] = 'l';
	mapping['y'] = 'a';
	mapping['s'] = 'n';
	mapping['l'] = 'g';
	mapping['c'] = 'e';
	mapping['k'] = 'i';
	mapping['d'] = 's';
	mapping['x'] = 'm';
	mapping['v'] = 'p';
	mapping['n'] = 'b';
	mapping['r'] = 't';
	mapping['i'] = 'd';
	mapping['b'] = 'h';
	mapping['t'] = 'w';
	mapping['a'] = 'y';
	mapping['h'] = 'x';
	mapping['w'] = 'f';
	mapping['f'] = 'c';
	mapping['o'] = 'k';
	mapping['u'] = 'j';
	mapping['g'] = 'v';
	mapping['q'] = 'z';
	mapping['z'] = 'q';
	mapping[' '] = ' ';

	
	fin>>testCases;
	fin.ignore();
	arrays = new string[testCases];
	for(int i=0;i<testCases;i++)
	{
		//arrays[i] = NULL;
		//arrays[i] = new char[MAX+1];
		getline(fin, arrays[i]);
		//fin.ignore();
		//cout<<arrays[i]<<endl;
	}
	
	for(int i=0;i<testCases;i++)
	{
		fout<<"Case #"<<i + 1<<": ";
		for(int j=0;j<(int)arrays[i].size(); j++)
		{
			fout<<mapping[arrays[i][j]];
		}
		fout<<'\n';
	}

	fout.close();
	fin.close();
	return 0;
}