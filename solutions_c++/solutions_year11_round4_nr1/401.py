#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;


struct aa{
	double l,r,s;
} a[10011];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	cin >>t;
	for (int tt=1;tt<=t;tt++){
		double x,w,r,shi;
		int n;
		cin >>x>>w>>r>>shi>>n;
		
		for (int i=1;i<=n;i++){
			cin >>a[i].l>>a[i].r>>a[i].s;
			x-=a[i].r-a[i].l;
		}
		a[++n].l=0;
		a[n].r=x;
		a[n].s=0;
		for (int i=1;i<n;i++) for (int j=i+1;j<=n;j++)	if (a[i].s>a[j].s) swap(a[i],a[j]);
		double ans=0;
		for (int i=1;i<=n;i++){
			if (shi<=1e-10) ans+=double(a[i].r-a[i].l)/(a[i].s+w); else {
				if ((a[i].s+r)*shi>=a[i].r-a[i].l) {
					double tim=a[i].r-a[i].l;
					tim/=a[i].s+r;
					shi-=tim;
					ans+=tim;
				} else {
					a[i].r-=shi*(a[i].s+r);
					ans+=shi;
					shi=0;
					ans+=double(a[i].r-a[i].l)/(a[i].s+w);
				}
			}
		}
		cout <<"Case #"<<tt<<": ";
		printf("%.8lf\n",ans);
	}


}
