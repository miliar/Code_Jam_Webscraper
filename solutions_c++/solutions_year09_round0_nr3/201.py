#include <iostream>
using namespace std;
char word[20] = "welcome to code jam";
int d[1024][20];
int main()
{
	int i, j, k, n, len, res, c = 0;
	char s[1024];
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	//freopen("in.txt", "r", stdin);
	scanf("%d\n", &n);
	while (n--)
	{
		gets(s);
		len = strlen(s);
		res = 0;
		memset(d, 0, sizeof(d));
		for (i = 0; i < len; i++)
		{
			for (j = 0; j < 19; j++)
			{
				if (s[i] == word[j])
				{
					if (j == 0)
					{
						d[i][j] = 1;
						continue;
					}
					for (k = 0; k < i; k++)
					{
						if (s[k] == word[j-1])
						{
							d[i][j] += d[k][j-1];
							d[i][j] %= 10000;
						}
					}
				}
			}
		}
		
		for (i = 0; i < len; i++)
		{
			res += d[i][18];
			res %= 10000;
		}
		printf("Case #%d: %04d\n", ++c, res);
		
	}
	return 0;
}
