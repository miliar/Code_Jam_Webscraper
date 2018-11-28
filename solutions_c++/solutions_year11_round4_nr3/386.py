
#include <cstdio>
#include <cstring>

typedef long long i64;

#define LEN 1000001

i64 s[LEN];
i64 p[LEN];
i64 q[LEN];

int main(){
	
	memset(s, 0, sizeof(s));
	i64 ptr = 0;

	for(i64 i=2; i<LEN; ++i){
		if(!s[i]){
			p[ptr++] = i;
			for(i64 j=i; j<LEN; j+=i){
				s[j] = 1;
			}
		}
	}

	for(i64 i=0; i<ptr; ++i){
		q[i] = p[i]*p[i];
	}

	i64 t; scanf("%lld", &t);
	i64 n;
	i64 ans;
	i64 tmp;

	for(i64 x=1; x<=t; ++x){
		scanf("%lld", &n);
		ans = 0;
		if(n == 1){
			ans = 0;
		}else{
			ans = 1;
		}
		for(i64 i=0; i<ptr && q[i] <= n; ++i){
			tmp = q[i];
			while(tmp <= n){
				++ans;
				tmp *= p[i];
			}
		}
		printf("Case #%lld: %lld\n", x, ans);
	}
	return 0;
}
