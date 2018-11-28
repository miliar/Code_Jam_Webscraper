#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


pair<long long, long long> ololo(long long p)
{
	long long f = 100;
	while (p > 0 && p % 2 == 0 && f % 2 == 0)
	{
		p /= 2;
		f /= 2;
	}
	while (p > 0 && p % 5 == 0 && p % 5 == 0)
	{
		p /= 5;
		f /= 5;
	}
	return make_pair(p, f);
}

bool solve(long long n, long long pd, long long pg)
{
	if (pg == 100)
		if (pd != 100)
			return false;
		else
			return true;

	if (pg == 0)
		if (pd == 0)
			return true;
		else
			return false;

	if (pd == 0)
		return true;

	long long day_g = n;
	pair<long long, long long> tp = ololo(pd);
	day_g = (day_g / tp.second) * tp.second;
	if (day_g == 0)
		return false;
	return true;
/*	long long day_w = (day_g / tp.second) * tp.first;
	if (day_w 
	return true;
	*/
	}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long n, pd, pg;
		cin >> n >> pd >> pg;
		printf("Case #%d: %s\n", i + 1, (solve(n, pd, pg)) ? "Possible" : "Broken");
		//if (solve(n, pd, pg))
	}
	return 0;
}