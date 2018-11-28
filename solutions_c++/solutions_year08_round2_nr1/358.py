// p4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

vector<pair<int, int>> foo;

int main()
{
	int n, a, b, c, d, x0, y0, m, t, tt;
	ifstream f("p4.in");
	f >> t;
	for (int tt = 0; tt < t; tt++)
	{
		foo.clear();
		f >> n >> a >> b >> c >> d >> x0 >> y0 >> m;

		long long x = x0, y = y0, cnt = 0;
		foo.push_back(pair<int, int>(x, y));
		for (int i = 1; i < n; i++)
		{
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			foo.push_back(pair<int, int>(x, y));
		}

		for (int i = 0; i < foo.size() - 2; i++)
			for (int j = i + 1; j < foo.size() - 1; j++)
				for (int k = j + 1; k < foo.size(); k++)
				{
					long long u = foo[i].first + foo[j].first + foo[k].first;
					long long v = foo[i].second + foo[j].second + foo[k].second;
					if (u % 3 == 0 && v % 3 == 0)
						cnt++;
				}

		cout << "Case #" << tt + 1 << ": " << cnt << endl;
	}
}
