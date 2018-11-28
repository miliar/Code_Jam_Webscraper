#include <iostream>
#include <cstdio>

using namespace std;

struct ride
{
	long long val, offset;
};

int main ()
{
	freopen("C-small.in", "r", stdin);
	freopen("output.out", "w", stdout);
	long long t;
	cin >> t;
	for(long long cnt = 0; cnt < t; cnt++)
	{
		ride amount[1000] = {0};
		long long arr[1000], r, k, n;
		cin >> r >> k >> n;
		for(long long i = 0; i < n; i++)
			cin >> arr[i];
		for(long long i = 0; i < n; i++)
		{
			amount[i].val = arr[i];
			amount[i].offset = 1;
			long long j = (i + 1) % n;
			while(j != i && amount[i].val + arr[j] <= k)
			{
				amount[i].val += arr[j];
				amount[i].offset++;
				j = (j + 1) % n;
			}
		}
		
		long long res = 0;
		for(long long i = 0, j = 0; j < r; j++, i = (i + amount[i].offset) % n)
			res += amount[i].val;
		cout << "Case #" << cnt + 1 << ": " << res << endl;
	}
}
