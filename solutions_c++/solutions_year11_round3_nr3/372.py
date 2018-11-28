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

FILE *fp = freopen("C-small-0.in", "r", stdin);
FILE *fout = freopen("C-small-0.out", "w", stdout);

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++) {
		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);
		vector<int> opf(n, 0);
		for (int i = 0; i < n; i++) scanf("%d", &opf[i]);
		int res = -1;
		for (int i = l; i <= h; i++) {
			bool ck = true;
			for (int j = 0; j < n; j++) {
				if (i % opf[j] == 0 || opf[j] % i == 0) ck = true; else ck = false;
				if (!ck) break;
			}
			if (ck) {
				res = i;
				break;
			}
		}
		if (res > 0) printf("Case #%d: %d\n", Ti, res);
		else printf("Case #%d: NO\n", Ti);
	}
	return 0;
}
