#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
struct aa{
	int b,e,w;
}a[1010];
int cmp(aa a,aa b){
	return a.w<b.w;
}
int t,tt,x,n,b,e,w,s,r,T;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("3.txt","w",stdout);
	scanf("%d",&T);
	for(int tt=0;tt<T;tt++){
		printf("Case #%d: ",tt+1);
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		memset(a,0,sizeof a);
		for(int i=0;i<n;++i){
			scanf("%d%d%d",&a[i].b,&a[i].e,&a[i].w);
			x-=(a[i].e-a[i].b);
		}
		sort(a,a+n,cmp);
		double ans=0,tmp=t;
		double temp=(double)x/r;
		double ll=x;
		if(temp>tmp){
			double l=ll-tmp*r;
			temp=tmp+l/s;
			tmp=0;
		}else tmp-=temp;
		ans+=temp;
		for(int i=0;i<n;++i){
			double v=a[i].w;	
			ll=a[i].e-a[i].b;
			temp=ll/(v+r);
			if(temp>tmp){
				double l=ll-tmp*(v+r);
				temp=tmp+l/(v+s);
				tmp=0;
			}else tmp-=temp;
			ans+=temp;
		}
		printf("%.10f\n",ans);
	}
	return 0;
}
