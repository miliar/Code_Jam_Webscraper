#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

const ld pi = atan2(0.0, -1.0);

ld sqr(ld x)
{
	return x * x;
}

ld len(ld x, ld y)
{
	return sqrt(x * x + y * y);
}

ld cross(ld x1, ld y1, ld x2, ld y2)
{
	return x1 * y2 - x2 * y1;
}

ld dot(ld x1, ld y1, ld x2, ld y2)
{
	return x1 * x2 + y1 * y2;
}

ld square(deque<ld>& x, deque<ld>& y)
{
	ld res = (x.front() - x.back()) * (y.front() + y.back());
	FOR(i, SZ(x)-1) res += (x[i+1] - x[i]) * (y[i+1] + y[i]);
	res = 0.5 * fabs(res);
	return res;
}

int main()
{
	ifstream fin("s3.in"); ofstream fout("s3.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		ld f, R, t, r, g;
		fin >> f >> R >> t >> r >> g;

		ld BR = R;
		R -= t + f;

		if (2 * f >= g || R < 1e-10)
		{
			fout << "Case #" << tt+1 << ": 1.000000\n";
			continue;
		}

		ld sq = 0, ix1, ix2, iy1, iy2;
		for (ld x = r+0.5*g; x-0.5*g <= R; x += 2*r+g)
		{
			for (ld y = r+0.5*g; y-0.5*g <= R; y += 2*r+g)
			{
				if (len(x-0.5*g+f, y-0.5*g+f) >= R) continue;

				if (len(x+0.5*g-f, y+0.5*g-f) <= R)
				{
					sq += sqr(g-2*f);
					continue;
				}
				
				deque<ld> qx, qy;
				
				qx.push_back(x-0.5*g+f);
				qy.push_back(y-0.5*g+f);

				if (len(x+0.5*g-f, y-0.5*g+f) <= R)
				{
					qx.push_back(x+0.5*g-f);
					qy.push_back(y-0.5*g+f);
					ix1 = x+0.5*g-f;
					iy1 = sqrt(sqr(R)-sqr(ix1));
					qx.push_back(ix1);
					qy.push_back(iy1);
				}
				else
				{
					iy1 = y-0.5*g+f;
					ix1 = sqrt(sqr(R)-sqr(iy1));
					qx.push_back(ix1);
					qy.push_back(iy1);
				}

				if (len(x-0.5*g+f, y+0.5*g-f) <= R)
				{
					qx.push_front(x-0.5*g+f);
					qy.push_front(y+0.5*g-f);
					iy2 = y+0.5*g-f;
					ix2 = sqrt(sqr(R)-sqr(iy2));
					qx.push_front(ix2);
					qy.push_front(iy2);
				}
				else
				{
					ix2 = x-0.5*g+f;
					iy2 = sqrt(sqr(R)-sqr(ix2));
					qx.push_front(ix2);
					qy.push_front(iy2);
				}

				sq += square(qx, qy);
				sq += 0.5 * sqr(R) * acos(dot(ix1, iy1, ix2, iy2)/R/R) - 0.5 * fabs(cross(ix1, iy1, ix2, iy2));
			}
		}

		ld res = 1.0 - 4 * sq / (pi * BR * BR);
		fout << fixed << setprecision(6) << "Case #" << tt+1 << ": " << res << endl;
	}

	return 0;	
}
