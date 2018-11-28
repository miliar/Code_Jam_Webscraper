#include "stdio.h"
#include "algorithm"
#include "functional"
using namespace std;

int freq[1000];
int keys[1000];

int main()
{
	int N, T = 1;
	int P, K, L;
	int i, j, k;
	scanf("%d", &N);
	for (; T<=N; T++){
		scanf("%d%d%d", &P, &K, &L);
		for (i = 0; i < L; i++){
			scanf("%d", freq + i);
		}
		sort(freq, freq + L, greater<int>());
		memset(keys, 0, sizeof(keys));
		long long ret = 0;
		k = 0;
		for (i = 0; i < L; i++){
			keys[k]++;
			ret += (long long)keys[k] * freq[i];
			k ++;
			if (k==K) k = 0;
		}
		printf("Case #%d: %lld\n", T, ret);
	}
}
