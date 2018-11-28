#include <cstdio>
#include <iostream>

#define N 1005

using namespace std;

int a[N], team[N], n, result, res1, res2, ans;

void rec(int step)
{
	if (step == n)
	{
		bool ok1 = false, ok2 = false;
		result = res1 = res2 = 0;

		for (int i = 0; i < n; i++)
		{
			if (team[i])
			{
				res1 ^= a[i];
				result += a[i];
				ok1 = true;
			}
			else
			{
				res2 ^= a[i];
				ok2 = true;
			}
		}

		if (res1 == res2 && ok1 && ok2)
		{
			if (result > ans)
				ans = result;
		}

		return;
	}

	team[step] = 0;
	rec(step + 1);
	team[step] = 1;
	rec(step + 1);
}

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> n;		
		ans = 0;

		for (int j = 0; j < n; j++)
			cin >> a[j];

		rec(0);

		if (ans)
			printf("Case #%d: %d\n", i + 1, ans);
		else
			printf("Case #%d: NO\n", i + 1);
	}
	return 0;
}
