#include <stdio.h>

typedef long long ll;


main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		ll g[1010];
		ll r,k,n;
		scanf("%lld%lld%lld",&r,&k,&n);
		ll turn[1010];
		for(int i=0;i<n;i++){
			scanf("%lld",&g[i]);
			turn[i]=-1;
		}
		ll cost[1010];
		ll ans=0;
		int pos=0;
		int i;
		for(i=0;i<r;i++){
			if(turn[pos]!=-1){
				break;
			}
			turn[pos]=i;
			cost[pos]=ans;
			ll init=pos;
			ll sum=0;
			for(;;){
				sum+=g[pos];
				if(sum>k){sum-=g[pos];break;}
				pos=(pos+1)%n;
				if(pos==init)break;
			}
			ans+=sum;
			//printf("%lld\n",sum);
		}
		ans+=(ans-cost[pos])*((r-i)/(i-turn[pos]));
		i+=((r-i)/(i-turn[pos]))*(i-turn[pos]);
		for(;i<r;i++){
			ll init=pos;
			ll sum=0;
			for(;;){
				sum+=g[pos];
				if(sum>k){sum-=g[pos];break;}
				pos=(pos+1)%n;
				if(pos==init)break;
			}
			ans+=sum;
		}
		printf("Case #%d: ",t);
		printf("%lld\n",ans);
		
	}

}