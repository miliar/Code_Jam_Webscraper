#include <cstdio>

long long ncas, cas, l, p, c; 

int main(){
	scanf("%lld", &ncas);
	while (ncas--){
		scanf("%lld %lld %lld", &l, &p, &c);
		long long times = 0, res = 0;
		while (l < p){
			l *= c;
			++times;
		}
		while (times > 1){
			times = (times+1)/2;
			++res;
		}
		printf("Case #%lld: %lld\n", ++cas, res);
	}
	return 0;
}

