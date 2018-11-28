#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int N;
double x[100], y[100], r[100];

double dist(int p1, int p2)
{
	double a = x[p1] - x[p2], b = y[p1] - y[p2];
	return sqrt(a * a + b * b);
}

int main()
{
	int i, C;

	freopen("D.IN","r",stdin);
	freopen("D.out","w",stdout);

	cin >> C;
	for ( int t = 1; t <= C; ++t )
	{
		cin >> N;
		for ( i = 1; i <= N; ++i )
			cin >> x[i] >> y[i] >> r[i];

		cout << "Case #" << t << ": ";

		if ( N == 1 )
			cout << fixed << setprecision(9) << r[1] * 1.0 << endl;
		if ( N == 2 )
			cout << fixed << setprecision(9) << min(( dist(1,2) + r[1] + r[2] ) / 2.0, max(r[1],r[2])) << endl;
		if ( N == 3 )
		{
			double tmp2, tmp = max(( dist(1,2) + r[1] + r[2] ) / 2.0, r[3] * 1.0 );
			
			if ( tmp > ( tmp2 = max(( dist(1,3) + r[1] + r[3] ) / 2.0, r[2]*1.0 )) )
				tmp = tmp2;
			if ( tmp > ( tmp2 = max(( dist(2,3) + r[2] + r[3] ) / 2.0, r[1]*1.0 )) )
				tmp = tmp2;

			cout << fixed << setprecision(9) << tmp << endl;
		}
	}

	return 0;
}