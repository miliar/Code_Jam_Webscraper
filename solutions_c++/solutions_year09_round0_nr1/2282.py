#include <stdio.h>

int l, d, n;
char strings[5000][16];
bool pattern[15][26];

int main()
{
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0 ; i < d ; i++)
		scanf("%s", strings[i]);
	char buffer[1000];
	for (int i = 0 ; i < n ; i++)
	{
		scanf("%s", buffer);
		for (int j = 0 ; j < l ; j++)
			for (int k = 0 ; k < 26 ; k++)
				pattern[j][k] = false;
		int p = 0;
		for (int j = 0 ; j < l ; j++)
		{
			if (buffer[p] == '(')
			{
				p++;
				while (buffer[p] != ')')
				{
					pattern[j][buffer[p] - 'a'] = true;
					p++;
				}
			}
			else
				pattern[j][buffer[p] - 'a'] = true;

			p++;
		}
		int cnt = 0;
		bool match;
		for (int j = 0 ; j < d ; j++)
		{
			match = true;
			for (int k = 0 ; k < l ; k++)
				if (!pattern[k][strings[j][k] - 'a'])
				{
					match = false;
					break;
				}
			if (match)
				cnt++;
		}
		printf("Case #%d: %d\n", i + 1, cnt);
	}
	return 0;
}
