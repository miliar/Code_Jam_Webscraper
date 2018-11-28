#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxN 1000

using namespace std;

int C, D, N;
char a[maxN], ans[maxN], ac;
char comb[100][100];
bool oppo[100][100];

int main()
{
	int T, z;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		memset(comb, 0, sizeof comb);
		memset(oppo, 0, sizeof oppo);
		cin >> C;
		for (int i = 0; i < C; i++)
		{
			char a, b, c;
			cin >> a >> b >> c;
			comb[a][b] = c;
			comb[b][a] = c;
		}
		cin >> D;
		for (int i = 0; i < D; i++)
		{
			char a, b;
			cin >> a >> b;
			oppo[a][b] = true;
			oppo[b][a] = true;
		}
		cin >> N >> a;
		ac = -1;
		for (int i = 0; i < N; i++)
		{
			ans[++ac] = a[i];
			while (ac && comb[ans[ac]][ans[ac - 1]])
			{
				char c = comb[ans[ac]][ans[ac - 1]];
				ans[--ac] = c;
			}
			for (int j = 0; j < ac; j++)
				for (int k = j + 1; k <= ac; k++)
					if (oppo[ans[j]][ans[k]])
						ac = -1;
		}
		printf("Case #%d: [", z);
		bool w = false;
		for (int i = 0; i <= ac; i++)
		{
			if (w)
				printf(", ");
			printf("%c", ans[i]);
			w = true;
		}
		printf("]\n");
	}
	return 0;
}
