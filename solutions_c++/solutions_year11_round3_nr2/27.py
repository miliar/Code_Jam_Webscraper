#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <bitset>

using namespace std;

long long Dist(const vector <int> &dist, long long T, long long sum, int L)
{
	if (T >= sum)
		return sum * 2;

	long long res = 0;
	int index = 0;
	for (;;++index)
		if (res + 2 * dist[index] >= T)
			break;
		else
			res += 2 * dist[index];

	res = res + 2 * dist[index];

	vector <int> d;
	d.push_back(res / 2 - T / 2);
	for (int i = index + 1; i < dist.size(); ++i)
		d.push_back(dist[i]);
	res = T;

	sort(d.rbegin(), d.rend());

	for (int i = 0; i < d.size(); ++i)
		if (i < L)
			res += d[i];
		else
			res += 2 * d[i];

	return res;
}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cntTest;
	cin >> cntTest;

	for (int test = 0; test < cntTest; ++test)
	{
		int n, c, l;
		long long t;

		cin >> l >> t >> n >> c;

		vector <int> aC(c);
		for (int i = 0; i < c; ++i)
			cin >> aC[i];

		vector <int> dist(n);
		long long sum = 0;
		for (int i = 0; i < n; ++i)
		{
			dist[i] = aC[i % c];
			sum += dist[i];
		}
		
		cout << "Case #" << test + 1 << ": " << Dist(dist, t, sum, l) << endl;
		
	}

	return 0;
}