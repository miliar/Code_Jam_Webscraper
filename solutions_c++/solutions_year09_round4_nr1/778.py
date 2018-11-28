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

bool hassolution(VI &c) {

	int n = c.sz;

	REP(i, n+1) {
		int cnt = 0;
		REP(j, n)
			if (c[j] >= i) cnt++;
		if (cnt > n-i) return false;
	}

	return true;
}

void testcase(int tst)
{
	int n;
	ifs >> n;

	VS a(n);

	REP(i, n)
		ifs >> a[i];

	VI b(n);
	REP(j, n) {
		b[j] = -1;
		for (int i = n-1; i >= 0; i--) {
			if (a[j][i] == '1') {
				b[j] = i;
				break;
			}
		}
	}

	int res = 0;

	VI was(n, 0);

	for (int j = n-1; j >= 0; j--) {
		int cnt = 0;
		for (int i = n-1; i >= 0; i--) if (!was[i]) {

			VI c;
			REP(k, n) if (!was[k] && k != i) c.pb(b[k]);

			if (hassolution(c)) {
				was[i] = 1;
				res += cnt;
				break;
			}
			
			cnt++;
		}
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
