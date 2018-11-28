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

void testcase(int tst)
{
	int n, m, a;

	ofs << "Case #" << tst+1 << ": ";

	ifs >> n >> m >> a;

	ll x1, x2, y1, y2;

	x1 = n;
	if ((a%n) == 0) y2 = a / n; else y2 = (a / n) + 1;

	if (y2 > m) { ofs << "IMPOSSIBLE" << endl; return; }

	int d = x1*y2-a;

	bool found = false;
	for (x2 = 0; x2 < min(d+1,n+1); x2++) {

		for (y1 = 0; y1 < min(d+1,m+1); y1++)
			if (x2*y1 == d)
			{
				found = true;
				break;
			}
		
		if (found) break;
	}

	if (!found) { ofs << "IMPOSSIBLE" << endl; return; }

	int ix1, ix2, iy1, iy2;
	ix1 = x1;
	ix2 = x2;
	iy1 = y1;
	iy2 = y2;
	ofs << "0 0 " << ix1 << " " << iy1 << " " << ix2 << " " << iy2 << endl;

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
