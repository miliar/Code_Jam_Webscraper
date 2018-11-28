#include <stdio.h>

static const int N = 110;

int sound[N];

int n;

bool Check(int x)
{
	for (int i = 0; i < n; ++i)
	{
		if (((sound[i] % x) != 0) && ((x % sound[i]) != 0))
			return false;
	}
	return true;
}

int main()
{
	int total;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	scanf("%d", &total);
	for (int test = 1; test <= total; ++test)
	{
		int low, high;
		bool flag = false;
		int ans = 0;
		
		scanf("%d%d%d", &n, &low, &high);

		for (int i = 0; i < n; ++i)
			scanf("%d", &sound[i]);

		for (int i = low; i <= high; ++i)
		{	
			if (Check(i))
			{
				flag = true;
				ans = i;
				break;
			}
		}

		printf("Case #%d: ", test);
			
		if (flag)
		{
			printf("%d\n", ans);
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}