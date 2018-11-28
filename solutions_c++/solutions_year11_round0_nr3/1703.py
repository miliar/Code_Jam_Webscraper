#include <cstdio>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for (int i = 0 ; i < T; i++) {
		int N;
		scanf("%d",&N);
		long long int C[1100];
		long long int sum = 0;
		long long int min = -1;
		long long int xorsum = 0;
		for ( int j = 0 ; j < N;j++) {
			scanf("%lld",&C[j]);
			xorsum ^= C[j];
			sum+=C[j];
			min = (min == -1 || min > C[j])?C[j]:min;
		}
		if (xorsum != 0) {
			printf("Case #%d: NO\n",i+1);
		}
		else{
			printf("Case #%d: %lld\n",i+1,sum-min);
		}
	}
	return 0;
}
