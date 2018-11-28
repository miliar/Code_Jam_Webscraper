#include <iostream>
#include <vector>

using namespace std;

static void solve()
{
	int n, s, p;
	cin >> n >> s >> p;

	vector<int> arr(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	int res = 0;
	for (int z = 0; z < 8; z++)
	{
		int count = 0, c = 0;
		for (int i = 0; i < n; i++)
		{
			int t = arr[i];
			if (z & (1 << i))
			{
				if (t < 2)
					continue;
				if (((t+2)+(3-((t+2)%3)))/3 >= p)
					count++;
				c++;
			}
			else
			{
				if (t % 3 == 0 && t/3 >= p)
					count++;
				else if (t % 3 == 1 && (t+2)/3 >= p)
					count++;
				else if (t % 3 == 2 && (t+1)/3 >= p)
					count++;
			}
		}
		if (c == s && count > res)
			res = count;
	}
	cout << res << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}
