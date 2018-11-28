//============================================================================
// Name        : SPEAKING.cpp
// Author      : Loc Ngo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");

void process(int T)
{
	char A[500];
	A['a'] = 'y';
	A['b'] = 'h';
	A['c'] = 'e';
	A['d'] = 's';
	A['e'] = 'o';
	A['f'] = 'c';
	A['g'] = 'v';
	A['h'] = 'x';
	A['i'] = 'd';
	A['j'] = 'u';
	A['k'] = 'i';
	A['l'] = 'g';
	A['m'] = 'l';
	A['n'] = 'b';
	A['o'] = 'k';
	A['p'] = 'r';
	A['q'] = 'z';
	A['r'] = 't';
	A['s'] = 'n';
	A['t'] = 'w';
	A['u'] = 'j';
	A['v'] = 'p';
	A['w'] = 'f';
	A['x'] = 'm';
	A['y'] = 'a';
	A['z'] = 'q';
	A[' '] = ' ';
	string s;
	getline(fin,s);
	fout<<"Case #"<<T<<": ";
	for(int i=0;i<s.length();i++)
		fout<<A[s[i]];
	fout<<endl;
}


int main() {
	int T;
	fin>>T;
	fin.ignore();
	for(int i=1;i<=T;i++)
		process(i);
	return 0;
}
