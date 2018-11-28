#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

int gcd(int a, int b) {
	while(a > 0 && b> 0) {
		if (a) b %=a;
		if (b) a %=b;
	}
	return a+b;
}

int s(int a, int b) {
	return (a+b-1)/b;
}

int main() {
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);

	int ntc; GI(ntc);
	
	LL n;
	int b1, b2;

	FORE(tc, 1, ntc) {
		cin >> n >> b1 >> b2;

		bool res;

		if (b2 == 0) {
			res = b1 == 0;
		} else {
		
			int g;
			g = gcd(b1, 100);
			int a1 = 100/g; b1 /=g;

			g = gcd(b2, 100);
			int a2 = 100/g; b2 /=g;

			if (g == 100) {
				res = b1 == 1 && a1 == 1;
			} else {
				/*int q = max(s(a1, a2), s(b1, b2));
				q = max(q, s(a1-b1, a2-b2));
				if (q==0)q=1;*/

				res = a1 <= n;
			}
		}


		if (res)
			printf("Case #%d: Possible\n", tc);
		else
			printf("Case #%d: Broken\n", tc);
	}

}
