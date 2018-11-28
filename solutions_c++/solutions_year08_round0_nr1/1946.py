#include <stdio.h>
#include <string.h>

int main(void)
{
	int N;
	int S, Q;
	char engine[100][100], query[1000][100];
	int switches[20];
	int i, j, k, last;
	bool used[100];
	for (i = 0; i < 20; i++)
		switches[i] = 0;

	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &S);
		for (j = 0; j < S; j++)
			scanf("%*[\n]%[^\n]", engine[j]);
		scanf("%d", &Q);
		for (j = 0; j < Q; j++)
			scanf("%*[\n]%[^\n]", query[j]);

		for (j = 0; j < S; j++)
			used[j] = false;
		last = -1;
		for (j = 0; j < Q; j++)
		{
			for (k = 0; k < S; k++)
			{
				if (strcmp(engine[k], query[j]) == 0)
				{
					used[last = k] = true;
					break;
				}
			}
			for (k = 0; k < S; k++)
			{
				if (!used[k])
					break;
			}
			if (k == S)
			{
				switches[i]++;
				for (k = 0; k < S; k++)
					used[k] = false;
				if (last >= 0)
					used[last] = true;
			}
		}
	}

	for (i = 0; i < N; i++)
	{
		printf("Case #%d: %d\n", i + 1, switches[i]);
	}

	return 0;
}
