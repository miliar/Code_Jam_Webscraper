#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

ifstream in("large.in");
ofstream out("large.out");

pair <double, int> s[1100];
double ans[210];

int main()
{
	int test, t;
	int i,n;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
		in >> n;
		double x = 0.0;	

		for (i = 0; i < n; ++i)
		{
			in >> s[i].first;
			s[i].second = i;
			x += s[i].first;
		}

		sort(s, s + n);

		out << "Case #" << t << ":";

		double sum = 2*x;		

		int u = 0;

		for (i = n - 1; i >= 0; --i)
		{
			if (s[i].first >= sum / (i + 1))
			{
				ans[s[i].second] = 0.0;
				sum -= s[i].first;
			}
			else
			{
				u = i + 1;
				break;
			}
		}

		for (; i >=0 ; --i)
		{			
			ans[s[i].second] = (sum - u * s[i].first) * 100.0 / (u * x);			
			
		}

		for (i = 0; i < n; ++i)
			out <<  " " << setiosflags(ios::fixed | ios::showpoint) << setprecision(7) << ans[i];
		out << endl;

	}
	return 0;
}