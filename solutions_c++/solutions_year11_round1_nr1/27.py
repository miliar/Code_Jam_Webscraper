#include <cstdio>

long long N;
int pd, pg;

bool process(){
	scanf("%lld%d%d", &N, &pd, &pg);
	
	if(pg == 0) return pd == 0;
	if(pg == 100)return pd == 100;
	
	int gcd = 100;
	
	while(pd%gcd != 0 || 100%gcd != 0)
		gcd--;
	
	gcd = 100 / gcd;
		
	if(gcd <= N){
		return true;	
	}else{
		return false;
		
	}
}

int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		printf("Case #%d: ", i);
		if(process())
			printf("Possible");
		else
			printf("Broken");
		printf("\n");
	}
	
	return 0;
}