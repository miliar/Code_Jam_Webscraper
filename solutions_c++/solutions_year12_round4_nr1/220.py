#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N;
struct vine_s
{
	int pos;
	int length;
	int max_reach;

	vine_s() : max_reach(-1) { }
};

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 1;ti <= tc;ti++)
	{
		vector<vine_s> vines;

		int N;
		scanf("%d", &N);
		for (int i = 0;i < N;i++)
		{
			vine_s x;
			scanf("%d %d", &x.pos, &x.length);
			vines.push_back(x);
		}

		int L;
		scanf("%d", &L);

		vines[0].max_reach = vines[0].pos * 2;

		int ans = false;
		for (int i = 0;i < N;i++)
		{
			if (vines[i].max_reach >= L)
				ans = true;
			for (int j = i + 1;j < N;j++)
			{
				if (vines[i].max_reach < vines[j].pos)
					break;
				int dist = min(vines[j].pos - vines[i].pos, vines[j].length);
				vines[j].max_reach = max(vines[j].max_reach, vines[j].pos + dist);
			}
		}

		printf("Case #%d: %s\n", ti, ans ? "YES" : "NO");
	}
	return 0;
}
