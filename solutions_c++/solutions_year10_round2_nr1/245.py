#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

void solve()
{
	static char path[1010];
	static vector<string> paths;
	paths.clear();

	auto count = [&]() -> int
	{
		int c = 0;
		sort(paths.begin(), paths.end());
		const char *last = "/";
		for (auto it = paths.begin(); it != paths.end(); it++)
		{
			int i;
			const char *curr = it->c_str();
			for (i = 0; curr[i] == last[i] && curr[i] && last[i]; i++);
			if (curr[i])
			{
				if (curr[i] != '/' || last[i])
					c++;
				for (; curr[i]; i++)
					if (curr[i] == '/')
						c++;
			}
			last = curr;
		}
		return c;
	};

	int n, m, c;
	scanf("%d %d\n", &n, &m);
	for (int i = 0; i < n; i++)
	{
		gets(path);
		paths.push_back(path);
	}
	c = -count();
	for (int i = 0; i < m; i++)
	{
		gets(path);
		paths.push_back(path);
	}
	c += count();
	printf("%d\n", c);
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}