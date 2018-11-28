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
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define x first
#define y second

const int MX=2036000;
LL X,S,R,t1,N;
int rem;
pair<int,int> p[MX];	// spd, len

double f(int n) {
	double ans=0;
	double t=t1;
	FOR(i,0,n) {
			double ti = (double)(p[i].y) / (p[i].x+R);
			if(ti>t) {
				double di = t * (p[i].x+R);
				double dr = p[i].y - di;
				ans+=t;
				ans+=dr/(p[i].x+S);
				t=0;
			}else{
				t-=ti;
				ans+=ti;
			}
	}
	return ans;
}

int main() {
	int T,ca=0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d:", ++ca);
		scanf("%lld%lld%lld%lld%lld",&X,&S,&R,&t1,&N);
		int rem = X;
		FOR(i,0,N) {
			int x,y,w;
			scanf("%d%d%d",&x,&y,&w);
			p[i]=pii(w,(y-x));
			rem-=(y-x);
		}
		p[N++]=pii(0,rem);

		sort(p,p+N);
		double a1=f(N);
		reverse(p,p+N);
		double a2=f(N);
		printf(" %.15f\n", min(a1,a2));
	}
	return 0;
}
