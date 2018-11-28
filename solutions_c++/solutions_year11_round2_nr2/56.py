#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define EPS (1e-9)
#define flt(x,y) ((x)<(y)-EPS)
#define fle(x,y) ((x)<(y)+EPS)
#define fgt(x,y) ((x)>(y)+EPS)
#define fge(x,y) ((x)>(y)-EPS)
#define feq(x,y) (fabs((x)-(y))<EPS)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define x first
#define y second

int T,ca=0;
const int N=2036000;
int a[N];
double INF=1e15;

int main() {
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++ca);
		int d,c,n=0;
		scanf("%d%d",&c,&d);
		while (c--) {
			int x,y;
			scanf("%d%d",&x,&y);
			while(y--) a[n++]=x;
		}
		double lo=0, hi=INF;
		FOR(iter,0,200) {
			double md=(hi+lo)*0.5;
			double x=-INF;
			bool ok=1;
			FOR(i,0,n) {
				if(fge(a[i],x+d)) {
					x=max(a[i]-md, x+d);
				}else{
					double y=min(a[i]+md,x+d);
					if(flt(y,x+d)) { ok=0; break; }
					x=y;
				}
			}
			if(ok) hi=md;
			else lo=md;
		}
		printf("%.15f\n", lo);
	}
	return 0;
}
