#include <cstdio>
#include <memory.h>

int N, Tests;
const int M = 19;
const char Pattern[M + 1] = "welcome to code jam";
char buff[1000];
int f[1000][20], Sum[20];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n", &Tests);
	for (int Cases = 1; Cases <= Tests; ++ Cases)
	{
		memset(f, 0, sizeof(f));
		memset(Sum, 0, sizeof(Sum));
		gets(buff); N = strlen(buff);
		for (int i = 0; i < N; ++ i)
		{
			for (int j = M - 1; j > 0; -- j)
			{
				if (buff[i] == Pattern[j])
					f[i][j] = Sum[j - 1];
				Sum[j] += f[i][j];
				if (Sum[j] >= 10000) Sum[j] %= 10000;
			}
			if (buff[i] == 'w') f[i][0] = 1, ++ Sum[0], Sum[0] %= 10000;
		}
		printf("Case #%d: ", Cases);
		if (Sum[M - 1] < 1000) printf("0");
		if (Sum[M - 1] < 100) printf("0");
		if (Sum[M - 1] < 10) printf("0");
		printf("%d\n", Sum[M - 1]);
	}
}
