#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;

int t,n[2];
#define NAME "B-large"

int read()
{
	int h,m;
	scanf("%d:%d",&h,&m);
	return h*60+m;
}

#define ARRIVE 0
#define DEPARTURE 1

class Event
{
public:
	int time;
	int kind,side;
};

bool operator<(const Event& x, const Event& y)
{
	return make_pair(x.time,x.kind)<make_pair(y.time,y.kind);
}

vector<Event> a;

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		scanf("%d%d%d",&t,&n[0],&n[1]);
		a.clear();
		REP(side,2)
			REP(i,n[side])
			{
				Event e;
				e.side = side;
				e.kind = DEPARTURE;
				e.time = read();
				a.push_back(e);
				e.side = 1-side;
				e.kind = ARRIVE;
				e.time = read()+t;
				a.push_back(e);
			}
		SORT(a);
		int cur[2],res[2];
		CLEAR(cur);
		CLEAR(res);
		REP(i,SZ(a))
		{
			if (a[i].kind==ARRIVE)
				cur[a[i].side]++;
			else
			{
				if (cur[a[i].side]>0)
					cur[a[i].side]--;
				else
					res[a[i].side]++;
			}
		}
		printf("Case #%d: %d %d\n",tst+1,res[0],res[1]);
	}
	return 0;
}
