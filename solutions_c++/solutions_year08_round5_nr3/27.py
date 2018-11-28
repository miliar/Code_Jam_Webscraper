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
typedef long long LL;

#define NAME "C-small-attempt0"

#define N 10
int n,m;
bool br[N][N];
int line[N];
int d[20][1<<N];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		scanf("%d%d",&n,&m);
		CLEAR(line);
		REP(i,n) REP(j,m)
		{
			char c;
			do c = getc(stdin);
			while (c!='.'&&c!='x');
			br[i][j]=c=='x';
			if (c=='x')
				line[i] |= 1<<j;
		}
		CLEAR(d);
		REP(i,n)
		{
			REP(msk,1<<m) if ((line[i] & msk)==0)
			{
				bool bad=false;
				REP(j,m-1)
					if ((msk & (1<<j)) != 0 && (msk & (1<<(j+1))) != 0)
						bad=true;
				if (bad) continue;
				int cnt=0;
				for (int x = msk; x!=0; x&=x-1)
					cnt++;
				REP(msk2,1<<m)
					if ((msk2 & (msk<<1)) == 0 && (msk2 & (msk>>1)) == 0)
						d[i+1][msk] = max(d[i+1][msk],d[i][msk2]+cnt);
			}
		}
		int res=0;
		REP(msk,1<<m)
			res=max(res,d[n][msk]);

		printf("Case #%d: %d\n",tst+1,res);
	}
	return 0;
}
