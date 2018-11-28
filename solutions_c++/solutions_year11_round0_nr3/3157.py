#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <deque>

using namespace std;


void Solve()
{
	int n;
	cin >> n;
	int mas[20];
	for (int i = 0; i < n; ++ i)
	{
		cin >> mas[i];
	}

	int last = 1 << n;

	int res = -1;
	for (int mask = 1; mask < last - 1; ++ mask)
	{
		int val1 = 0, val2 = 0;
		int sum1 = 0, sum2 = 0;
		for (int i = 0; i < n; ++ i)
		{
			if (mask & (1 << i))
			{
				sum1 += mas[i];
				val1 ^= mas[i];
			}
			else
			{
				sum2 += mas[i];
				val2 ^= mas[i];
			}
		}
		if (val1 == val2) res = max(res, max(sum1, sum2));
	}

	if (res > 0) cout << res << endl;
	else cout << "NO" << endl;

}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int ntest;
	cin >> ntest;

	for (int test = 1; test <= ntest; ++ test)
	{
		cout << "Case #" << test << ": ";
		Solve();
	}



	return 0;
}