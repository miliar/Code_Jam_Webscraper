#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define MAX_N 100000
#define inf 1000000000

int n, m, v[MAX_N], c[MAX_N], g[MAX_N], V;
int mi[MAX_N][2];

int solve(int p, int b) {
	int &res=mi[p][b];
	if (res!=-1) return res;
	res=inf;
	if (p>m) {
		if (v[p]==b) return res=0;
		else return res=inf;
	} else {
		int opOR=inf;
		if (b==0) opOR=min(opOR,solve(2*p,0)+solve(2*p+1,0));
		else {
			opOR=min(opOR,solve(2*p,0)+solve(2*p+1,1));
			opOR=min(opOR,solve(2*p,1)+solve(2*p+1,0));
			opOR=min(opOR,solve(2*p,1)+solve(2*p+1,1));
		}
		int opAND=inf;
		if (b==1) opAND=min(opAND,solve(2*p,1)+solve(2*p+1,1));
		else {
			opAND=min(opAND,solve(2*p,0)+solve(2*p+1,1));
			opAND=min(opAND,solve(2*p,1)+solve(2*p+1,0));
			opAND=min(opAND,solve(2*p,0)+solve(2*p+1,0));
		}
		if (g[p]==1) {
			res=min(res,opAND);
			if (c[p]==1) res=min(res,opOR+1);
		} else {
			res=min(res,opOR);
			if (c[p]==1) res=min(res,opAND+1);
		}
		return res;
	}
}

int main()
{
	int t; scanf("%d", &t);
	FOR(tC,1,t) {
		scanf("%d %d", &n, &V);
		m=(n-1)/2;
		FOR(i,1,n) {
			if (i<=m) scanf("%d %d", &g[i], &c[i]);
			else scanf("%d", &v[i]);
		}
		printf("Case #%d: ", tC);
		CLR(mi,-1);
		int res = solve(1,V);
		if (res==inf) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}
