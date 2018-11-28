#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

struct node{
	int p1,p2,p3;
};

int n,m,p,q,k,s,len,tt,rr;
node a[1020];

bool cmp(node a,node b){
	return a.p3<b.p3;
}

int main(){
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);

	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;++cas){
		scanf("%d%d%d%d%d",&len,&s,&rr,&tt,&n);
		double t=tt,r=rr,p=s;
		for (int i=1;i<=n;++i) scanf("%d%d%d",&a[i].p1,&a[i].p2,&a[i].p3);
		a[0].p1=0;a[0].p2=a[1].p1;a[0].p3=0;
		a[++n].p1=a[n-1].p2;a[n].p2=len;a[n].p3=0;
		int pp=n;
		for (int i=0;i<pp;++i)
		 if (a[i].p2!=a[i+1].p1){
			a[++n].p1=a[i].p2;
			a[n].p2=a[i+1].p1;
			a[n].p3=0;
		 }
		sort(a,a+n+1,cmp);
		double ans=0;
		for (int i=0;i<=n;++i){
			double tmp=a[i].p2-a[i].p1;
			if (tmp/(r+a[i].p3) < t || (fabs(tmp/(r+a[i].p3)-t)<1e-8)){ 
				ans+=tmp/(r+a[i].p3);
				t-=tmp/(r+a[i].p3);
			}else{
				ans+=t;
				tmp-=(r+a[i].p3)*t;
				t=0;
				ans+=tmp/(p+a[i].p3);
			}
		}
		printf("Case #%d: %.10f\n",cas,ans);
	}
	return 0;
}
