#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int n;
		cin >> n;
		long long sum = 0;
		long long min = 1000000000000000ll;
		long long xor = 0;
		for (int i = 0; i < n; ++i)
		{
			long long cur;
			cin >> cur;
			sum += cur;
			xor ^= cur;
			if (cur < min) min = cur;
		}
		cout << "Case #" << t << ": ";
		if (xor)
		{
			cout << "NO" << endl;
		}
		else 
		{
			cout << sum - min << endl;
		}
	}
	return 0;
}