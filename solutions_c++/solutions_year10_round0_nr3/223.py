#include<cstdio>
#include<cstring>

int T, ca;
long long N, K, R;

int main(){
	scanf("%d", &T);
	while (T--){
		scanf("%lld%lld%lld", &R, &K, &N);
		long long P[2*N], Q[2*N];
		for (int i = 0 ; i < N; ++i)
			scanf("%lld", P+i);
		for (int i = N; i < 2*N; ++i)
			P[i] = P[i-N];
		long long S[N];
		for (int i = 0 ; i < N; ++i){
			for (long long j = i, k = 0; k + P[j] <= K && j-i < N; ++j)
				S[i] = (j+1)%N, Q[i] = (k+=P[j]);
		}
		long long res = 0;
		long long p = 0;
		for (int i = 0 ; i < R; ++i)
			res += Q[p], p = S[p]; 
		printf("Case #%d: %lld\n", ++ca, res);
	}
	return 0;
}
