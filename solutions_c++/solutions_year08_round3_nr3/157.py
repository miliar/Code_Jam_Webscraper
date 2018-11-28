#include <stdio.h>
#define MAXN 1000

//#define DEBUG
long long int table[MAXN];
long long int num[MAXN];
int A[MAXN];

int main()
{
	int i, j, n, m;
	long long int X, Y, Z;
	int icase, ncase;
	long long int ans;
	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		scanf("%d%d%ld%ld%ld", &n, &m, &X, &Y, &Z);
		X %= Z;
		Y %= Z;
		for(i=0; i<m; ++i)
			scanf("%ld", &A[i]);
		ans = 0;
		for(i=0; i<n; ++i){
			table[i] = 1;
			num[i] = A[i%m];
			A[i%m] = ((X * A[i%m])%Z + (Y*(i+1))%Z) % Z;
			for(j=i-1; j>=0; --j)
				if(num[i] > num[j])
					table[i] += table[j] % 1000000007;
			ans += table[i];
			ans %= 1000000007;
		}
#ifdef DEBUG
		for(i=0; i<n; ++i)
			printf("%lld ", num[i]);
		printf("\n");
		for(i=0; i<n; ++i)
			printf("%lld ", table[i]);
		printf("\n");
#endif
		printf("Case #%d: %lld\n", icase+1, ans);
	}

	return 0;
}
