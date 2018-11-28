#include <stdio.h>
#include <memory.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#define MAX 100000
#define MAX_INT 1000000000

int tree[MAX];
bool change[MAX];
long long mas[MAX][2];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int M, V;
	for (int t = 0; t < T; t++)
	{
		scanf("%d%d", &M, &V);
		for (int i = 1; i <= (M-1)/2; i++)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			tree[i] = a;
			change[i] = b == 1;
			mas[i][0] = MAX_INT;
			mas[i][1] = MAX_INT;
		}
		for (int i = (M-1)/2 + 1; i <= M; i++)
		{
			scanf("%d", &tree[i]);
			mas[i][0] = MAX_INT;
			mas[i][1] = MAX_INT;
			mas[i][tree[i]] = 0;
		}

		

		for (int i = (M-1)/2; i > 0; i--)
		{
			for (int a = 0; a < 2; a++)
				for (int b = 0; b < 2; b++)
				{
					long long cost = mas[i * 2][a] + mas[i*2+1][b];
					bool val = ((bool)a) && ((bool)b);
					if (tree[i] == 0)
					{
						if (change[i])
							cost++;
						else
							cost = MAX_INT;
					}
					int v = val ? 1 : 0;
					mas[i][v] = min(mas[i][v], cost);

					cost = mas[i * 2][a] + mas[i*2+1][b];
					val = ((bool)a) || ((bool)b);
					if (tree[i] == 1)
					{
						if (change[i])
							cost++;
						else
							cost = MAX_INT;
					}
					v = val ? 1 : 0;
					mas[i][v] = min(mas[i][v], cost);
				}
		}

		if (mas[1][V] < MAX_INT)
			printf("Case #%d: %lld\n", t  +1, mas[1][V]);
		else
			printf("Case #%d: %IMPOSSIBLE\n", t  +1);
	}



	fclose(stdin);
	fclose(stdout);
	return 0;
}