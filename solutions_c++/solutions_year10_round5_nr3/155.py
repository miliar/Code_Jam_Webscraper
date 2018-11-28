#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <cassert>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

const int LGT=2300000;
int tak[LGT];
int siz[LGT];
queue<int> td;
ll moves;

void cleanall() {
	while (!td.empty()) td.pop();
	REP (i, LGT) tak[i] = 0;
	REP (i, LGT) {
		if (siz[i] > 1) {
			int lgt = 1;
			while (siz[i + 2*lgt] > 1) lgt++;
			for (int j = i; j < i + 2*lgt; j+=2) {siz[j] -= 2;}
			for (int j = i-1; j < i + 2*lgt; j++) {siz[j] += 1;}
			siz[i + lgt - 1] -= 1;
			moves += (((ll) lgt) * (((ll) lgt) + 1LL)) / 2LL;
		}
	}
	REP (i, LGT) if (siz[i] > 1) {
		td.push(i);
		tak[i] = 1;
	}
}

int main () {
  int number_of_tests;
  scanf("%d", &number_of_tests);
  REP (test_number, number_of_tests) {
    printf("Case #%d: ", test_number+1);
		REP (i, LGT) {tak[i] = 0; siz[i] = 0;}
		while(!td.empty()) td.pop();
    int N;
		scanf("%d", &N);
		moves = 0LL;
		int x, s;
		REP (i, N) {
			scanf("%d %d", &x ,&s);
			siz[x + LGT/2] += s;
			if (siz[x+LGT/2] > 1 && !tak[x+LGT/2]) {
				td.push(x+LGT/2);
				tak[x+LGT/2] = 1;
			}
		}
    int counter = 0;
		int ok = 1;
		while (ok) {
//			if (counter % 500 == 0) cleanall();
			counter++;
			if (td.empty()) {
				printf("%lld\n", moves);
				ok = 0;
			} else {
				int tm = td.front();
				td.pop();
				tak[tm] = 0;
				int del = siz[tm] / 2;
				moves += (ll) del;
				siz[tm] -= 2*del;
				siz[tm+1] += del;
				siz[tm-1] += del;
				if ((siz[tm+1] > 1) && !tak[tm+1]) {td.push(tm+1); tak[tm+1] = 1;}
				if ((siz[tm-1] > 1) && !tak[tm-1]) {td.push(tm-1); tak[tm-1] = 1;}
			}
		}
		REP (i, LGT) assert(siz[i] < 2);
  }
  return 0;
}

