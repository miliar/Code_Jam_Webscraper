#include <stdio.h>


int L, D, N;
char word[5000][16];
char pattern[1000];

int main()
{
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; i++)
	{
		scanf("%s", word + i);
	}

	for (int i = 0; i < N; i++)
	{
		int res = 0;
		scanf("%s", pattern);

		for (int j = 0; j < D; j++)
		{
			int k = 0;
			int m = 0;
			while (word[j][k])
			{
				if (pattern[m] == '(')
				{
					m++;
					bool found_in_bracket = false;
					while (pattern[m] != ')')
					{
						if (!found_in_bracket && word[j][k] == pattern[m])
						{
							k++;
							found_in_bracket = true;
						}
						m++;
					}
					m++;
					if (!found_in_bracket)
					{
						break;
					}
				}
				else
				{
					if (word[j][k] == pattern[m])
					{
						k++;
						m++;
					}
					else
					{
						break;
					}
				}
			}
			if (!word[j][k])
			{
				res++;
			}
		}

		printf("Case #%d: %d\n", i+1, res);
	}
}
