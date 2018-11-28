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
	int n, s, p;
	ifs >> n >> s >> p;

	VI good(n, 0);
	VI goodSur(n, 0);
	VI sur(n, 0);

	REP(i, n) {
		int a;
		ifs >> a;

		if (a >= (3*p - 2)) good[i] = 1;
		if (a > 1 && a >= (3*p - 4)) goodSur[i] = 1;
		if (a > 1) sur[i] = 1;
	}

	VI was(n, 0);
	int res = 0;
	REP(i, n) {
		if (goodSur[i] == 1 && good[i] == 0 && s > 0) {
			res++;
			was[i] = 1;
			s--;
		}
	}

	REP(i, n) {
		if (goodSur[i] == 1 && was[i] == 0 && s > 0) {
			res++;
			was[i] = 1;
			s--;
		}
	}

	REP(i, n) {
		if (good[i] == 1 && was[i] == 0) {
			res++;
			was[i] = 1;
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
