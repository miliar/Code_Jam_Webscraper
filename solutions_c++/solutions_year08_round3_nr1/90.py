#include<stdio.h>
#include<algorithm>
using namespace std;
bool compare(__int64 a, __int64 b)
{
	return a > b;
}
int main()
{
	__int64 N, P, K, L, i, j, a[1005];
	__int64 time;
	freopen("A-large.in", "r", stdin);
	freopen("out1.txt", "w", stdout);
	scanf("%I64d", &N);
	for(i=1; i<=N; i++)
	{
		scanf("%I64d %I64d %I64d", &P, &K, &L);
		for(j=0; j<L; j++)
		{
			scanf("%I64d", &a[j]);
		}
		sort(a, a + L, compare);
		time = 0;
		__int64 t = 1;
		for(j=0; j<L; j++)
		{
			time = time + a[j] * t;
			if((j + 1) % K == 0)
			{
				t ++;
			}
		}
		printf("Case #%I64d: %I64d\n", i, time);
	}
	return 0;
}