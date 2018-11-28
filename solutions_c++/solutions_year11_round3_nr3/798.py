#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<long long, long long> pll;
typedef pair<int, int> pii;
typedef pair<long double, long double> plld;
typedef pair<double, double> pd;

long long solve(vector<long long> v, long long l, long long h)
{
	for (long long j = l; j <= h; j++)
	{
		bool good = true;
		for (int i = 0; i < v.size() && good; i++)
		{
			if (v[i] % j != 0 && j % v[i] != 0)
				good = false;
		}
		if (good)
			return j;
	}
	return -1;
}



int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long n, l, h;
		cin >> n >> l >> h;
		vector<long long> v(n);
		for (int j = 0; j < n; j++)
			cin >> v[j];
		long long r = solve(v, l, h);
		printf("Case #%d: ", i + 1);
		if (r == -1)
			cout << "NO" << endl;
		else
			cout << r << endl;
	}
}