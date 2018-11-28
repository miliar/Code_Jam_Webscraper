#include <stdio.h>

typedef long long ll;

ll L,t,N,C;
ll rep[2000];
ll acu[2000];

ll check(ll i,ll time){
	ll tacu = acu[i]-time;
	if(t<tacu){
		return rep[i%C];	
	}
	ll entrou = t-tacu;
	if(2*rep[i%C] > entrou)
		return (2*rep[i%C]-entrou)/2;
	return 0;
}


int main(){
	ll T;
	scanf("%lld",&T);
	for(ll c = 1;c<=T;c++){

		scanf("%lld %lld %lld %lld",&L,&t,&N,&C);
		for(ll i = 0;i<C;i++){
			scanf("%lld",rep+i);
		}
		acu[0] = 0;
		for(ll i = 1;i<=N;i++){
			acu[i] = acu[i-1]+rep[(i-1)%C]*2;
		//	printf("acu[%d] = %d\n",i,acu[i]);
		}
		ll max = 0;
		if(L  == 2 )
			for(ll i = 0;i<N;i++){
				for(ll j = 0;j<i;j++){
					ll eco = check(j,0);
					ll eco2 =eco;
					eco+=check(i,eco);
					if(eco > max){

//						printf(">> %d %d %d %d\n",i,j, eco, eco2);
						max = eco;
					}
				}
			}
		if(L  == 1 )
			for(ll i = 0;i<N;i++){
				ll eco = check(i,0);
				//printf(">> %d  > %d\n",i,eco);
				if(eco > max){
				//	printf(">> %d \n",i);
					max = eco;
				}
			}
		
		printf("Case #%lld: %lld\n",c,acu[N]-max);
	}
	return 0;
}
