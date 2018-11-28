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

int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tcn, n, s, p, t;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		cin >> n >> s >> p;
		int res = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> t;
			if ((t + 2) / 3 >= p)
				res++;
			else if (t % 3 != 1 && (t + 2) / 3 == p - 1 && s > 0 && t > 0)
			{
				res++;
				s--;
			}
		}

		printf("Case #%d: %d\n", tc, res);
	}

	return 0;
}
