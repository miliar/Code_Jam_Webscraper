// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 1010
using namespace std;
const double eps=1e-12;
struct P {
	double len,w;
	P(){}
	P( int _len, int _w ):len(_len),w(_w){}
	void read() {
		double st,ed;
		scanf("%lf%lf%lf",&st,&ed,&w);
		len=ed-st;
	}
} p[N];
bool cp( P a, P b ) { return a.w<b.w; }
double x,s,r,t;
int n;
void input() {
	scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
	for ( int i=0; i<n; i++ ) p[i].read();
	int sum=0;
	for ( int i=0; i<n; i++ ) sum+=p[i].len;
	p[n++]=P(x-sum,0);
	sort(p,p+n,cp);
}
void solve() {
	static int cas=0;
	double ans=0;
	for ( int i=0; i<n; i++ ) {
		//printf("%d: %f,%f\n",i,p[i].len,p[i].w);
		if ( t<eps ) ans+=p[i].len/(s+p[i].w);
		else if ( t>=p[i].len/(r+p[i].w) ) {
			double now=p[i].len/(r+p[i].w);
			ans+=now;
			t-=now;
		} else {
			double tmp=t*(r+p[i].w);
			ans+=t;
			ans+=(p[i].len-tmp)/(s+p[i].w);
			t=0;
		}
	}
	printf("Case #%d: %.9f\n",++cas,ans);
}
int main()
{
	int T;
	scanf("%d",&T);
	while ( T-- ) {
		input();
		solve();
	}
	return 0;
}
