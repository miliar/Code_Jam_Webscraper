#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, d;
long long arr[1000100];

bool Can(long double m)
{
	long double last = arr[0] - m;
	for(int i = 1; i < n; i++)
	{
		long double now = arr[i] - m;
		if(last + d > now)
		{
			now = last + d;
			if(fabs(now - arr[i]) > m)
				return false;
		}
		last = now;
	}
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int nn;
		cin >> nn >> d;
		n = 0;
		for(int i = 0; i < nn; i++)
		{
			int p, k;
			cin >> p >> k;
			while(k)
			{
				arr[n++] = p;
				k--;
			}
		}
		long double l = 0, r = 1000000000000000ll;
		for(int i = 0; i < 100; i++)
		{
			long double m = (l + r) / 2;
			if(Can(m))
				r = m;
			else
				l = m;
		}
		printf("Case #%d: %.9Lf\n", tc + 1, l);
	}
	return 0;
}