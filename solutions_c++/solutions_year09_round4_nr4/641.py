#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct p
{
	int x, y, r;
};

double Dist(const p &p1, const p &p2)
{
	return (sqrt(double(p1.x - p2.x) * (p1.x - p2.x) + double(p1.y - p2.y) * (p1.y - p2.y)) + p1.r + p2.r) / 2.;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		vector <p> arr;
		arr.resize(n);
		for(int j = 0; j < n; j++)
			cin >> arr[j].x >> arr[j].y >> arr[j].r;
		double ans = 1e9;
		if(n == 1)
			ans = arr[0].r;
		if(n == 2)
			ans = max(arr[0].r, arr[1].r);
		if(n == 3)
		{
			ans = min(ans, max (Dist(arr[0], arr[1]), (double)arr[2].r));
			ans = min(ans, max (Dist(arr[2], arr[1]), (double)arr[0].r));
			ans = min(ans, max (Dist(arr[0], arr[2]), (double)arr[1].r));
		}
		printf("Case #%d: %.6lf\n", i + 1, ans);
	}
	return 0;
}