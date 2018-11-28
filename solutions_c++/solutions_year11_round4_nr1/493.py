#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

double x_now, x_prev, w;
vector < pair < double, double > > a;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TEST_NUMBER;
	cin >> TEST_NUMBER;
	
	for (int TEST = 1; TEST <= TEST_NUMBER; TEST++)
	{
		x_now = x_prev = 0;

		a.clear();

		double x, s, r, t;
		int n;
		cin >> x >> s >> r >> t >> n;
		double time_res = 0;
		
		for (int i = 0; i < n; i++)
		{
			double tmp;
			cin >> x_now >> tmp >> w;
			a.push_back(make_pair(0, x_now - x_prev));
			x_prev = x_now;
			x_now = tmp;
			a.push_back(make_pair(w, x_now-x_prev));
			x_prev = x_now;
		}

		a.push_back(make_pair(0, x-x_prev));

		sort(a.begin(), a.end());

		for (int i = 0; i < a.size(); i++)
		{
			double t1, t2;
			t1 = a[i].second/(r+a[i].first);
			t2 = min(t1, t);
			t -= t2;
			time_res += t2;
			a[i].second -= t2*(r+a[i].first);

			t1 = a[i].second/(s+a[i].first);
			time_res += t1;
		}

		cout << "Case #" << TEST << ": ";
		printf("%.9f\n", time_res);
	}

	return 0;
}