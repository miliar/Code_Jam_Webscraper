#include <cstdio>
#include <cstring>

int N, M, L;
int a[1000][1000];
char s[1000];
char pattern[100];

int main()
{
	freopen("welcome.in","r",stdin);
	freopen("welcome.out","w",stdout);

	int i, j, k, l;
	strcpy(pattern, "welcome to code jam");
	L = strlen(pattern);

	scanf("%d\n", &N);
	for (k = 1; k <= N; k++)
	{
		fgets(s, 505, stdin);
		M = strlen(s);

		for (i = 0; i < M; i++)
			if (s[i] == pattern[0]) a[0][i] = 1;
			else a[0][i] = 0;

		for (i = 1; i < L; i++)
			for (j = i; j <= M; j++)
				if (s[j] == pattern[i])
					for (l = j - 1; l >= 0; l--) 
					{
						a[i][j] += a[i - 1][l];
						a[i][j] %= 10000;
					}
		int rez = 0;
		for (i = 0; i < M; i++)
		{
			rez += a[L - 1][i];
			rez %= 10000;
		}

		printf("Case #%d: ",k);
		if (rez > 999) printf("%d\n",rez);
		else if (rez > 99) printf("0%d\n",rez);
		else if (rez > 9) printf("00%d\n", rez);
		else printf("000%d\n",rez);

		for (i = 0; i <= L; i++)
			for (j = 0; j <= 500; j++) a[i][j] = 0;
	}
	return 0;
}



		