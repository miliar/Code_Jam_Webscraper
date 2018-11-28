#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <string>

using namespace std;

const int maxn = 128;

struct {
	int button;
	int move;
} O[maxn], B[maxn];

int lenO,lenB;

ifstream fin("input.txt");

void input() {
	memset(O,0,sizeof(O));
	memset(B,0,sizeof(B));
	string str;
	getline(fin, str);
	stringstream ss;
	ss << str;
	int x;
	char c;
	int i = 0;
	lenO = lenB = 0;
	ss >> x;
	while (ss >> c) {
		ss >> x;
		//cerr << "input " << x << " " << c << "\n";
		i++;
		if (c == 'O') {
			O[lenO].button = x;
			O[lenO].move = i;	
			lenO++;
		} else {
			B[lenB].button = x;
			B[lenB].move = i;
			lenB++;
		}
	}/*
	cerr << "DEBUG\n";
	cerr << str << "\n";
	for (int i=0;i<lenO;i++) {
		cerr << O[i].button << " " << O[i].move << "\n";
	}
	cerr << "\n";
	for (int i=0;i<lenB;i++) {
		cerr << B[i].button << " " << B[i].move << "\n";
	}
	cerr << "----\n";*/
}

int solution;

void solve() {
	solution = 0;
	int curB = 1;
	int curO = 1;
	int posB = 0;
	int posO = 0;
	while (posB < lenB || posO < lenO) {
		bool pushed = false;
		solution++;
		if (posB < lenB) {
			if (curB < B[posB].button) curB++; 
			else if (curB > B[posB].button) curB--;
			else {
				if ((posO >= lenO) || ((posO < lenO) && (B[posB].move < O[posO].move))) {
					pushed = true;
					posB++;
				}
			}
		}
		if (posO < lenO) {
			if (curO < O[posO].button) curO++;
			else if (curO > O[posO].button) curO--;
			else {
				if (!pushed) {
					if ((posB >= lenB) || ((posB < lenB) && (O[posO].move < B[posB].move))) {
						posO++;
					}
				}
			}
		}
	}
}

int main() {

	int T;
	fin >> T;
	string str;
	getline(fin, str);
	for (int t=1;t<=T;++t) {
		input();
		solve();		
		cout << "Case #" << t << ": " << solution << "\n";
	}
	
	return 0;
}
