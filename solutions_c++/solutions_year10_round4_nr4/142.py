#include <iostream>
#include <vector>
#include <cmath>

const long double PI = 3.1415926535897932384626433832795;

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n, m;
		cin >> n >> m;
		vector <pair <long double, long double> > arr(n);
		for(int i = 0; i < n; i++)
			cin >> arr[i].first >> arr[i].second;
		printf("Case #%d: ", tc + 1);
		for(int i = 0; i < m; i++)
		{
			pair <long double, long double> a;
			cin >> a.first >> a.second;
			long double r1, r2;
			r1 = sqrt((a.first - arr[0].first) * (a.first - arr[0].first) + (a.second - arr[0].second) * (a.second - arr[0].second));
			r2 = sqrt((a.first - arr[1].first) * (a.first - arr[1].first) + (a.second - arr[1].second) * (a.second - arr[1].second));

			long double dist  = sqrt((arr[1].first - arr[0].first) * (arr[1].first - arr[0].first) + (arr[1].second - arr[0].second) * (arr[1].second - arr[0].second));
			if(dist >= r1 + r2)
			{
				printf("%.7Lf ", 0.);
				continue;
			}
			if(dist + min(r1, r2) <= max(r1, r2))
			{
				printf("%.7Lf ", min(r1, r2) * min(r1, r2) * PI);
				continue;
			}
			a = arr[1];
			//a.first = dist;
			//r1 = sqrt(r1);
			//r2 = sqrt(r2);
			//dist = sqrt(dist);
			long double x = (r1 * r1 - r2 * r2 + dist * dist) / 2 / dist;
			long double y = sqrt(r1 * r1 - x * x);
			if(x >= 0 && x <= dist)
			{
				long double angle = asin(y / r1);
				long double area = angle * r1 * r1 / 2 - y * x / 2;
				angle = asin(y / r2);
				area += angle * r2 * r2 / 2 - y * (dist - x) / 2;
				printf("%.7Lf ", area * 2);
			}
			else
			{
				long double angle = asin(y / r1);
				long double area = angle * r1 * r1 / 2 - y * fabs(x) / 2;
				angle = asin(y / r2);
				area -= angle * r2 * r2 / 2 - y * fabs(dist - x) / 2;
				printf("%.7Lf ", min(r1, r2) * min(r1, r2) * PI - fabs(area) * 2);
			}
			//a.second -= arr[0].second;
			/*if(dist > max(r1, r2))
			{
				long double x = r1 + r2 - dist;
				x = r1 - x * (r2 / (r2 + r1));
				long double len = sqrt(r1 * r1 - x * x);
				long double area = asin(len / r1) * r1 * r1 / 2;
				area -= len * x / 2;
				area += asin(len / r2) * r2 * r2 / 2;
				long double nx = r1 - x;
				nx = r1 + r2 - dist - nx;
				area -= (r2 + nx) * len / 2;
				printf("%.6lf ", area * 2);
			}*/

		}
		cout << endl;
	}
	return 0;
}