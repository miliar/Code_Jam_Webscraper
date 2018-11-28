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

#define FN "A-large"

#define N 128
int w,n1,n2,g;
PII a[N],b[N];

double get(int n, PII a[N], double w)
{
	int i = 0;
	double res = 0;
	while (i < n-1 && a[i+1].X <= w)
	{
		res += (a[i+1].X-a[i].X)/2.0*(a[i+1].Y+a[i].Y);
		i++;
	}
	if (i==n-1) return res;
	double y = (w-a[i].X)*((a[i+1].Y-a[i].Y)/(double)(a[i+1].X-a[i].X)) + a[i].Y;
	res += (w-a[i].X)/2.0*(y+a[i].Y);
	return res;
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

		scanf("%d%d%d%d",&w,&n1,&n2,&g);
		REP(i,n1)
		{
			scanf("%d%d",&a[i].X,&a[i].Y);
		}
		REP(i,n2)
		{
			scanf("%d%d",&b[i].X,&b[i].Y);
		}
		vector<double> res;
		double left=0,right=w;
		double area = -get(n1,a,w) + get(n2,b,w);
		REP(i,g-1)
		{
			double need = area - (i+1)*area/(double)g;
			REP(step,100)
			{
				double x = (left+right)/2;
				double ar = -get(n1,a,x) + get(n2,b,x);
				if (ar > need)
					right = x;
				else
					left = x;
			}
			res.pb(left);
			right = left;
			left = 0;
		}
		reverse(ALL(res));

		printf("Case #%d:\n",test);
		REP(i,SZ(res))
			printf("%.10lf\n",res[i]);
		fflush(stdout);
	}
	return 0;
}