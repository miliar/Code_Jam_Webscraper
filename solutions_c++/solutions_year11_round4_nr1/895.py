#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

const int GGG = 300;
const double eps = 1e-9;

int X, S, R, N;
double t;

priority_queue<pair<int, int>> Q;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int o;
	cin >> o;
	int I = 0;
	while (o--)
	{
		I++;
		cout << "Case #" << I << ": ";
		cin >> X >> S >> R >> t >> N;
		R -= S;
		int l = 0;
		while (N--)
		{
			int a, b, v;
			cin >> a >> b >> v;
			if (a > l) Q.push(make_pair(GGG - S, a - l));
			Q.push(make_pair(GGG - (S + v), b - a));
			l = b;
		}
		if (X > l) Q.push(make_pair(GGG - S, X - l));
		double ans = 0;
		while (!Q.empty())
		{
			pair<int, int> z = Q.top();
			Q.pop();
			double v = GGG - z.first;
			double r = z.second;
			double x = r / (v + R);
			if (x - t > eps) x = t;
			if (t - x > -eps) t -= x;
			if (t < eps) t = 0;
			ans += x;
			r -= x * (v + R);
			ans += r / v;
		}
		printf("%.6lf\n", ans);
	}
	return 0;
}