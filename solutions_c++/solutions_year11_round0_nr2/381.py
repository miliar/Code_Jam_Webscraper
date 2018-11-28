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

int del[256][256];
char tr[256][256];

char buf[1024];
char str[1024];

int main() {
freopen("B-large.in", "rt", stdin);
freopen("B-large.out", "w", stdout);

	int ntc; GI(ntc);
	
	FORE(tc, 1, ntc) {
		memset(del, 0, sizeof del);
		memset(tr, 0, sizeof tr);

		int n;

		GI(n);
		FI {
			scanf("%s", buf);
			tr[ buf[0] ][ buf[1] ] = tr[ buf[1] ][ buf[0] ] = buf[2];
		}

		GI(n);
		FI {
			scanf("%s", buf);
			del[ buf[0] ][ buf[1] ] = del[ buf[1] ][ buf[0] ] = 1;
		}

		GI(n);
		scanf("%s", buf);

		int cnt = 0;
		FI {
			if (!cnt) { str[cnt++] = buf[i]; continue; }

			if (tr[ str[cnt-1] ][ buf[i] ])
				str[cnt-1] = tr[ str[cnt-1] ][ buf[i] ];
			else {
				bool er = false;

				FORD(k, cnt-1, 0)
					if (del[ str[k] ][ buf[i] ]) {
						er = true;
						break;
					}

				if (!er)
					str[cnt++] = buf[i];
				else
					cnt = 0;
			}
		}


		printf("Case #%d: [", tc);
		if (cnt) printf("%c", str[0]);
		FOR(i, 1, cnt) printf(", %c", str[i]);
		puts("]");
	}

}
