#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
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

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

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
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define FN "B-large"

#define N 512
int n,m,one;
int a[N][N],ax[N][N],ay[N][N];
int d[N][N],dx[N][N],dy[N][N];

void process(int a[N][N], int d[N][N])
{
	REP(i,n) REP(j,m)
	{
		d[i+1][j+1] = a[i][j] + d[i][j+1] + d[i+1][j] - d[i][j];
	}
}

int get(int a[N][N], int d[N][N], int i, int j, int k)
{
	int ii = i+k;
	int jj = j+k;
	return d[ii][jj]-d[i][jj]-d[ii][j]+d[i][j] - a[ii-1][jj-1] - a[i][jj-1] - a[ii-1][j] - a[i][j];
}

int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"*");
		scanf("%d%d%d",&n,&m,&one);
		REP(i,n) REP(j,m)
		{
			char c;
			do c = getc(stdin);
			while (!isdigit(c));
			a[i][j] = c-'0';
		}
		REP(i,n) REP(j,m)
		{
			ax[i][j] = a[i][j]*i;
			ay[i][j] = a[i][j]*j;
		}
		CLEAR(d);
		CLEAR(dx);
		CLEAR(dy);
		process(a,d);
		process(ax,dx);
		process(ay,dy);
		int res = -1;
		for (int k = min(n,m); k >= 3; --k)
		{
			REP(i,n-k+1) REP(j,m-k+1)
			{
				LL s = get(a,d,i,j,k);
				LL sx = get(ax,dx,i,j,k);
				if (2*sx == s*(2*i + k-1))
				{
					LL sy = get(ay,dy,i,j,k);
					if (2*sy == s*(2*j + k-1))
					{
						res = k;
						goto ok;
					}
				}
			}
		}
		ok:
		printf("Case #%d: ",test);
		if (res == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n",res);
	}
	return 0;
}