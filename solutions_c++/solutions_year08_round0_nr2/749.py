#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))


/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

struct E{
	int tm, idx, val;
	E(int _tm, int _idx, int _val) : tm(_tm), idx(_idx), val(_val) {}
	bool operator<(const E &a) const {
		if(tm != a.tm) return tm > a.tm;
		return val < a.val;
	}
};

void solve(void)
{
	int T, NA, NB;
	scanf("%d %d %d\n", &T, &NA, &NB);
	
	priority_queue<E> pq;
	REP(i, NA+NB) {
		int a, b, c, d;
		scanf("%d:%d %d:%d\n", &a, &b, &c, &d);

		int t1 = a*60 + b, t2 = c*60 + d;
		pq.push( E(t1, (i < NA ? 0 : 1), -1));
		pq.push( E(t2+T, (i < NA ? 1 : 0), +1));
	}

	int cnt[2], mn[2];
	RESET(cnt, 0); RESET(mn, 0);

	while(!pq.empty()) {
		E e = pq.top(); pq.pop();
		cnt[e.idx] += e.val;

		mn[e.idx] = min(mn[e.idx], cnt[e.idx]);
	}

	printf("%d %d\n", -mn[0], -mn[1]);
}

int main(void)
{
	int D, T = 1;
	scanf("%d\n", &D);
	while(D--) {printf("Case #%d: ", T++); solve(); }
	return (0);
}
