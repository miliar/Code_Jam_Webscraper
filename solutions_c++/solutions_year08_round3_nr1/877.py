#include <stdio.h>
#include <stdlib.h>

int N, P, K, L;
int keys[12];
int feq[100];

int intComp(const void* a, const void* b)
{
	return *(const int*)b - *(const int*)a;
}

void readData()
{
	int i;
	scanf("%d%d%d", &P, &K, &L);
	for (i=0; i<L; ++i) scanf("%d", &feq[i]);
}

int solve()
{
	int ans = 0, i, j, k=0;
	qsort(feq, L, sizeof(int), intComp);
	for (i=1; i<=P; ++i)
		for (j=0; j<K && k<L; ++j, ++k)
			ans += i * feq[k];
	return ans;
}

int main()
{
	int i;
	scanf("%d", &N);
	for (i=1; i<=N; ++i)
	{
		readData();
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
