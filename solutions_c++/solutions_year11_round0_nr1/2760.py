#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cmath>
using namespace std;

#define eps 1e-9
#define pb push_back
#define mp make_pair
#define RE(i, a, b) for(int (i) = a; (i) < (int)(b); (i)++)
#define REF(i, a, b) RE(i, a, b + 1)
#define REP(i, n) RE(i, 0, n) 
#define FOR(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define SZ(v) ((int)(v).size())
template<class T>string toString(T a) { stringstream t; t << a; return t.str(); }

FILE *fin = freopen("A-large.in", "r", stdin);
FILE *fout = freopen("A.out", "w", stdout);

int main()
{
	int ncase;
	scanf("%d ", &ncase);
	for (int cases = 1; cases <= ncase; cases++) {
		int res = 0;
		int n; scanf("%d ", &n);
		int nt[2] = {0, 0}; // 0 : o, 1 : b
		int np[2] = {1, 1};
		for (int i = 0; i < n; i++) {
			char c; int b;
			scanf("%c %d ", &c, &b);
			int j;
			if (c == 'O') j = 0; else j = 1;
			if (nt[1 - j] >= nt[j] + abs(np[j] - b)) {
				nt[j] = nt[1 - j] + 1;
				np[j] = b;
			}
			else {
				nt[j] += abs(b - np[j]) + 1;
				np[j] = b;
			}
		}
		res = max(nt[0], nt[1]);
		printf("Case #%d: %d\n", cases, res);
	}

	return 0;
}
