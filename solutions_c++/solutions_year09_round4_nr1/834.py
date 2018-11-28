#include <cstdio>
#include <algorithm>
using std::swap;

int main()
{
	freopen("A2.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	int row[45], i, j, t, n;
	char line[45];
	
	scanf("%d", &t);
	for (int id = 1; id <= t; ++id)
	{
		scanf("%d", &n);
		getchar();
		for (i = 1; i <= n; ++i)
		{
			gets(line);
			for (j = n - 1; j >= 0; --j)
				if (line[j] == '1')
					break;
			row[i] = j + 1;
		}
		
		int cnt = 0;
		for (i = 1; i <= n; ++i)
		{
			j = i;
			while (row[j] > i)
				++j;
			while (j > i)
			{
				swap(row[j], row[j - 1]);
				++cnt;
				--j;
			}
		}
		printf("Case #%d: %d\n", id, cnt);
	}
	
	return 0;
}
