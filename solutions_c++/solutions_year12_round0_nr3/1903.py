#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

int next(int x, int w)
{
	return w * (x % 10) + x / 10;
}

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn, a, b;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		cin >> a >> b;
		int w = 1;
		while (w * 10 <= b)
			w *= 10;

		int res = 0;
		for (int i = a; i <= b; ++i)
		{
			int x = next(i, w);
			while (x != i)
			{
				if (x > i && x <= b)
					res++;
				x = next(x, w);
			}
		}
	
		printf("Case #%d: %d\n", tc, res);
	}

	return 0;
}
