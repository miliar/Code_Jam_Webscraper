#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>

using namespace std;

int MaxN = 1000005;
int D, N, Np;
vector<double> pos, pos1;

double abs(double x)
{
	if (x < 0) return -x;
	return x;
}

int main()
{
	int Ncase;
	freopen("b_small.in", "r", stdin);
	freopen("b_small.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		pos.clear();
		cin >> Np >> D;
		for (int i = 0; i < Np; ++i)
		{
			int p, v;
			cin >> p >> v;
			for (int j = 0; j < v; ++j)
				pos.push_back(p);
		}

		double l = 0, r = D * pos.size(), m;
		double eps = 1e-8;
		while (true)
		{
			m = (l + r) / 2;
			//cout << l << " " << m << " " << r << endl;
			pos1 = pos;
			pos1[0] -= m;
			//cout << pos1[0] << " ";
			bool ok = true;
			for (int i = 1; i < pos.size(); ++i)
			{
				if (pos1[i-1] + D - pos1[i] > m)
				{
					ok = false;
					break;
				}
				pos1[i] = max(pos1[i] - m, 0.0 + pos1[i-1] + D);
				//cout << pos1[i] << " ";
			}
			//cout << endl;
			if (ok) r = m;
			else l = m;
			if (abs(l - r) < eps) break;
		}

		cout << "Case #" << run+1 << ": " << l << endl;
	}
}
