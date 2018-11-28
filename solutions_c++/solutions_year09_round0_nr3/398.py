
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	using namespace std;

	char list[505];
	char p[20] = "welcome to code jam";
	int ans[505][20];

	void work()
	{
		char c;
		int n = 1;
		while (c = getchar(), c != '\n')
		{
			list[n] = c;
			n ++;
		}
		memset(ans, 0, sizeof(ans));
		ans[0][0] = 1;
		for (int i = 1; i < n; i ++)
			for (int j = 0; j < 20; j ++)
			{
				ans[i][j] = ans[i - 1][j];
				if (j > 0 && list[i] == p[j - 1])
					ans[i][j] = (ans[i][j] + ans[i - 1][j - 1]) % 10000;
			}
		int u = ans[n - 1][19];
		if (u < 10)	printf("000%d\n", u);
		else	if (u < 100)	printf("00%d\n", u);
		else	if (u < 1000)	printf("0%d\n", u);
		else	printf("%d\n", u);
	}

	int main()
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int T;
		scanf("%d\n", &T);
		for (int i = 0; i < T; i ++)
		{
			printf("Case #%d: ", i + 1);
			work();
		}
		return 0;
	}
