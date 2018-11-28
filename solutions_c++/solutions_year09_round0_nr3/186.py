#include <stdio.h>
#include <string.h>
char welcom[] = {"welcome to code jam"};
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
	int N, i, j, k; 
	char word[1000];
	int ans[1000], tmp[1000];
	scanf("%d\n", &N);
	for (i = 0; i < N; i++)
	{
		gets(word);
		for (k = 0; welcom[k]; k++)
			ans[k] = 0, tmp[k] = 0;
		for (j = 0; word[j]; j++)
		{
			for (k = 0; welcom[k]; k++)
				tmp[k] = 0;
			for (k = 0; welcom[k]; k++)
				if (word[j] == welcom[k])
				{
					if (k)
						tmp[k] = (ans[k] + ans[k - 1]) % 10000;
					else
						tmp[k] = ans[k] + 1;
				}
				else
					tmp[k] = ans[k];
			for (k = 0; welcom[k]; k++)
				ans[k] = tmp[k];
		}
		printf("Case #%d: %04d\n", i + 1, ans[strlen(welcom) - 1]);
	}
	return 0;
}
