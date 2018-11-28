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

#define FN "A-large"//-small-attempt0

#define N 1024
int len,S,R,ttt,n;
PII a[N];

int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		scanf("%d%d%d%d%d",&len,&S,&R,&ttt,&n);
		REP(i,n)
		{
			int x,y,ww;
			scanf("%d%d%d",&x,&y,&ww);
			a[i].second=y-x;
			a[i].first=ww;
			len-=y-x;
		}
		a[n].first=0;
		a[n].second=len;
		++n;
		sort(a,a+n);
		double T = ttt;
		double res = 0;
		REP(i,n)
		{
			int x = a[i].second;
			int w = a[i].first;
			double rt = min(T, x/(double)(w+R));
			T-=rt;
			double xx = a[i].second - rt*(w+R);
			double st = xx/(double)(w+S);
			res += st+rt;
		}
		printf("Case #%d: %.10lf\n",test,res);
	}
	return 0;
}