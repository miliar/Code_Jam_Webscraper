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

int h, w, r;

VVI a;

int was[128][128];

int go(int y, int x) {

	if (y == h && x == w) return 1;
	if (y > h || x > w) return 0;
	if (a[y][x] == 1) return 0;
	int&  res = was[y][x];
	if (res > -1) return res;
	res = (go(y+1, x+2) + go(y+2,x+1)) % 10007;
	return res;

}

void testcase(int tst)
{

	ifs >> h >> w >> r;
	a.assign(h+1, VI(w+1, 0));
	REP(i, r)
	{
		int y, x;
		ifs >> y >> x;
		a[y][x] = 1;
	}

	memset(was, -1, sizeof(was));
	int res = go(1, 1);

	ofs << "Case #" << tst+1 << ": " << res << endl;
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
