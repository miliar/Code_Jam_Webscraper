#include <iostream>
#include <stdio.h>
#include <fstream>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
using namespace std;



int main()
{
	ofstream fout("out.txt");
	ifstream fin("in.txt");

	char data[256];

	data['a'] = 'y';
	data['b'] = 'h';
	data['c'] = 'e';
	data['d'] = 's';
	data['e'] = 'o';
	data['f'] = 'c';
	data['g'] = 'v';
	data['h'] = 'x';
	data['i'] = 'd';
	data['j'] = 'u';
	data['k'] = 'i';
	data['l'] = 'g';
	data['m'] = 'l';
	data['n'] = 'b';
	data['o'] = 'k';
	data['p'] = 'r';
	data['q'] = 'z';
	data['r'] = 't';
	data['s'] = 'n';
	data['t'] = 'w';
	data['u'] = 'j';
	data['v'] = 'p';
	data['w'] = 'f';
	data['x'] = 'm';
	data['y'] = 'a';
	data['z'] = 'q';
	data[' '] = ' ';

	int t;
	fin>>t;

	string str;
	int cnt = 0;
	getline(fin, str);
	while (cnt < t){
		getline(fin, str);
		fout<<"Case #"<<cnt+1<<": ";
		for (int i = 0; i < str.size(); i++){
			fout<<data[str[i]];
		}
		fout<<endl;
		cnt++;
	}

	fout.close();

	return 0;
}