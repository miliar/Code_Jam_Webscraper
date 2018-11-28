#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <set>
#include <iostream>
#include <queue>
using namespace std;


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t  <= tc; t ++)
	{
		int c,d;
		cin >> c >> d;
		vector <pair<int,int> > a(c);
		for (int i = 0; i < c; i ++)
			cin >> a[i].first >> a[i].second;
		
		long double l = 0;
		//long double r= 1e9*2;
		long double r= 1e12;

		for (int it = 0; it < 100; it ++)
		{
			long double m = (l+r)/2;
			bool ok = true;

			long double last = -1e12;
			for (int i = 0; ok && i < c; i ++)
				for (int j = 0; ok && j < a[i].second; j ++)
				{
 					if (last <= a[i].first-m)
					{
						last = a[i].first-m+d;
						continue;
					}
					if (last <=a[i].first)
					{

						//long double tmp = min(a[i].first-last, m);
						last += +d;
						continue;
					}
					else
					{
						if (last > a[i].first + m)
							ok = false;
						else
							last += d;
					}
				}

			if (ok)
				r = m;
			else
				l = m;
		}

		printf("Case #%d: %.9Lf\n", t, r);
		//cout << "Case #" << t << ":" << endl;

	

	}

	return 0;
}
