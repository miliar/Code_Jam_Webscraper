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

#define FN "C-small-attempt0"

#define N 128
int n,m;
char a[N][N];

const char* str = "-|\\/";
const int dx[4] = {0,1,1,1};
const int dy[4] = {1,0,1,-1};

#define MOD 1000003

int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"*");

		scanf("%d%d",&n,&m);
		REP(i,n)
			scanf("%s",a[i]);

		int res = 0;
		REP(mask,1<<(n*m))
		{
			bool used[50][50];
			CLEAR(used);
			REP(is,n) REP(js,m)
			{
				int x = is;
				int y = js;
				while (!used[x][y])
				{
					used[x][y] = true;
					int ind = -1;
					REP(j,4)
						if (str[j] == a[x][y])
							ind = j;
					if (ind == -1)
						fprintf(stderr,"BAD\n");
					int xx = x + dx[ind]*(mask&(1<<(x*m+y)) ? 1 : -1);
					int yy = y + dy[ind]*(mask&(1<<(x*m+y)) ? 1 : -1);
					x = (xx+n)%n;
					y = (yy+m)%m;
				}
				if (x != is || y != js)
				{
					goto bad;
				}
			}
			++res;
			bad:;
		}

		res%=MOD;
		printf("Case #%d: ",test);
		printf("%d\n",res);
		fflush(stdout);
	}
	return 0;
}