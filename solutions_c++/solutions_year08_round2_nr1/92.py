#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b) x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) c.begin(), c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for (VAR(i,c.begin()); i != c.end(); ++i)
#define PB push_back
#define ST first
#define ND second
const int MAXN = 100;
int x[MAXN], y[MAXN];
int main()
{
	int N;
	scanf("%d",&N);
	REP(z,N) {
		int n;
		LL A,B,C,D,x0,y0,X,Y,M;
		scanf("%d%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		x[0] = x0;
		y[0] = y0;
		FOR(i,1,n) {
			x[i] = (A*x[i-1]+B)%M;
			y[i] = (C*y[i-1]+D)%M;
		}
		int res = 0;
		FOR(i,0,n) FOR(j,i+1,n) FOR(k,j+1,n) { if ((x[i]+x[j]+x[k])%3 == 0 && (y[i]+y[j]+y[k]) % 3 == 0) res++; }
		printf("Case #%d: %d\n",z+1,res);
	}
	return 0;
}
