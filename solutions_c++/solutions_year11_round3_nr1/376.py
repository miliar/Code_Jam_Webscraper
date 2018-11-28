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

FILE *fin = freopen("A-large-0.in", "r", stdin);
FILE *fout = freopen("A-large-0.out", "w", stdout);

int main()
{
	int T;
	scanf("%d ", &T);
	for (int Ti = 1; Ti <= T; Ti++) {
		int n, m;
		scanf("%d %d ", &n, &m);
		vector< vector<bool> > b(n, vector<bool>(m, false));
		vector< vector<int> > f(n, vector<int>(m, 0));
		for (int i = 0; i < n; i++) {
			char buf[255];
			scanf("%s ", &buf);
			for (int j = 0; j < m; j++) {
				if (buf[j] == '#') b[i][j] = true; else b[i][j] = false;
			}
		}

		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < m - 1; j++) {
				if (b[i][j] && b[i][j + 1] && b[i + 1][j] && b[i + 1][j + 1]) {
					f[i][j] = f[i + 1][j + 1] = -1;
					f[i][j + 1] = f[i + 1][j] = 1;
					b[i][j] = b[i][j + 1] = b[i + 1][j] = b[i + 1][j + 1] = false;
				}
			}
		}

		bool ck = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (b[i][j]) ck = false;
				if (!ck) break;
			}
			if (!ck) break;
		}

		printf("Case #%d:\n", Ti);
		if (ck) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (f[i][j] == 0) printf(".");
					else if (f[i][j] == -1) printf("/");
					else if (f[i][j] == 1) printf("\\");
				}
				printf("\n");
			}
		}
		else printf("Impossible\n");
	}
	return 0;
}
