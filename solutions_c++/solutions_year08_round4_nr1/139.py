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

int m, v;
VI g, c;
VI l;

int was[5000][2];

int go(int i, int v) {

	if (2*i > m) {
		return (v == l[i]) ? 0 : 1000000;
	}
	int& res = was[i][v];
	if (res > -1) return res;

	res = 1000000;

	if (v == 0) {

		if (g[i] == 1 || c[i] == 1)
			res = min(res, go(2*i, 0) + go(2*i+1, 0) + ((g[i] == 1) ? 0 : 1));
		if (g[i] == 1 || c[i] == 1)
			res = min(res, go(2*i, 1) + go(2*i+1, 0) + ((g[i] == 1) ? 0 : 1));
		if (g[i] == 1 || c[i] == 1)
			res = min(res, go(2*i, 0) + go(2*i+1, 1) + ((g[i] == 1) ? 0 : 1));


		if (g[i] == 0 || c[i] == 1)
			res = min(res, go(2*i, 0) + go(2*i+1, 0) + ((g[i] == 0) ? 0 : 1));

	} else
	{

		if (g[i] == 0 || c[i] == 1)
			res = min(res, go(2*i, 1) + go(2*i+1, 1) + ((g[i] == 0) ? 0 : 1));
		if (g[i] == 0 || c[i] == 1)
			res = min(res, go(2*i, 1) + go(2*i+1, 0) + ((g[i] == 0) ? 0 : 1));
		if (g[i] == 0 || c[i] == 1)
			res = min(res, go(2*i, 0) + go(2*i+1, 1) + ((g[i] == 0) ? 0 : 1));


		if (g[i] == 1 || c[i] == 1)
			res = min(res, go(2*i, 1) + go(2*i+1, 1) + ((g[i] == 1) ? 0 : 1));

	}

	return res;

}

void testcase(int tst)
{

	ifs >> m >> v;
	g.assign(m+1, 0);
	c.assign(m+1, 0);
	l.assign(m+1, 0);

	REP(i, (m-1)/2)
		ifs >> g[i+1] >> c[i+1];

	for (int i = (m-1)/2; i < m; i++)
		ifs >> l[i+1];

	memset(was, -1, sizeof(was));

	ofs << "Case #" << tst+1 << ": ";
	int res = go(1, v);

	if (res < 1000000)
	{
		ofs << res << endl;
	} else
		ofs << "IMPOSSIBLE" << endl;
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
