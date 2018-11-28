#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
using namespace std;

int n, k;
int x[10], y[10], r[10];
double ans;

int main()
{
	freopen("D-small-attempt0.in","rt",stdin);
	freopen("d.out","wt",stdout);
	int T, tt=0;
	scanf("%d",&T);
 	while (tt<T) {
		scanf("%d",&n);
		for(int i=1;i<=n;++i) {
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		}
		if (n==1) ans=r[1];
		else if (n==2) {
			if (r[1]>r[2]) ans=r[1];
			else ans=r[2];
		} else {
			ans=1e17;
		for(int i=1;i<n;++i)
			for(int j=i+1;j<=n;++j) {
				double tmp;
				for(int k=1;k<=n;++k)
					if (k!=i && k!=j) tmp=r[k];
				double xx=x[i]-x[j], yy=y[i]-y[j], rr;
				rr=sqrt(xx*xx+yy*yy)+r[i]+r[j];
				rr/=2;
				if (rr<tmp) tmp=rr;
				if (rr<ans) ans=rr;
		}
		}
		printf("Case #%d: %.6lf\n",++tt, ans);
	}
	return 0;
}