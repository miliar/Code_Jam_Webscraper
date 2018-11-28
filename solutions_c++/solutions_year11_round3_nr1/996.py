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

const int N_MAX = 50 + 10;

char a[N_MAX][N_MAX];
int r;
int c;

bool TryToPut()
{
	bool res = false;

	for (int i = 0; i < r - 1; ++i)
		for (int j = 0; j < c - 1; ++j)
			if (a[i][j] == '#' && a[i + 1][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j + 1] == '#')
			{
				a[i][j] = '/';
				a[i][j + 1] = '\\';
				a[i + 1][j] = '\\';
				a[i + 1][j + 1] = '/';
				res = true;
			}

	return res;
}

bool check()
{
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			if (a[i][j] == '#')
			{
				return true;
			}

	return false;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	scanf("%d", &testNum);
	for (int testId = 1; testId <= testNum; ++testId)
	{
		scanf("%d%d\n", &r, &c);
		for (int i = 0; i < r; ++i)
		{
			gets(a[i]);
		}
		
		while (TryToPut());
		bool res = !check();

		printf("Case #%d:\n", testId);
		if (res)
		{
			for (int i = 0; i < r; ++i)
			{
				printf("%s\n", a[i]);
			}
		}
		else
		{
			printf("Impossible\n");
		}
	}

	return 0;
}