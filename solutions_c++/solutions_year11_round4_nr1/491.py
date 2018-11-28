/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair
#define DEBUG 1
#define PRINT(x...) DEBUG && printf(x)

int T, N;
double X, S, R, t;

struct lho
{
	double x, v;
	bool operator<(const lho& o) const
	{
		return v < o.v;
		return x*o.v > o.x*v;
	}
};

lho data[10000];

bool ok(double test)
{
	double cur = 0;
	double bonus = t;
	
	REP(i, N+1)
	{
		double req = data[i].x / (data[i].v-S+R);
		if (req <= bonus)
		{
			cur += req;
			bonus -= req;
		}
		else
		{
			cur += bonus;
			double rem = data[i].x - (bonus*(data[i].v-S+R));
			cur += rem/data[i].v;
			bonus = 0;
		}
	}
	
	return cur <= test;
}

int main()
{
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	cin >> T;
	REP(tc, T)
	{
		cin >> X >> S >> R >> t >> N;
		double walkways = 0;
		REP(i, N)
		{
			double b, e, w;
			cin >> b >> e >> w;
			data[i] = (lho){e-b, S+w};
			walkways += e-b;
		}
		
		data[N] = (lho){X-walkways, S};
		
		sort(data, data+N+1);
		
		double lo = 0, hi = 1e20, mid;
		REP(zzz, 100)
		{
			mid = (lo+hi)/2;
			if (ok(mid))
				hi = mid;
			else
				lo = mid;
		}
		printf("Case #%d: %.10lf\n", tc+1, mid);
	}
}
