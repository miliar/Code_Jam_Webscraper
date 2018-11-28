#include <iostream>
#include <vector>
#include <map>
#include <vector>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <set>
#include <algorithm>

using namespace std;

int T, N, D, C;
#define MAX 20000 //20000000000000
#define EPS 0.00000001

vector<pair<double, int>> points;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		points.clear();

		cin >> C >> D;
		for (int i = 0; i < C; ++i)
		{
			double p;
			int v;
			cin >> p >> v;

			points.push_back(make_pair(p,v));
		}

		sort(points.begin(), points.end());
		long double st = 0, dr = MAX, mid;

		while (!(dr - st < EPS))
		{
			mid = st + (dr - st) / 2;

			bool isGood = true;
			double antPos = points[0].first - mid + (points[0].second - 1) * D;

			if (abs(antPos - points[0].first) > mid)
				isGood = false;

			for (int i = 1; i < points.size() && isGood; ++i)
			{
				double posSt = points[i].first - mid;

				if (posSt < antPos || abs(posSt - antPos) < D)
					posSt = antPos + D;

				double posDr = posSt + (points[i].second - 1) * D;
				
				if (abs(posDr - points[i].first) > mid)
				{
					isGood = false;
				}

				antPos = posDr;
			}

			if (isGood)
				dr = mid;
			else
				st = mid;
		}

		printf("Case #%i: %llf\n", t, dr);

		//cout << "Case #" << t <<": " << dr << endl;
	}

	return 0;
}