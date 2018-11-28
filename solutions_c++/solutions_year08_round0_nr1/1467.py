/*
PROG: A
LANG: C++            
ID: skip
*/

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <ctype.h>
#include <math.h>

using namespace std;

#define FOR(i, a, b) for (int _n(b), i(a); i < _n; i++)
#define REP(i, n) FOR(i, 0, n)
#define ALL(a) a.begin(), a.end()

typedef vector< string > vs;

char infile[] = "input.txt";
char outfile[] = "output.txt";
int n, s, q;
int a[100][1000];

void Input() {
	freopen(infile, "rt", stdin);
	cin >> n;
	freopen(outfile, "wt", stdout);
}

void Find() {
	REP(test, n) {
		scanf("%d\n", &s);
		vs engines;
		REP(i, s) {
			string name;
			getline(cin, name);
			engines.push_back(name);
		}
		scanf("%d\n", &q);
		
		string query;
		getline(cin, query);
		string x("abc");
		int t = x.find("d");
		REP(i, s) {
			if (query.find(engines[i]) != -1) {
				a[i][0] = 10000;
			} else {
				a[i][0] = 0;
			}
		}

		FOR(j, 1, q) {
			getline(cin, query);
			REP(i, s) {
				a[i][j] = 10000;
				if (query.find(engines[i]) != -1) {
					continue;
				}
				REP(k, s) {
					a[i][j] = min(a[i][j], a[k][j-1] + (i != k));
				}
			}
		}

		int res = 10000;
		REP(i, s) {
			res = min(res, a[i][q-1]);
		}
		cout << "Case #" << (test+1) << ": " << res << endl;
	}
}

void Output() {
}

int main() {
	Input();
	Find();
	Output();
}
