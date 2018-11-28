
#include <cstdio>

int main(){
	
	int t; scanf("%d", &t);

	long long n;
	int d, g;

	for(int x=1; x<=t; ++x){
		scanf("%lld %d %d", &n, &d, &g);
		int poss;
		if(n < 100){
			poss = 0;
			for(long long i=1; i<=n && !poss; ++i){
				for(long long j=0; j<=i && !poss; ++j){
					if(j*100 == i*d){
						poss = 1;
					}
				}
			}
		}else{
			poss = 1;
		}
		if(poss){
			if(d != 100 && g == 100 || d != 0 && g == 0){
				printf("Case #%d: Broken\n", x);
			}else{
				printf("Case #%d: Possible\n", x);
			}
		}else{
			printf("Case #%d: Broken\n", x);
		}
	}
	return 0;
}
