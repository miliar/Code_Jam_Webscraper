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

int r, k, n;
VI g;

void testcase(int tst)
{
	ifs >> r >> k >> n;

	g.assign(n, 0);
	REP(l, n)
		ifs >> g[l];

	VI was(n, 0);
	VI rnd(n, 0);

	int i = 0;

	vector<ll> cost(1,0);

	int round = 0;
	ll rcst = 0;
	while (!was[i]) {

		rnd[i] = round;
		was[i] = 1;

		int cur = 0;
		int j = i;
		while (cur + g[j] <= k) {
			cur += g[j];
			j++;
			if (j >= n) j = 0;
			if (j == i) break;
		}

		rcst += cur;
		cost.pb(rcst);
		i = j;
		round++;
	}

	ll res = cost[rnd[i]];
	r -= rnd[i];

	int count = round - rnd[i];
	rcst -= cost[rnd[i]];

	res += ((ll)(r / count)) * rcst + cost[(r % count) + rnd[i]] - cost[rnd[i]];

	char buf[100];
	sprintf(buf, "%lld", res);

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
