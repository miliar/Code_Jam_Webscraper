#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main()
{
	ifstream cin("input.txt");
	freopen("output.txt", "w", stdout);

	int T;

	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		double S, R, t, b, e, w;
		int X, N;
		cin >> X >> S >> R >> t >> N;

		double path = 0;
		vector<pair<double, double> > a;
		for (int i = 0; i < N; i++)
		{
			cin >> b >> e >> w;
			a.push_back(make_pair(w, e - b));
			path += e - b;
		}
		sort(a.begin(), a.end());

		double tmp, r = 0;
		tmp = (X - path) / R;
		if (tmp > t)
		{
			r += t;
			r += ((X - path) - R * t) / S;
			t = 0;
		}
		else
		{
			r += tmp;
			t -= tmp;
		}

		for (int i = 0; i < N; i++)
		{
			tmp = a[i].second / (R + a[i].first);
			if (tmp > t)
			{
				r += t;
				r += (a[i].second - (R + a[i].first) * t) / (S + a[i].first);
				t = 0;
			}
			else
			{
				r += tmp;
				t -= tmp;
			}
		}

		printf("Case #%d: %.6lf\n", tc, r);
		//cout << "Case #" << tc << ": " << r << endl;
	}
	return 0;
}