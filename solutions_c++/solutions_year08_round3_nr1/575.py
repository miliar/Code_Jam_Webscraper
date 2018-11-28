/*
PROG: 
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

char infile[] = "input.txt";
char outfile[] = "output.txt";
int n;

void Input() {
	freopen(infile, "rt", stdin);
	freopen(outfile, "wt", stdout);
	cin >> n;
}

void Find() {
	REP(test, n) {
		int p, k, l;
		cin >> p >> k >> l;
		vector< int > a(l);
		REP(i, l) cin >> a[i];
		sort(ALL(a));
		reverse(ALL(a));
		int res = 0;
		int z = 1;
		REP(i, l) {
			res += z*a[i];
			if ((i+1)%k == 0) {
				z++;
			}
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
