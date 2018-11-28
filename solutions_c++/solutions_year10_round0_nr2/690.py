#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

long long gcd (long long a, long long b)
{
	return b == 0 ? a : gcd(b, a % b);
}

int main ()
{
	freopen("B-small.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for(long long cnt = 0; cnt < t; cnt++)
	{
		int n;
		cin >> n;
		long long arr[1000];
		for(int i = 0; i < n; i++)
			cin >> arr[i];
		sort(&arr[0], &arr[n]);
		long long res = 0;
		for(int i = 0; i < n - 1; i++)
			res = gcd(res, arr[i + 1] - arr[0]);
		cout << "Case #" << cnt + 1 << ": " << res - ((arr[0] - 1) % res + 1) << endl;
	}
}

