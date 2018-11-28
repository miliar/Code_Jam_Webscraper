#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <queue>
#include <string>
#include <memory.h>



using namespace std;
#define MAX 200
#define MAX_TIME 2000010
pair<long long, long long> types[MAX];
long long mas[MAX_TIME];

int main()
{
	long long MAX_LONG = 1000000000;
	MAX_LONG = MAX_LONG * MAX_LONG;
	int T;

	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		long long M, F, N;
		scanf("%lld%lld%lld", &M, &F, &N);
		for (int i = 0; i < N; i++)
			scanf("%lld%lld", &types[i].first, &types[i].second);
		sort(types, types + N);		
		for (int i = 0; i < MAX_TIME; i++)
			mas[i] = MAX_LONG;
		int tIndex = 0;
		mas[0] = F + types[tIndex].first;
		for (int i = 1; i < MAX_TIME; i++)
		{
			while (tIndex < N && types[tIndex].second < i)
				tIndex++;
			if (tIndex == N)
				break;
			mas[i] = mas[i-1] + types[tIndex].first;
		}
		for (int i = 1; i < MAX_TIME; i++)
		{
			long long a = mas[(i - 1) / 2] + mas[i / 2];
			for (int j = 0; i - 1 - j >= j && j <= 200; j++)
				a = min(a, mas[j] + mas[i - 1 - j]);
			
			mas[i] = min(mas[i], a);
		}
		long long res = 0;
		for (int i = 0; i < MAX_TIME; i++)
			if (mas[i] <= M)
				res = i + 1;
			else
				break;
		printf("Case #%d: %lld\n", t+1, res);
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}