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
#define INF 1000000000
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

template<class T> inline T gcd(T a,T b) {
	if(a<0)a=-a; if(b<0)b=-b; if(a<b)swap(a,b);
	while (b) {T t = b; b=a%b; a=t;} return a; }

#define NAME "B-small-attempt0"

LL len;
int n;
int a[128];
#define MX 200000
int d[MX];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		fprintf(stderr,"Test #%d\n",tst+1);

		scanf("%lld%d",&len,&n);
		REP(i,n) scanf("%d",a+i);
		int g = 0;
		REP(i,n)
			g=gcd(g,a[i]);
		LL res = len+1000;
		if (len % g != 0)
			res = -1;
		else
		{
			int mx = *max_element(a,a+n);
			REP(i,MX) d[i]=INF;
			d[0]=0;
			REP(i,n) REP(x,MX-a[i])
				d[x+a[i]]=min(d[x+a[i]],d[x]+1);
			REP(i,MX) if ((len-i)%mx == 0 && d[i]<INF)
				res=min(res,(len-i)/mx+d[i]);
		}
		printf("Case #%d: ",tst+1);
		if (res==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%lld\n",res);
	}
	return 0;
}