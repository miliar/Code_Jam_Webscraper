#include <stdio.h>

int pd,pg;

typedef long long ll;
ll n;

ll gcd(ll a,ll b){
	while(b){
		ll r = a %  b;
		a = b,b = r;
	}
	return a;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int tc = 1;tc<=T;tc++){
		scanf("%lld%d%d",&n,&pd,&pg);
			
		printf("Case #%d: ",tc);

		if(pd!=0 && pg==0
			|| pd!=100 && pg==100){
			puts("Broken");
			continue;
		}
		
		ll xd = 100 / gcd(100,pd);
	
		puts(n>=xd ? "Possible" : "Broken");
	}
	return 0;
}
