#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> data;
map<int, int> left;
int N;

int possible(int sz)
{
	map<int, int> current = left;
	map<int, int> safe;

	for (int i = 1;i <= 10000;)
	{
		if (safe[i])
		{
			int lv = min(current[i], safe[i]);
			safe[i] = 0;
			current[i] -= lv;
			safe[i + 1] += lv;
			continue;
		}

		if (current[i] == 0)
		{
			i++;
			continue;
		}


		int j;
		for (j = 0;j < sz;j++)
		{
			if (!current[i + j])
				break;
		}
		if (j != sz)
			return false;

		for (int j = 0;j < sz;j++)
			current[i + j]--;

		safe[i + j]++;
	}
	return true;
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 1;ti <= tc;ti++)
	{
		fprintf(stderr, "Case %d\n", ti);
		data.clear();
		left.clear();
		scanf("%d", &N);
		for (int i = 0;i < N;i++)
		{
			int v;
			scanf("%d", &v);
			left[v]++;
		}


		int st = 1;
		int ed = N;
		for (;;)
		{
			if (st > ed)
				break;
			int mid = (st + ed) / 2;

			if (possible(mid))
				st = mid + 1;
			else
				ed = mid - 1;
		}

		printf("Case #%d: %d\n", ti, st - 1);
	}
}
