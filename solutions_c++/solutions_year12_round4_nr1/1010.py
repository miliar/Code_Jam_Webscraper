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

int n;
VI d, l;

bool was[10010][10010];

bool go(int p, int h) {

	if (h == n-1 || p == n-1) return true;

	if (was[p][h]) return false;

	int mx = d[h] + min(d[h] - d[p], l[h]);
	for (int j = h+1; d[j] <= mx; j++)
		if (go(h, j))
			return true;

	was[p][h] = true;
	return false;
}

void testcase(int tst)
{
	ifs >> n;
	
	d.clear();
	l.clear();

	d.pb(0);
	l.pb(0);

	REP(i, n) {
		int nd;
		int nl;
		ifs >> nd;
		ifs >> nl;
		d.pb(nd);
		l.pb(nl);
	}

	int D;
	ifs >> D;
	d.pb(D);
	l.pb(2000000000);

	n += 2;

	ofs << "Case #" << tst+1 << ": ";

	memset(was, false, sizeof(was));
	if (go(0, 1)) {
		ofs << "YES";
	} else {
		ofs << "NO";
	}
	
	ofs << endl;
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
