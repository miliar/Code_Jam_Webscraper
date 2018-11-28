/*
PROG: B
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
	scanf("%d",&n);
	freopen(outfile, "wt", stdout);
}

void Find() {
	REP(test, n) {
		int na, nb, t;
		scanf("%d%d%d\n", &t, &na, &nb);

		int a[200][2];
		int b[200][2];
		int h1, h2, m1, m2;
		REP(i, na) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a[i][0] = h1*60 + m1;
			a[i][1] = h2*60 + m2 + t;
		}
		REP(i, nb) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			b[i][0] = h1*60 + m1;
			b[i][1] = h2*60 + m2 + t;
		}

		int needA[4*1024];
		int needB[4*1024];
		memset(needA, 0, sizeof(needA));
		memset(needB, 0, sizeof(needB));
		REP(i, na) {
			needA[a[i][0]]--;
			needB[a[i][1]]++;
		}
		REP(i, nb) {
			needA[b[i][1]]++;
			needB[b[i][0]]--;
		}

		int ak = 0, bk = 0;
		int ar = 0, br = 0;
		REP(i, 24*60) {
			ak += needA[i];
			bk += needB[i];
			ar = min(ar, ak);
			br = min(br, bk);
		}

		cout << "Case #" << (test+1) << ": " << -ar << " " << -br << endl;
	}
}

void Output() {
}

int main() {
	Input();
	Find();
	Output();
}
