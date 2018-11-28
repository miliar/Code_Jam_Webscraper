#include <cstdio>
#include <memory.h>

char Dict[5001][20], Pattern[8000];
bool Flush[5001], Appear[500];
int L, D, N, EIP, Count;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d %d %d\n", &L, &D, &N);
	for (int i = 1; i <= D; ++ i)
		gets(Dict[i]);
	for (int i = 1; i <= N; ++ i)
	{
		gets(Pattern); EIP = 0; Count = 0;
		memset(Flush, 0, sizeof(Flush));
		for (int j = 0; j < L; ++ j)
		{
			memset(Appear, 0, sizeof(Appear));
			if (Pattern[EIP] == '(')
			{
				++ EIP;
				while (Pattern[EIP] != ')') Appear[Pattern[EIP ++] - 'a' + 1] = true;
				++ EIP;
			}
			else Appear[Pattern[EIP ++] - 'a' + 1] = true;
			for (int k = 1; k <= D; ++ k)
				if (!Flush[k] && !Appear[Dict[k][j] - 'a' + 1]) Flush[k] = true;
		}
		for (int k = 1; k <= D; ++ k)
			if (!Flush[k]) ++ Count;
		printf("Case #%d: %d\n", i, Count);
	}
}
