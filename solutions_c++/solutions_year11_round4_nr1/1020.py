#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>

using namespace std;

int main()
{
	int T, test;
	cin >> T;
	for (test=1;test<=T;test++)
	{
		double len;
		double S, R, t;
		int n;
		cin >> len >> S >> R >> t >> n;

		vector<pair<double, double> > intervals;
		vector<double> speed;

		double prev = 0.0;

		for (int i=0;i<n;i++)
		{
			double begin, end, w;
			cin >> begin >> end >> w;

			if (begin - prev > 0.001)
			{
				intervals.push_back(make_pair(prev, begin) );
				speed.push_back(0.0);
			}

			intervals.push_back(make_pair(begin, end) );
			speed.push_back(w);

			prev = end;
		}

		if (len - prev > 0.001)
		{
			intervals.push_back(make_pair(prev, len) );
			speed.push_back(0.0);
		}

		double res = 0.0;

		for (int i=0;i<speed.size();i++)
		{
			double b, e, w;
			b = intervals[i].first;
			e = intervals[i].second;
			w = speed[i];
			res+=(e-b)/(w+S);
		}

		int k = speed.size();
		vector<int> st(k, 0);
		do
		{
		
			bool f = false;
			double maxDT;
			double maxT;
			double maxD;
			int idx;

			for (int i=0;i<k;i++)
				if (st[i] == 0)
				{
					double b, e, w;
					b = intervals[i].first;
					e = intervals[i].second;
					w = speed[i];

					double x = e - b - t*(w + R);
					double usedT, usedL;
					if (x<=0.0)
					{
						usedT = (e - b)/(w + R);
						usedL = e - b;
					}
					else
					{
						usedT = t;
						usedL = e - b - x;
					}

					double t1, t2;
					t1 = (e - b)/(w + S);
					t2 = usedL/(w + R) + (e-b-usedL)/(w + S);

					/*if (f==false || (t2/t1 < maxDT) )
					{
						maxDT = t2/t1;
						maxT = usedT;
						maxD = t1 - t2;
						idx = i;
						f = true;
					}*/
					double T1, T2;
					T1 = usedL/(w+S);
					T2 = usedL/(w+R);
					if (f==false || (T2/T1 < maxDT) )
					{
						maxDT = T2/T1;
						maxT = usedT;
						maxD = t1 - t2;
						idx = i;
						f = true;
					}
				}

			if (f)
			{
				res-=maxD;
				t-=maxT;
				st[idx] = 1;
			}
			else break;
			
		}
		while(t>=1.0e-10);

		printf("Case #%d: %1.10lf\n", test, res);

	}


	return 0;
}