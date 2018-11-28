#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int N;
	int z;
	scanf("%d", &N);
	for(z = 1; z <= N; z++)
	{
		printf("Case #%d: ", z);
		int P, K, L;
		scanf("%d", &P);
		scanf("%d", &K);
		scanf("%d", &L);
		int* alph = new int[L];
		int* keys = new int[K];
		int i;
		for(i = 0; i < L; i++)
		{
			scanf("%d", &alph[i]);
		}
		sort(alph, alph+L);
		reverse(alph, alph+L);
		int sum = 0;
		for(i = 0; i < L; i++)
		{
			keys[i%K] = i/K + 1;
			sum = sum + keys[i%K] * alph[i];
		}
		printf(" %d\n", sum);
	}
	return 0;
}
