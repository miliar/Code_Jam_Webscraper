#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <list>
#include <stack>
#include <set>
#include <map>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof( V.begin() ) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

struct chick {
	int loc, speed;
};

const int MAXN = 1000;

chick T[MAXN];
bool da_sie[MAXN];

void testcase(int v) {
	printf("Case #%d: ", v);
	int n, k, b, t;
	scanf("%d%d%d%d", &n, &k, &b, &t);
	REP(i,n) scanf("%d", &T[i].loc);
	REP(i,n) scanf("%d", &T[i].speed);
	REP(i,n) da_sie[i] = false;
	reverse(T,T+n);
	int ile_swapow = 0, ile_gosci = 0;
	int nie_da_sie = 0;
	REP(i,n) {
		if(T[i].loc + T[i].speed * t >= b) da_sie[i] = true;
		if(da_sie[i]) {
			if(ile_gosci < k) {
				++ile_gosci;
				ile_swapow += nie_da_sie;
			}
		} else ++nie_da_sie;
	}
	if(ile_gosci < k) printf("IMPOSSIBLE\n");
	else printf("%d\n", ile_swapow);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i,t) testcase(i+1);
	return 0;
}