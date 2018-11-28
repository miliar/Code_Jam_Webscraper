#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

vector<int> a;

bool bit(int x, int i)
{
	return (1 << i) & x;
}

void solve(int TCase)
{
	int n = a.size();
	
	int ans = -1;
	
	for (int mask = 1; mask < (1 << n) - 1; ++mask)
	{
		int sum1 = 0, sum2 = 0, sn = 0;
		for (int i = 0; i < n; ++i)
		{
			if (bit(mask, i) == 0)
				sum1 = sum1 ^ a[i];
			else
				sum2 = sum2 ^ a[i], sn += a[i];
		}
		if (sum1 == sum2)
			ans = max(ans, sn);
	}
	if (ans == -1)
		cout << "Case #" << TCase + 1 << ": NO" << endl;
	else
		cout << "Case #" << TCase + 1 << ": " << ans << endl;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int n;
		cin >> n;
		a.resize(n);
		for (int j = 0; j < n; ++j)
			cin >> a[j];
		solve(i);
	}
}
