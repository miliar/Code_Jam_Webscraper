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

	int n, A, B, C, D, x0, y0, m;

	ifs >> n >> A >> B >> C >> D >> x0 >> y0 >> m;

	vector<PII> t;
	ll x, y;
	x = x0, y = y0;
	t.pb(mp(x, y));

	REP(i, n-1)
	{
		x = (x*A+B)%m;
		y = (y*C+D)%m;
		t.pb(mp(x,y));
	}

	REP(i, t.sz)
	{
		t[i].fs = t[i].fs%3;
		t[i].sc = t[i].sc%3;
	}

	VI ax(9, 0);
	REP(i, t.sz)
		ax[t[i].fs*3+t[i].sc]++;

	ll res = 0;
	REP(i0, 9)
		REP(i1, i0+1)
			REP(i2, i1+1)
	{
		int x0 = i0 / 3, y0 = i0 % 3;
		int x1 = i1 / 3, y1 = i1 % 3;
		int x2 = i2 / 3, y2 = i2 % 3;
		if (((x0 + x1 + x2)%3) != 0) continue;
		if (((y0 + y1 + y2)%3) != 0) continue;
		if (i0 == i1 && i1 == i2)
		{
			if (ax[i0] < 3) continue;
			ll c = ax[i0];
			res += c * (c-1) * (c-2) / 6;
			continue;
		}

		if (i0 == i1)
		{
			if (ax[i0] < 2) continue;
			ll c = ax[i0];
			res += c * (c-1) / 2 * ax[i2];
			continue;
		}

		if (i1 == i2)
		{
			if (ax[i1] < 2) continue;
			ll c = ax[i1];
			res += c * (c-1) / 2 * ax[i0];
			continue;
		}

		if (i0 == i2)
		{
			if (ax[i0] < 2) continue;
			ll c = ax[i0];
			res += c * (c-1) / 2 * ax[i1];
			continue;
		}

		ll c = ax[i0];
		res += c * ax[i1] * ax[i2];

	}

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
