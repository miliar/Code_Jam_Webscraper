#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

char dictionary[5000][20];
bool templ[20][26];
int D, L, N;

int main()
{
	scanf("%d%d%d", &L, &D, &N);
	freopen("output.txt", "w", stdout);
	for (int i = 0; i < D; i++)
		scanf("%s", dictionary[i]);
	for (int i = 0; i < N; i++)
	{
		memset(templ, 0, sizeof(bool) * 26 * 20);
		char s[1000];
		scanf("%s", s);
		int k = 0;
		for (int j = 0; s[j]; j++)
		{
			if (s[j] == '(')
			{
				j++;
				while (s[j] != ')')
				{
					templ[k][s[j] - 'a'] = true;
					j++;
				}
			}
			else
			{
				templ[k][s[j] - 'a'] = true;
			}
			k++;
		}
		int res = 0;
		for (int j = 0; j < D; j++)
		{
			bool match = true;
			for (int k = 0; dictionary[j][k]; k++)
				if (!templ[k][dictionary[j][k] - 'a'])
				{
					match = false;
					break;
				}
			if (match)
				res++;
		}
		printf("Case #%d: %d\n", i + 1, res);

	}

	fclose(stdout);
	return 0;
}