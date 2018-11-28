# include <cstdio>
# include <cstdlib>
# include <climits>
# include <cstring>
# include <cctype>

# include <iostream>
# include <sstream>
# include <vector>
# include <string>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <algorithm>

using namespace std;

const int N_MAX = 100 + 10;
 int a[N_MAX];
 int n;
 int l;
 int h;

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	scanf("%d", &testNum);
	for (int testId = 1; testId <= testNum; ++testId)
	{
		scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);

		int res = -1;
		for (int i = l; i <= h; ++i)
		{
			bool flag = true;
			for (int j = 0; j < n; ++j)
				if (a[j] % i != 0 && i % a[j] != 0)
				{
					flag = false;
					break;
				}
			if (flag)
			{
				res = i;
				break;
			}
		}

		printf("Case #%d: ", testId);
		if (res == -1)
			printf("NO\n");
		else
			printf("%d\n", res);
	}

	return 0;
}