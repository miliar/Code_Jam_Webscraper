#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

double d;

vector <double> v;

bool work(double T)
{
	int i, n = v.size();
	double last;
	for (i = 0 ; i < n; ++i)
	{
		if (i == 0)
			last = v[0] - T;
		else
		{
			double tex = last + d;
			if (tex > v[i])
			{
				if (tex - v[i] > T)
					return false;
				else
					last = tex;
			}
			else
			{
				if (v[i] - tex <= T)
					last = tex;
				else
					last = v[i] - T;
			}
		}
	}
	return true;
}

double solve()
{
	double L = 0,R = 2000.0,m;
	R = R * R;
	R = R * R;
	for (int i = 0; i < 1000; ++i)
	{
		m = (L + R) / 2.0;
		if (work(m))
			R = m;
		else
			L = m;
	}

	return (L + R)/2.0;

}

int main()
{
	int test,t,i,j,u,p,g;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
		v.clear();
		in >> u >> d;
		for (i = 0; i < u; ++i)
		{
			in >> p >> g;
			for (j = 0 ; j < g; ++j)
				v.push_back(p);
		}
		sort(v.begin(), v.end());
		double answer = solve();
		out << setiosflags(ios::fixed | ios::showpoint);
		out << "Case #" << t << ": " << setprecision(8) << answer << endl;

	}
	return 0;
}