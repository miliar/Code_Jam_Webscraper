#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

typedef long long ll;

//#define ifs cin
//#define ofs cout

ifstream ifs;
ofstream ofs;

map<char, char> m;

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");

	VS inp;
	VS out;

	inp.pb("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	out.pb("our language is impossible to understand");

	inp.pb("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	out.pb("there are twenty six factorial possibilities");;

	inp.pb("de kr kd eoya kw aej tysr re ujdr lkgc jv");
	out.pb("so it is okay if you want to just give up");

	int was[1000];
	REP(i, inp.sz) {
		REP(j, inp[i].sz) {
			if (inp[i][j] != ' ') {
				m[inp[i][j]] = out[i][j];
				was[out[i][j]] = 1;
			}
		}
	}

	
/*
	for (char c = 'a'; c <= 'z'; c++) {
		if (was[c] != 1)
			cout << c << endl;
	}

	for (map<char, char>::iterator it = m.begin(); it != m.end(); it++) {
		cout << (*it).fs << (*it).sc << ' ';
	} */

	m['q'] = 'z';
	m['z'] = 'q';

	string s;
	int n;
	getline(ifs, s);
	sscanf(s.c_str(), "%d", &n);
	
	REP(i, n) {
		getline(ifs, s);
		ofs << "Case #" << i+1 << ": ";
		REP(j, s.sz) {
			if (s[j] == ' ')
				ofs << ' ';
			else
				ofs << m[s[j]];
		}
		ofs << endl;
	}



	return 0;
} 
