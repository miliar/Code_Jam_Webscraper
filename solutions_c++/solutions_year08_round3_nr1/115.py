#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>

using namespace std;

struct tt
{
	int x, y;
};


int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int r;
	cin >> r;
	for (int y = 1; y <= r; y++)
	{
		long long p, k, l;
		cin >> p >> k >> l;
		vector<long long> v(l);
		for (int i = 0; i < l; i++)
			cin >> v[i];
		sort(v.begin(), v.end());
		long long cnt = 0;
		long long j = 0;
		long long t = 1;
		for (int i = l-1; i >= 0; i--)
		{
			if (j == k)
			{
				t++;
				j = 0;
			}
			cnt += v[i] * t;
			j++;
		}

		cout << "Case #" << y << ": " << cnt << endl;
	}
	return 0;
}

