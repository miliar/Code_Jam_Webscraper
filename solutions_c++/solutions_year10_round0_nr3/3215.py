#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		long long money = 0;

		int r, k, n;
		cin >> r >> k >> n;

		queue<int> q;

		for (int j = 0; j < n; ++j)
		{
			int groupSize;
			cin >> groupSize;

			q.push(groupSize);
		}

		for (int j = 0; j < r; ++j)
		{
			int groups = 0;
			int pasangers = 0;
			
			while (groups < n)
			{
				int groupSize = q.front();
				
				if (pasangers + groupSize <= k)
				{
					++groups;
					pasangers += groupSize;
					q.pop();
					q.push(groupSize);
				}
				else
				{
					break;
				}
			}

			money += pasangers;
		}

		printf("Case #%d: %ld\n", i, money);
	}

	return 0;
}
