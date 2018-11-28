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

int q;
VI t;

int was[128][128];

int go(int l, int r) {
	
	if (r - l <= 1) return 0;

	int& res = was[l][r];
	if (res > -1) return res;

	res = 1000000000;

	for (int m = l+1; m < r; m++) {
		res = min(res, go(l, m) + go(m, r) + t[r] - t[l] - 2);
	}

	return res;
}

void testcase(int tst)
{
	int p;
	ifs >> p >> q;

	t.assign(q, 0);
	REP(i, q)
		ifs >> t[i];
	
	q += 2;

	t.pb(0);
	t.pb(p+1);

	sort(ALL(t));

	memset(was, -1, sizeof(was));

	ofs << "Case #" << tst+1 << ": " << go(0, q-1) << endl;
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
