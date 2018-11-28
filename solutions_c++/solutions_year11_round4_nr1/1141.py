#include<stdio.h>
#include<algorithm>
#include<iostream>
struct ee{double l,w;}a[1010];
bool cmp(struct ee x,struct ee y){
	return x.w<y.w;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("AB.txt","w",stdout);
	int t,T,n,i;
	double ans,q,ti,l,r,s,x,R;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&ti,&n);
		a[n].l=x;
		a[n].w=0;
		for(i=0;i<n;i++){
			scanf("%lf%lf%lf",&l,&R,&a[i].w);
			a[i].l=R-l;
			a[n].l-=R-l;
		}
		n++;
		std::sort(a,a+n,cmp);
		ans=0;
		for(i=0;i<n;i++){
			if(ti==0){
				ans+=a[i].l/(a[i].w+s);
				continue;
			}
			q=a[i].l/(a[i].w+r);
			if(q<=ti){
				ti-=q;
				ans+=q;
			}
			else{
				ans+=ti;
				ans+=(a[i].l-(a[i].w+r)*ti)/(a[i].w+s);
				ti=0;
			}
		}
		printf("Case #%d: %.8lf\n",t,ans);
	}
}
