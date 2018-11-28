#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define MAX 10000
int N, D;
int ds[MAX];
int ls[MAX];
int mas[MAX];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%d%d", &ds[i], &ls[i]);
		scanf("%d", &D);
		for (int i = 0; i < N; i++)
			mas[i] = 0;
		if (ls[0] >= ds[0])
			mas[0] = ds[0];
		for (int i = 0; i < N - 1; i++)
		{
			for (int j = i + 1; j < N; j++)
			{
				if (ds[i] + mas[i] >= ds[j])
					mas[j] = max(mas[j], min(ds[j] - ds[i], ls[j]));
			}
		}
		bool can = false;
		for (int i = 0; i < N; i++)
			if (ds[i] + mas[i] >= D)
				can = true;
		printf("Case #%d: %s\n", t+1, can ? "YES" : "NO");
	}


	fclose(stdin);
	fclose(stdout);

	return 0;
}