#include <iostream>
#include <iomanip>
#include <complex>
#include <algorithm>
#include <vector>

using namespace std;

typedef complex<double> point;

double cover( const point &p1, int r1, const point &p2, int r2)
{
	return (r1 + r2 + abs(p1 - p2)) / 2;
}

int main()
{
	int tc;
	cin >> tc;
	for (int casecnt = 1; casecnt <= tc; ++casecnt)
	{
		cout << "Case #" << casecnt << ": " << setprecision(12);
		int n;
		cin >> n;

		vector<point> pos;
		vector<int> rad;

		for (int c = 0; c < n; ++c)
		{
			int x, y, r;
			cin >> x >> y >> r;
			pos.push_back(point(x,y));
			rad.push_back(r);
		}

		if (n == 1)
		{
			cout << (double)rad[0] << endl;
			continue;
		}

		if (n == 2)
		{
			double r = max(rad[0], rad[1]);
			r = min(r, cover(pos[0], rad[0], pos[1], rad[1]));
			cout << r << endl;
			continue;
		}

		int p[] = {0,1,2};

		double minR = 1e9;
		do
		{
			int j = p[1], k = p[2];
			double R = max( (double)rad[ p[0] ], cover( pos[j], rad[j], pos[k], rad[k] ) );

			minR = min(minR, R);

		} while(next_permutation(p,p+3));

		cout << minR << endl;
	}

	return 0;
}
