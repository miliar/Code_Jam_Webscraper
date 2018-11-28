#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;

void Solve()
{
	long long x, s, r, n;
	double t;
	vector <pair<long long, double> > arr;
	cin >> x >> s >> r >> t >> n;
	for(int i = 0; i < n; i++)
	{
		int x, y, w;
		cin >> x >> y >> w;
		arr.push_back(make_pair(w + s, y - x));
	}
	double sum = 0;
	for(int i = 0; i < n; i++)
		sum += arr[i].second;
	if(sum < x)
		arr.push_back(make_pair(s, x - sum));
	sort(arr.begin(), arr.end());
	double ans = 0;
	r -= s;
	for(int i = 0; i < arr.size(); i++)
	{
		double can = t * (arr[i].first + r);
		if(can >= arr[i].second)
		{
			double need = arr[i].second / (arr[i].first + r);
			t -= need;
			ans += need;
		}
		else
		{
			ans += t;
			t = 0;
			double rem = arr[i].second - can;
			ans += rem / arr[i].first;
		}
	}
	printf("%.9lf\n", ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		printf("Case #%d: ", tc + 1);
		Solve();
	}
	return 0;
}