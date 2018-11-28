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

FILE *fp = freopen("A-large-0.in", "r", stdin);
FILE *fout = freopen("A-large-0.out", "w", stdout);

int main()
{
	int T;
	scanf("%d ", &T);
	for (int Ti = 1; Ti <= T; Ti++) {
		int n;
		scanf("%d ", &n);
		vector< vector<int> > table(n, vector<int>(n, false));
		vector<double> wp(n, 0.0);
		vector<double> owp(n, 0.0);
		vector<double> oowp(n, 0.0);

		for (int i = 0; i < n; i++) {
			char buf[255];
			scanf("%s ", &buf);
			for (int j = 0; j < n; j++) {
				if (buf[j] == '.') table[i][j] = -1; else table[i][j] = int(buf[j] - '0');
			}
		}

		for (int i = 0; i < n; i++) {
			int win = 0, total = 0;
			for (int j = 0; j < n; j++) {
				if (table[i][j] >= 0) total++;
				if (table[i][j] > 0) win++;
			}
			wp[i] = double(win) / double(total);
		}

		for (int i = 0; i < n; i++) {
			int totals = 0;
			double twp = 0.0;
			for (int j = 0; j < n; j++) {
				if (table[i][j] >= 0) {
					int win = 0, total = 0;
					for (int k = 0; k < n; k++) {
						if (k == i) continue;
						if (table[j][k] >= 0) total++;
						if (table[j][k] > 0) win++;
					}
					totals++;
					twp += double(win) / double(total);
				}
			}
			owp[i] = twp / double(totals);
		}

		for (int i = 0; i < n; i++) {
			int total = 0;
			double towp = 0.0;
			for (int j = 0; j < n; j++) {
				if (table[i][j] >= 0) {
					total++;
					towp += owp[j];
				}
			}
			oowp[i] = towp / double(total);
		}

		printf("Case #%d:\n", Ti);
		for (int i = 0; i < n; i++) {
			printf("%lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
