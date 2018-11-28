#include <stdio.h>
#include <algorithm>
using namespace std;

#define MAX 100000

long long har[MAX];



int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	long long T, t, N, L, H, i, ans, p;
	scanf("%lld", &T);
	for(t = 1; t <= T; t++){
		scanf("%lld %lld %lld", &N, &L, &H);
		for(i = 0; i < N; i++) scanf("%lld", &har[i]);
		
		for(ans = L; ans <= H; ans++){
			p = 0;
			for(i = 0; i < N; i++){
				if(!(har[i]%ans)) p++;
				else if(har[i]) if(!(ans%har[i])) p++;
			}
			//printf("%lld %lld\n", ans, p);
			if(p == N) break;
		}
		if(ans < L || ans > H) printf("Case #%lld: NO\n", t);
		else printf("Case #%lld: %lld\n", t, ans);
	}
	return 0;
}
