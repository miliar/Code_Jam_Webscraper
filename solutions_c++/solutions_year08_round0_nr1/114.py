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

#define NAME "A-large"
char buf[1024];
int n,m;
vector<string> a,b;
int d[1024][1024];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);
	
	gets(buf);
	int tests;
	sscanf(buf,"%d",&tests);
	REP(tst,tests)
	{
		gets(buf);
		sscanf(buf,"%d",&n);
		a.clear();
		REP(i,n)
		{
			gets(buf);
			a.push_back(string(buf));
		}
	
		gets(buf);
		sscanf(buf,"%d",&m);
		b.clear();
		REP(i,m)
		{
			gets(buf);
			b.push_back(string(buf));
		}

		REP(i,n) REP(j,m+1)
			d[i][j]=1000000000;
		REP(i,n)
			d[i][0]=0;
		REP(j,m)
		{
			REP(i,n)
				if (b[j]!=a[i])
				{
					REP(ii,n)
						d[i][j+1] = min(d[i][j+1], d[ii][j]+((i!=ii)?1:0));
				}
		}
		int res=1000000000;
		REP(i,n)
			res=min(res,d[i][m]);
		printf("Case #%d: %d\n",tst+1,res);
	}
	return 0;
}
