#include <iostream>

typedef unsigned long long u64;

using namespace std;

struct mem
{
	u64 profit;
	u64 nextGroup;
};

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		u64 r, k, n;
		cin >> r >> k >> n;

		u64* g = new u64[n];
		for (u64 i = 0; i < n; ++i)
			cin >> g[i];

		mem* m = new mem[n];
		for (u64 i = 0; i < n; ++i)
		{
			u64 c = 0;
			u64 j = i;
			do
			{
				u64 x = c + g[j];
				if (x > k)
					break;

				c = x;
				j = (j + 1) % n;
			}
			while (c < k && i != j);

			m[i].profit = c;
			m[i].nextGroup = j;
		}

		u64 profit = 0;
		u64 cur = 0;
		for (u64 i = 0; i < r; ++i)
		{
			profit += m[cur].profit;
			cur = m[cur].nextGroup;
		}

		cout << "Case #" << t << ": " << profit << endl;
	}
}
