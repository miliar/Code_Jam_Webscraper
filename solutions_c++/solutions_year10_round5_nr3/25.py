#include <stdio.h>
#include <algorithm>
#include <utility>
using namespace std;

#define NL 2010061320100613LL

typedef long long ll;

pair<pair<ll,ll>,pair<ll,ll> > stk[100010];
int height;

//[l,r], s,k;

ll p[100010],v[100010];

ll divdn(ll a,ll b){ //b>0
	if(a>=0)return a/b;
	else return -((-a+b-1)/b);
}

ll divup(ll a, ll b){
	return -divdn(-a,b);
}

ll ssq(ll a){
	return a*(a+1)*(2*a+1)/6;
}

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%lld%lld",&p[i],&v[i]); //coordinates are sorted
		
		height=0;
		for(int i=0;i<n;i++){
			ll l,r,s,k;
			l=v[i]/2+p[i];
			r=-v[i]/2+p[i];
			s=p[i]*v[i];
			k=v[i];
			for(;height>0;){
				pair<pair<ll,ll>,pair<ll,ll> > tp=stk[--height];
				ll tr=tp.first.first;
				ll tl=tp.first.second;
				ll ts=tp.second.first;
				ll tk=tp.second.second;
				if(tl<r){
					stk[height++]=tp;break;
				}else{
					ll nr,nl,ns,nk;
					ns=ts+s;
					nk=tk+k;
					if(nk%2==0){
						nr=-nk/2+divdn(ns+nk/2,nk);
						nl=nk/2+divup(ns-nk/2,nk);
					}else{
						nr=-nk/2+divdn(ns,nk);
						nl=nk/2+divup(ns,nk);
					}
					r=nr;l=nl;s=ns;k=nk;
				}
			}
			stk[height++]=make_pair(make_pair(r,l),make_pair(s,k));
/*			for(int j=0;j<height;j++){
				printf("%lld-%lld %lld ko\n",r,l,k);
			}*/
		}
		ll ans=0;
		for(int i=0;i<n;i++)ans-=p[i]*p[i]*v[i];
		for(;height>0;){
			pair<pair<ll,ll>,pair<ll,ll> > tp=stk[--height];
			ll r=tp.first.first;
			ll l=tp.first.second;
			ll s=tp.second.first;
			ll k=tp.second.second;
			ll eng=ssq(l)-ssq(r-1);
			if(k!=l-r+1);{
				ll pos=(l+r)*(l-r+1)/2-s;
				eng-=(pos*pos);
			}
			ans+=eng;
		}
		ans/=2;
		printf("Case #%d: %lld\n",t,ans);
	}
}