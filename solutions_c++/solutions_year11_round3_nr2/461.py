#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int casen = 1; casen <= cases; casen++)
	{
		cout << "Case #" << casen << ": ";
		__int64 l, t, n, c;
		cin >> l >> t >> n >> c;
		vector<int> a(c);
		int cyclesum = 0;
		for (int i = 0; i < c; ++i)
		{
			cin >> a[i];
			cyclesum += a[i];
		}
		double dist = t / 2.0;
		__int64 fullcycles = dist / cyclesum;
		__int64 stars = fullcycles * c;
		__int64 curdist = fullcycles * cyclesum;
		for (int i = 0; i < c; ++i)
		{
			if (curdist < dist)
			{
				curdist += a[i];
				stars++;
			}
			else
			{
				break;
			}
		}
		double cutoffdist = curdist - dist;
		vector<double> s(n);
		for (int i = 0; i < n; ++i)
		{
			if (i == stars-1)
				s[i] = cutoffdist;
			else if (i < stars-1)
				s[i] = 0;
			else
				s[i] = a[i % c];
		}
		sort(s.rbegin(), s.rend());
		__int64 savedtime = 0;
		for (int i = 0; i < l; ++i)
		{
			savedtime += s[i];
		}
		__int64 fulltime = 0;
		for (int i = 0; i < n; ++i)
		{
			fulltime += 2*a[i % c];
		}
		cout << fulltime - savedtime << endl;
	}
}