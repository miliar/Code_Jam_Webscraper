#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

double f, R, t, r, g;

inline bool isinside(double r, double x, double y) { return x*x+y*y < r*r + 1E-10; }

double countsq(double x, double y)
{
	double x1, y1, x2, y2;
	double sg = g / 2 - f, sr = R - t - f;
	if (sg < 1E-10) return 0.0;
	if (sr < 1E-10) return 0.0;

	x1 = x - sg;
	y1 = y - sg;
	x2 = x + sg;
	y2 = y + sg;

	if (!isinside(sr, x1, y1) && !isinside(sr, x1, y2) && !isinside(sr, x2, y1) && !isinside(sr, x2, y2)) return 0.0;
	if (isinside(sr, x1, y1) && isinside(sr, x1, y2) && isinside(sr, x2, y1) && isinside(sr, x2, y2)) return 4*sg*sg;

	double res = 0.0;

	if (sr*sr-y2*y2 > x1*x1)
	{
		res += (sqrt(sr*sr-y2*y2) - x1) * (y2-y1);
		x1 = sqrt(sr*sr-y2*y2);
	}

	if (sr*sr-x2*x2 > y1*y1)
	{
		res += (sqrt(sr*sr-x2*x2) - y1) * (x2-x1);
		y1 = sqrt(sr*sr-x2*x2);
	}

	y2 = sqrt(sr*sr-x1*x1);
	x2 = sqrt(sr*sr-y1*y1);

	res += (x2*sqrt(sr*sr-x2*x2)-x1*sqrt(sr*sr-x1*x1))/2;
	res += (sr*sr*asin(x2/sr)-sr*sr*asin(x1/sr))/2;
	res -= (x2-x1)*y1;

	return res;


}

void testcase(int tst)
{
	ifs >> f >> R >> t >> r >> g;

	double st = (r + g / 2);

	double sq = 0;
	for (double x = r + g / 2; x <= R + g + 2*r; x += (g + 2*r))
		for (double y = r + g / 2; y <= R + g + 2*r; y += (g + 2*r))
			sq += countsq(x, y);

	ofs << "Case #" << tst+1 << ": ";

	double pi = acos(-1.0);

	char buf[100];
	sprintf(buf, "%.6lf", (double)1.0 - 4 * sq / (pi*R*R));

	ofs << buf << endl;

}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
