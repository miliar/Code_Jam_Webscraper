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

int w, l, u, g, xl[128], yl[128], xu[128], yu[128];
double ly[1024], uy[1024], h[1024], a[1024];
int main(int argc, char *argv[])
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		//fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		scanf("%d%d%d%d", &w, &l, &u, &g);
		REP(i,l) scanf("%d%d", &xl[i], &yl[i]);
		FOR(i,1,l-1) {
			int x1=xl[i-1], x2=xl[i], y1=yl[i-1], y2=yl[i];
			FOR(x,x1,x2) {
				ly[x]=y1+(double)(y2-y1)*(x-x1)/(x2-x1);
			}
		}
		REP(i,u) scanf("%d%d", &xu[i], &yu[i]);
		FOR(i,1,u-1) {
			int x1=xu[i-1], x2=xu[i], y1=yu[i-1], y2=yu[i];
			FOR(x,x1,x2) {
				uy[x]=y1+(double)(y2-y1)*(x-x1)/(x2-x1);
			}
		}
		FOR(i,0,w) h[i]=uy[i]-ly[i];
		a[0]=0;
		FOR(i,1,w) a[i]=a[i-1]+(h[i]+h[i-1])/2;
		printf("Case #%d:\n", test_case_id);
		double s=a[w]/g;
		FOR(i,1,g-1) {
			double ar=s*i;
			int id=lower_bound(a,a+w+1,ar-EPS)-a-1;
			ar-=a[id];
			double A=h[id+1]-h[id], B=2*h[id], C=-2*ar;
			double left=(-B+sqrt(B*B-4*A*C))/2/A;
			printf("%.6lf\n", id+left);
		}

	}
}
