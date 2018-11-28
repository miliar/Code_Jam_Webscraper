#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <cmath>
#include <cstdio>
#include <map>
#include <cstdio>

using namespace std;

string S[30];
int T;

map<char, int> m, m_s;

void analysis()
{
	for (int i=0; i<26; i++) m['a'+i] = 0;
	for (int i=0; i<T; i++) {
		for (int j=0; j<S[i].size(); j++) {
			m[S[i][j]]++;
		}
	}

	for (int i=0; i<26; i++) {
		char c = 'a'+i;
		printf("%c: %5d     ", c, m[c]);
		if ((i+1) % 5 == 0) cout << endl;
	}
	cout << endl;
}

void _replace(char a, char b)
{
	for (int i=0; i<T; i++) 
		for (int j=0; j<S[i].size(); j++) {
			if (S[i][j] == a) S[i][j] = b;
			else if (S[i][j] == b) S[i][j] = a;
		}
}

void replace()
{
	char a, b;
	cin >> a >> b;
	_replace(a, b);
}

void print()
{
	for (int i=0; i<T; i++)
		cout << "case " << i+1 << ":  " << S[i] << endl;
}

void set()
{
	char c;
	cin >> c;
	m_s[c] = 1;
}

void get()
{
	for (char c='a'; c<='z'; c++)
		if (m_s[c] == 0) cout << c << " ";
	cout << endl;
}

void output()
{
	ofstream myfile;
	myfile.open("A-small-1.out");
	for (int i=1; i<=T; i++)
		myfile << "Case #" << i << ": " << S[i-1] << endl;
	myfile.close();
}

void decipher()
{
	_replace('e', 'o');	
	_replace('j', 'u');	
	_replace('p', 'r');	
	_replace('m', 'l');	
	_replace('y', 'a');	
	_replace('s', 'n');	
	_replace('m', 'g');	
	_replace('c', 'e');	
	_replace('k', 'i');	
	_replace('d', 's');	
	_replace('x', 'm');	
	_replace('v', 'p');	
	_replace('d', 'b');	
	_replace('v', 't');	
	_replace('k', 'd');	
	_replace('v', 'w');	
	_replace('h', 'x');	
	_replace('v', 'f');	
	_replace('v', 'c');	
	_replace('v', 'k');	
	_replace('h', 'v');	
	_replace('z', 'q');	
}

void solve()
{
	char command;
	while (true) {
		cout << "a: analysis, r: replace, p: print, o: output" << endl;
		cin >> command;
		switch (command) {
		case 'a':
			analysis();
			break;
		case 'r':
			replace();
			break;
		case 'p':
			print();
			break;
		case 's':
			set();
			break;
		case 'g':
			get();
			break;
		case 'o':
			output();
			break;
		case 'd':
			decipher();	
			break;
		}
	}
}


int main()
{
	ifstream myfile;
	myfile.open("A-small-1.in");

	string tmp;
	//getline(myfile, tmp);
	myfile >> T;
	
	getline(myfile, tmp);	
	for (int t=1; t<=T; t++) {
		// initialization, IO
		getline(myfile, S[t-1]);	
	}
	
	solve();

	//for (int t=1; t<=T; t++) {
	//	cout << "Case #" << t << ": ";
	//	solve();
	//}
}
