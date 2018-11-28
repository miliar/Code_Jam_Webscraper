#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int a[1000001];

int go(int x, int y)
{
	if (y > a[x]) return y - a[x];
	return 0;
}

int main()
{
	a[0] = 0;
	a[1] = 1;
	a[2] = 3;
	for (int i = 3; i <= 1000000; ++i)
	{
		int ret = i;
		a[i] = i + (lower_bound(a, a + (i - 1), i) - a) - 1;
	}
	int T;
	scanf("%d", &T);
	for (int qn = 1; qn <= T; ++qn)
	{
		int a1, a2, b1, b2;
		long long ret = 0;
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);

		for (int i = a1; i <= a2; ++i)
		{
			if (b2 <= i)
			{
				continue;
			}
			else
			if (b1 <= i)
			{
				ret += go(i, b2);
			}
			else
			{
				ret += go(i, b2) - go(i, b1 - 1);
			}
		}

		swap(a1, b1);
		swap(a2, b2);
		
		for (int i = a1; i <= a2; ++i)
		{
			if (b2 <= i)
			{
				continue;
			}
			else
			if (b1 <= i)
			{
				ret += go(i, b2);
			}
			else
			{
				ret += go(i, b2) - go(i, b1 - 1);
			}
		}

		printf("Case #%d: ", qn);
		cout << ret << endl;
	}
}
