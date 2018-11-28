#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
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
#define MCPY(dest,src) memcpy(dest,src,sizeof(src))
template<class T> T checkmax(T &a, T b) {return a=max(a,b);}
template<class T> T checkmin(T &a, T b) {return a=min(a,b);}
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
const double EPS=1e-9;
const double PI=acos(-1);
const int INF=0x3F3F3F3F;

typedef pair<double,double> PT;
int x, s, r, t, n, b[1024], e[1024], w[1024];
PT a[1<<20];
int main(int argc, char *argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		printf("Case #%d: ", test_case_id);
		cin>>x>>s>>r>>t>>n; REP(i,n) cin>>b[i]>>e[i]>>w[i];
		double walk=1.0/s, run=1.0/r;
		REP(i,x) a[i]=PT(run-walk, walk);
		REP(i,n) {
			walk=1.0/(s+w[i]); run=1.0/(r+w[i]);
			FOR(j, b[i], e[i]-1) a[j]=PT(run-walk, walk);
		}
		sort(a, a+x);
		double ans=0; REP(i,x) ans+=a[i].second;
		double left=t;
		REP(i,x) {
			double r=a[i].second+a[i].first;
			checkmin(r,left);
			left-=r;
			ans+=r/(a[i].second+a[i].first)*a[i].first;
		}
		printf("%.7lf\n", ans);
	}
}
