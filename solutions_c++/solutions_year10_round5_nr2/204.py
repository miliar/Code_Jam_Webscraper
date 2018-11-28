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

const int max_B = 10005;
const int max_n = 100;
int kolesie[max_n];
int osiagalne[max_B];

LL duzo = (LL)INT_MAX * (LL) INT_MAX;

void testcase(int v) {
	printf("Case #%d: ", v);
	LL L, n;
	cin >> L >> n;
	REP(i,n)
		cin >> kolesie[i];
	int byczek = kolesie[0];
	REP(i,n) byczek = max(byczek, kolesie[i]);
	REP(i,max_B) osiagalne[i] = INT_MAX;
	osiagalne[0] = 0;
	REP(i,n) REP(j,max_B) {
		if(osiagalne[j] == INT_MAX) continue;
		if(kolesie[i] + j >= max_B) continue;
		osiagalne[kolesie[i]+j] = min(osiagalne[kolesie[i]+j], osiagalne[j]+1);
	}
	LL res = duzo;
	int bescior = -1;
	REP(i,max_B) if(osiagalne[i] != INT_MAX && (i%byczek == L%byczek)) {
		LL tmp_res = res;
		res = min(res, osiagalne[i] + (L-i)/byczek);
		if(tmp_res != res) bescior = i;
	}
	//printf("BESCIOR: %d\n", bescior);
	if(res == duzo) printf("IMPOSSIBLE\n");
	else printf("%lld\n", res);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i,t) testcase(i+1);
	return 0;
}

