#include <stdio.h>
#include <string.h>

#define maxlen (20)
#define maxls (1005)
#define maxs (5005)
#define maxc (130)

char S[maxs][maxlen];

int V[maxlen][maxc];

int L, D, N;

char str[maxls];

int main()
{
	int i, j, k;

	scanf("%d %d %d", &L, &D, &N);

	for(i = 0; i < D; ++i)
	{
		scanf("%s", S[i]);
	}

	for(i = 0; i < N; ++i)
	{
		memset(V, 0, sizeof(V));

		scanf("%s", str);

		int c = 0;

		for(j = 0; str[j]; ++j)
		{
			if(str[j] == '(')
			{
				for(k = j + 1; str[k] != ')'; ++k)
				{
					V[c][str[k]] = 1;
				}

				j = k;
			}
			else
			{
				V[c][str[j]] = 1;
			}
			++c;
		}

/*
		for(j = 0; j < L; ++j)
		{
			for(k = 'a'; k <= 'z'; ++k)
			{
				printf("%d", V[j][k]);
			}
			printf("\n");
		}
//*/

		int res = 0;

		for(j = 0; j < D; ++j)
		{
			int f = 1;

			for(k = 0; k < L; ++k)
			{
				if(!V[k][S[j][k]])
				{
					f = 0;
					break;
				}
			}

			if(f)
			{
				++res;
			}
		}

		printf("Case #%d: %d\n", i + 1, res);
	}

	return 0;
}
