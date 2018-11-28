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

typedef long long ll;

char infile[] = "input.txt";
char outfile[] = "output.txt";
int n, res;
string s;
int a[100];

void Input() {
	freopen(infile, "rt", stdin);
	freopen(outfile, "wt", stdout);
	scanf("%d\n", &n);
}

 void p(int k) {
	if (k == s.length()) {
		ll number = 0;
		ll part = 0;
		int sign = 1; // +
		REP(i, k) {
			if (a[i] == 0) {
				part = part*10 + (s[i]-'0');
			} else {
				if (sign == 1) {
					number += part;
				} else {
					number -= part;
				}
				sign = a[i];
				part = s[i]-'0';
			}
		}
		if (sign == 1) {
			number += part;
		} else {
			number -= part;
		}

		if (number % 2 == 0 || number % 3 == 0 || number % 5 == 0 || number % 7 == 0) {
			res++;
		}

		return;
	}
	a[k] = 0; // nothing
	p(k+1);
	a[k] = 1; // +
	p(k+1);
	a[k] = 2; // -
	p(k+1);
}

void Find() {
	REP(test, n) {
		getline(cin, s);
		res = 0;
		a[0] = 0;
		p(1);
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
