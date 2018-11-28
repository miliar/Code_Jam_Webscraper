/* standard includes {{{ */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cmath>
#include <complex>

#include <iostream>
#include <sstream>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/* }}} */

/* defines: REP, FOR, FORD, FORE, FORER, CLEAR, SIZE {{{ */
#define REP(i,n) for (__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for (__typeof(b) i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (__typeof(a) i=(a); i>=(b); --i)
#define FORE(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define FORER(it,c) for (__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define CLEAR(t,v) memset((t),v,sizeof(t))
#define SIZE(c) ((int)((c).size()))
/* }}} */

class moo
{
	public:
		int t, where, arr;
		moo(int _t=0, int _w=0, int _a=0): t(_t), where(_w), arr(_a) {}

		bool operator<(const moo &b) const
		{
			if (t!=b.t) return t<b.t;
			if (arr!=b.arr) return arr>b.arr;
			return where<b.where;
		}
};

int main(void)
{
	int cas;
	scanf("%d ", &cas);

	REP(ca,cas)
	{
		int T, NA, NB;
		scanf("%d %d %d ", &T, &NA, &NB);

		vector<moo> P;

		REP(i,NA)
		{
			int a, b, c, d;
			scanf("%d:%d %d:%d ", &a, &b, &c, &d);
			P.push_back(moo(60*a+b, 0, 0));
			P.push_back(moo(60*c+d+T, 1, 1));
		}
		REP(i,NB)
		{
			int a, b, c, d;
			scanf("%d:%d %d:%d ", &a, &b, &c, &d);
			P.push_back(moo(60*a+b, 1, 0));
			P.push_back(moo(60*c+d+T, 0, 1));
		}

		sort(P.begin(), P.end());

		int N=SIZE(P), p[2] = {0,0}, q[2] = {0,0};
		REP(i,N)
		{
			if (P[i].arr==1)
			{
				p[P[i].where]++;
			}
			else
			{
				if (p[P[i].where]>0)
				{
					p[P[i].where]--;
				}
				else
				{
					q[P[i].where]++;
				}
			}
		}
		printf("Case #%d: %d %d\n", ca+1, q[0], q[1]);
	}

	return 0;
}
