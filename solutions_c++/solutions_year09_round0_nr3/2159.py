#include <iostream>
#include <string>

using namespace std;

const char *pat = "welcome to code jam";

int f[100][1000];
char line[1000];

int	main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int task;
	scanf("%d\n", &task);
	int m = strlen(pat);
	for (int ncase = 0; ncase < task; ++ncase)
	{
		gets(line);
		int n = strlen(line);
		for (int k = 0; k < m; ++k)
		{
			for (int i = 0; i < n; ++i) 
			{
				f[k][i] = (i == 0) ? 0 : f[k][i - 1];
				if (line[i] == pat[k])
					if (k == 0)
						f[k][i] += 1;
					else if (i > 0)
						f[k][i] += f[k - 1][i - 1];
				f[k][i] %= 10000;
			}
		}
		printf("Case #%d: %.4d\n", ncase + 1, f[m - 1][n - 1]);
	}
	return 0;
}