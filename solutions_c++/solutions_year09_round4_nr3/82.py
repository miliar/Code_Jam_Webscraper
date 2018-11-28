#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CONTAIN(container, it) (container.find(it)!=container.end())
#define CLR(c,n) memset(c,n,sizeof(c))
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
const int INF=1000000000;
const double EPS=1e-10;
const double PI=acos(-1);
int n, k, p[100][25];
bool g[100][100];
int c[100], nc;
int best;
int dfs(int id) {
	if (nc>=best) return best;
	if (id>=n) return best=nc;
	int ans=best;
	bool v[nc]; CLR(v,0);
	REP(i,id) if (g[i][id]) v[c[i]]=true;
	REP(i,nc) if (!v[i]) {
		c[id]=i;
		ans<?=dfs(id+1);
	}
	c[id]=nc++;
	ans<?=dfs(id+1);
	--nc;
	return ans;
}
int main()
{
	//freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	//freopen("C-small-practice.in", "r", stdin); freopen("practice.out","w",stdout);
	int testCase; scanf("%d", &testCase);
	for (int caseID=1; caseID<=testCase; ++caseID) {
		//cerr << caseID << " of " << testCase << endl;
		scanf("%d%d", &n, &k); REP(i,n) REP(j,k) scanf("%d", &p[i][j]);
		CLR(g,0);
		REP(i,n) REP(j,i) {
			if (p[i][0]==p[j][0]) g[i][j]=g[j][i]=true;
			else if (p[i][0]<p[j][0]) {
				REP(l,k) if (p[i][l]>=p[j][l]) {g[i][j]=g[j][i]=true; break;}
			} else {
				REP(l,k) if (p[i][l]<=p[j][l]) {g[i][j]=g[j][i]=true; break;}
			}
		}
		nc=0; CLR(c,-1); best=n;
		printf("Case #%d: %d\n", caseID, dfs(0));
	}
}
