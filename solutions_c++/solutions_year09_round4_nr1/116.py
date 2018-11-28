#include <cstdio>

int Tests, Cases, N;
int Map[50][50], Last[50];
char Buff[500];

void swap(int &a, int &b) { int c = a; a = b; b = c; }

int Do_it()
{
	int Ans = 0;
	for (int P = 0; P < N; ++ P)
		for (int i = P; i < N; ++ i)
			if (Last[i] <= P)
			{
				int j = i;
				while (j != P)
				{
					swap(Last[j], Last[j - 1]);
					++ Ans, -- j;
				}
				break;
			}
	return Ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &Tests);
	for (int Cases = 1; Cases <= Tests; ++ Cases)
	{
		scanf("%d\n", &N);
		for (int i = 0; i < N; ++ i)
		{
			gets(Buff);
			for (int j = 0; j < N; ++ j)
				Map[i][j] = Buff[j] - '0';
		}
		for (int i = 0; i < N; ++ i)
		{
			int j = N - 1;
			while (!Map[i][j] && j > 0) -- j;
			if (!j && !Map[i][j]) Last[i] = -1;
			else Last[i] = j;
		}
		printf("Case #%d: %d\n", Cases, Do_it());
	}
}
