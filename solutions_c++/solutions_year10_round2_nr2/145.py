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
	int n, k, b, t;

	ifs >> n >> k >> b >> t;

	VI x(n);

	REP(i, n)
		ifs >> x[i];

	VI v(n);

	REP(i, n)
		ifs >> v[i];

	VI a;
	VI reach(n, 0);
	for (int i = n-1; i >= 0; i--) {
		
		reach[i] = ((b-x[i]) <= t*v[i]) ? 1 : 0;

		if (reach[i]) {

			int cost = 0;
			for (int j = i+1; j < n; j++)
				if (reach[j] == 0)
					cost++;

			a.pb(cost);
		}
	}

	ofs << "Case #" << tst+1 << ": ";

	if (a.sz < k)
		ofs << "IMPOSSIBLE";
	else {
		int res = 0;
		REP(i, k)
			res += a[i];
		ofs << res;
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
