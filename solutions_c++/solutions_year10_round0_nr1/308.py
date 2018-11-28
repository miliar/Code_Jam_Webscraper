#include <stdio.h>
#include <string.h>

typedef long long LL;

int main(){
	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\A.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		LL n, k;
		scanf("%lld%lld", &n, &k);
		if((k + 1) % (1LL << n) == 0)
			printf("Case #%d: ON\n", case_t);
		else
			printf("Case #%d: OFF\n", case_t);
	}
	return 0;
}