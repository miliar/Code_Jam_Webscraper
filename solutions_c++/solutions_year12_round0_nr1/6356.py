// ProblemA.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>
#include <map>
using namespace std;
int main(int argc, char* argv[])
{
	map<char,char> translate;
	translate['a'] = 'y';
	translate['b'] = 'h';
	translate['c'] = 'e';
	translate['d'] = 's';
	translate['e'] = 'o';
	translate['f'] = 'c';
	translate['g'] = 'v';
	translate['h'] = 'x';
	translate['i'] = 'd';
	translate['j'] = 'u';
	translate['k'] = 'i';
	translate['l'] = 'g';
	translate['m'] = 'l';
	translate['n'] = 'b';
	translate['o'] = 'k';
	translate['p'] = 'r';
	translate['q'] = 'z';
	translate['r'] = 't';
	translate['s'] = 'n';
	translate['t'] = 'w';	
	translate['u'] = 'j';
	translate['v'] = 'p';
	translate['w'] = 'f';
	translate['x'] = 'm';
	translate['y'] = 'a';
	translate['z'] = 'q';
	int numCases = 0;
	cin >> numCases >> ws;
	for (int A = 0; A < numCases; A++) {
		//char str[101] = {0};
		string strr;
		getline(cin,strr,'\n');
		//str = strr.c_str();
		for (int b = 0; b < strr.length();b++) {
			if (strr[b] != ' ' && strr[b] != '\0') {
				strr[b] = translate[strr[b]];
			}
		}
		cout << "Case #" << (A+1) << ": " << strr << endl;
	}
	return 0;
}

