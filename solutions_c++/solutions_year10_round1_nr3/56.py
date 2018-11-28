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

#define NAME "C-large"

bool solve(int x, int y)
{
	if (x>y) swap(x,y);
	if (x==y) return false;
	if (x==0||y==0) return true;
	int len = (y-1)/x;
	if (len>=2) return true;
	return !solve(y-x,x);
}

const double phi = (sqrt(5.0)-1)/2;

int main()
{
/*	//freopen("qqq.txt","w",stdout);
	while (1) {
	int a;
	scanf("%d",&a);
	FOR(b,1,100) printf("%d - %d\n",b,solve(a,b));
	int prev = 1;
	int q=0;
	FOR(b,1,3*a)
	{
		int x = solve(a,b);
		if (x!=prev) { q++; printf("%d\n",b-x);}
		prev=x;
	}
	int bb1 = ceil(phi*a);
	int bb2 = floor((phi+1)*a);
	printf("%d\n%d\n%d\n",bb1,bb2,q);
}
	return 0;
/**/
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"Case %d: \n",test);

		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		LL res=0;
		FOR(a,a1,a2)
		{
			int bb1 = ceil(phi*a);
			int bb2 = floor((phi+1)*a);
			bb1 = max(bb1,b1);
			bb2 = min(bb2,b2);
			res += b2-b1+1 - max(0,bb2-bb1+1);
		}
		printf("Case #%d: %lld\n",test,res);
	}
	return 0;
}