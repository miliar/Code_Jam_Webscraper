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
int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	//freopen("A-small-practice.in", "r", stdin); freopen("practice.out","w",stdout);
	int testCase; scanf("%d", &testCase);
	for (int caseID=1; caseID<=testCase; ++caseID) {
		cerr << caseID << " of " << testCase << endl;
		int n, r[40];
		char g[40][41];
		scanf("%d",&n); REP(i,n) scanf("%s", g[i]);
		CLR(r,0); REP(i,n) REP(j,n) if (g[i][j]=='1') r[i]=j;
		int ans=0;
		REP(i,n) {
			int j=i;
			while (r[j]>i) ++j;
			for (int k=j; k>i; --k) r[k]=r[k-1];
			ans+=j-i;
		}
		printf("Case #%d: %d\n", caseID, ans);
	}
}
