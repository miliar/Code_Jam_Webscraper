#include<iostream>
#include<iomanip>
#include<cstdio>
#include<algorithm>
using namespace std;
struct FP{
	long s,v;
	inline void init(const long _s,const long _v){
		s=_s,v=_v;
		}
}F[3000001];
inline bool cmp(const FP &x,const FP &y){
	return x.v<y.v;
}
long T,TT;
long double ans;
long x,s,r,t,n,last,i,j,k,l;
double tt,f1;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%ld",&T);
	while(TT++!=T){
		scanf("%ld%ld%ld%ld%ld",&x,&s,&r,&t,&n),l=last=0,ans=0,r-=s;
		while(n--)
			scanf("%ld%ld%ld",&i,&j,&k),F[last++].init(i-l,s),F[last++].init(j-i,s+k),l=j;
		F[last++].init(x-l,s);
		sort(F,F+last,cmp);
		tt=t;
		for(i=0;i<last;++i){
			if((double)F[i].s/(F[i].v+r)<=tt)
				f1=(double)F[i].s/(F[i].v+r),tt-=f1,ans+=f1;
			else{
				f1=(F[i].v+r)*tt,ans+=tt,tt=0;
				ans+=(F[i].s-f1)/F[i].v;
				++i;break;
				}
			}
		for(;i<last;++i)
			ans+=(long double)F[i].s/F[i].v;
		cout<<"Case #"<<TT<<": "<<fixed<<setprecision(10)<<ans<<endl;
		}
	cin>>T;
	return 0;
}
