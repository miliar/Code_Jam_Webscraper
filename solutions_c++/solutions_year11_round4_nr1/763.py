#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

typedef vector<int>		VI;
typedef vector<VI>		VVI;
typedef vector<string>	VS;
typedef pair<int,int>	PII;
typedef vector<PII>		VPII;

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		int X, N;
		double S, R, t;
		cin >> X >> S >> R >> t >> N;
		int pos = 0;
		map<int,int> pieces;
		for (int i = 0; i < N; i++)
		{
			int B, E, w;
			cin >> B >> E >> w;
			pieces[0] += B - pos;
			pieces[w] += E - B;
			pos = E;
		}
		pieces[0] += X - pos;

		double res = 0;
		for (map<int,int>::iterator it = pieces.begin(); it != pieces.end(); it++)
		{
			double T = it->second / (R + it->first);
			if (T <= t)
			{
				res += T;
				t -= T;
			}
			else
			{
				res += t + (it->second - (R + it->first) * t) / (S + it->first);
				t = 0;
			}
		}
		printf("Case #%d: %.12lf\n", kase, res);
	}
	return 0;
}
