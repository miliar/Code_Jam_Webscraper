#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int v1[8];
int v2[8];

int compare(const void *a, const void *b)
{
	return *(int *)a - *(int *)b;
}

int main()
{
	int i, j;
	int t, T;
	int n;
	int result;

	scanf("%d", &T);

	for(t=1;t<=T;t++)
	{
		scanf("%d", &n);

		for(i=0;i<n;i++)
		{
			scanf("%d", &v1[i]);
		}
		for(i=0;i<n;i++)
		{
			scanf("%d", &v2[i]);
		}
		qsort(v1, n, sizeof(int), compare);
		qsort(v2, n, sizeof(int), compare);
		result = 0;
		for(i=0;i<n;i++)
			result += v1[i] * v2[n-i-1];
		printf("Case #%d: %d\n", t, result);
	}
	return 0;
}


