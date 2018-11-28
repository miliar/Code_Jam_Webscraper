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

#define NAME "B-large"

#define N 128
int n,m,del,ins;
int a[N];
int d[N][256];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"Case %d: \n",test);

		scanf("%d%d%d%d",&del,&ins,&m,&n);
		REP(i,n)
			scanf("%d",&a[i]);
		CLEAR(d);
		REP(i,n+1)
		{
			//insert
			if (m>0)
				REP(j1,256) REP(j2,256) if (j1!=j2)
					d[i][j1]=min(d[i][j1],d[i][j2]+((abs(j1-j2)+m-1)/m)*ins);
			if (i==n) break;
			REP(j,256)
				d[i+1][j]=d[i][j]+del;
			REP(j1,256) REP(j2,256)
				if (abs(j2-j1) <= m)
					d[i+1][j1] = min(d[i+1][j1], d[i][j2]+abs(a[i]-j1));
		}
		int res=INF;
		REP(j,256)
			res=min(res,d[n][j]);
		printf("Case #%d: %d\n",test,res);
	}
	return 0;
}