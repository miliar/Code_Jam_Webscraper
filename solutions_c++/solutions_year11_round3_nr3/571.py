#include <stdio.h>

typedef long long ll;
ll n;
ll L,H;
ll freq[200];

ll gcd(ll a, ll b){
	if(a == 0LL) return b;
	if(b<a) return gcd(b,a);
	if(a == b) return a;
	if(a == 1) return 1;
	return gcd(b%a,a);
}

bool can(ll num){
	int mult = 0;
	for(int i = 0;i<n;i++){
		if(num%freq[i] == 0LL || freq[i]%num == 0LL) mult++;
	}
	if(mult == n)
		return true;
	return false;
		
}


int main(){
	int T;
	scanf("%d",&T);
	for(int c = 1;c<=T;c++){
		scanf("%lld %lld %lld",&n,&L,&H);
		for(int i = 0;i<n;i++){
			scanf("%lld",freq+i);
		}
		ll i;
		for(i = L;i<=H;i++){
			if(can(i)){ // HAHHAHAHAH
				break;
			}
				
		}
		printf("Case #%d: ",c);
		if(i == H+1LL){
			printf("NO\n");	
		}else{
			printf("%lld\n",i);
		}
	}

}
