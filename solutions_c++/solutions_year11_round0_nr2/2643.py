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

int combine[30][30];
bool oppose[30][30];

int c2i(char c)
{
	return c - 'A' + 1;
}

FILE *fin = freopen("B-large.in", "r", stdin);
FILE *fout = freopen("B-large.out", "w", stdout);
int main()
{
	int ncase;
	scanf("%d ", &ncase);
	for (int cases = 1; cases <= ncase; cases++) {
		memset(combine, 0, sizeof(combine));
		memset(oppose, 0, sizeof(oppose));
		int n;
		char buf[255];
		scanf("%d ", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s ", &buf);
			int j = c2i(buf[0]), k = c2i(buf[1]);
			combine[j][k] = combine[k][j] = c2i(buf[2]);
		}
		scanf("%d ", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s ", &buf);
			int j = c2i(buf[0]), k = c2i(buf[1]);
			oppose[j][k] = oppose[k][j] = true;
		}
		scanf("%d ", &n);
		scanf("%s ", &buf);
		int vec[255] = {0, }, ptr = 0;
		for (int i = 0; i < n; i++) {
			vec[ptr++] = c2i(buf[i]);
			if (ptr >= 2) {
				if (combine[vec[ptr - 1]][vec[ptr - 2]] > 0) {
					int t = combine[vec[ptr - 1]][vec[ptr - 2]];
					vec[--ptr] = 0; vec[--ptr] = 0; vec[ptr++] = t;
				}
				else {
					int z = -1;
					for (int j = ptr - 1; j >= 0; j--) {
						if (oppose[vec[j]][vec[ptr - 1]]) {
							z = j; break;
						}
					}
					if (z >= 0) {
						memset(vec, 0, sizeof(vec));
						ptr = 0;
					}
				}
			}
		}
		printf("Case #%d: [", cases);
		for (int i = 0; i < ptr; i++) {
			if (i < ptr - 1) printf("%c, ", vec[i] + 'A' - 1);
			else printf("%c", vec[i] + 'A' - 1);
		}
		printf("]\n");
	}
	fcloseall();
	return 0;
}
