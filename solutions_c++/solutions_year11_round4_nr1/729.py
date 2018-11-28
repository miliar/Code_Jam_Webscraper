#include <iostream>
#include <algorithm>
#include <utility>
#include <cstdio>
using namespace std;
#define xx first
#define yy second
typedef pair<double,double> PII;
typedef pair<PII,double> PIII;

PIII a[1010];
PII b[2010];

int main() {
//	freopen("a.in","r",stdin);
//	freopen("a.out","w",stdout);
	
	int T,n;
	double x,s,r,t;
	cin>>T;
	for (int c0=1;c0<=T;++c0) {
		cin>>x>>s>>r>>t>>n;
		for (int i=1;i<=n;++i) cin>>a[i].xx.xx>>a[i].xx.yy>>a[i].yy;
		sort(a+1,a+1+n);
		a[0].xx.yy=0; a[n+1].xx.xx=x;
		
		int m=0;
		for (int i=n;i>=0;--i) if (a[i+1].xx.xx>a[i].xx.yy) b[++m].xx=0, b[m].yy=a[i+1].xx.xx-a[i].xx.yy;
		for (int i=n;i>=1;--i) b[++m].xx=a[i].yy, b[m].yy=a[i].xx.yy-a[i].xx.xx;
		sort(b+1,b+1+m);
		
		double ans=0;
		for (int i=1;i<=m;++i) {
			if (t<1e-8)
			    ans+=b[i].yy/(b[i].xx+s);
			else {
				double d=b[i].yy/(b[i].xx+r);
				if (d<t+1e-8)
					t-=d, ans+=d;
				else
				    ans+=t+(b[i].yy-(b[i].xx+r)*t)/(b[i].xx+s),
				    t=0;
			}
		}
		printf("Case #%d: %.8f\n",c0,ans);
	}
}
