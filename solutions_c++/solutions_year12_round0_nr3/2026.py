#include <cstdio>
#include <unordered_set>

using namespace std;

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 1;ti <= tc;ti++)
	{
		int st, ed;
		scanf("%d %d", &st, &ed);
		int bound = 1; for (;bound <= ed;bound *= 10);

		unordered_set<int> did;
		long long ans = 0;
		for (int i = st;i <= ed;i++)
		{
			unordered_set<int> group;
			int cur = i;
			for (;;)
			{
				if (did.find(cur) != did.end())
					break;
				did.insert(cur);
				if (st <= cur && cur <= ed)
					group.insert(cur);
				cur = cur / 10 + (cur % 10) * (bound / 10);
			}
			ans += (long long)group.size() * (group.size() - 1) / 2;
		}

		printf("Case #%d: %lld\n", ti, ans);
		fprintf(stderr, "Case #%d: %lld\n", ti, ans);
	}
	return 0;
}
