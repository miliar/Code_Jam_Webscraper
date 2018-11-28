
	#include <cstdlib>
	#include <cstdio>

	using namespace std;

	int work()
	{
		int n, cur[50];
		scanf("%d", &n);
		char c;
		while ((c = getchar()) != '\n');
		for (int i = 0; i < n; i ++)
		{
			cur[i] = 0;
			for (int j = 0; j < n; j ++)
			{
				c = getchar();
				if (c == '1')
					cur[i] = j;
			}
			while ((c = getchar()) != '\n');
			//printf("%d ", cur[i]);
		}
			//printf("\n");
		int ans = 0;
		for (int i = 0; i < n; i ++)
		{
			for (int j = i; j < n; j ++)
				if (cur[j] <= i)
				{
					ans += (j - i);
					int tmp = cur[j];
					for (int k = j; k > i; k --)
						cur[k] = cur[k - 1];
					cur[i] = j;
					break;
				}
			//printf("%d\n", ans);
		}
		return ans;
	}

	int main()
	{
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		int t;
		scanf("%d", &t);
		for (int i = 1; i <= t; i ++)
			printf("Case #%d: %d\n", i, work());
		return 0;
	}
