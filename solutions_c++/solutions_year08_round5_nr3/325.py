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

int m, n;
VS a;

int was[10][2048];

int check(int m2, int m1, int y) {
	int res = 0;
	REP(i, n) {
		if (((1<<i)&m2) > 0) {
			if (a[y][i] == 'x') return -1;

			res++;
			
			if (((1<<(i+1)) & m2) > 0) return -1;
			if (i > 0 && (((1<<(i-1)) & m2) > 0)) return -1;
			if (((1<<(i+1)) & m1) > 0) return -1;
			if (i > 0 && (((1<<(i-1)) & m1) > 0)) return -1;

		}
	}
	return res;
}

int go(int y, int p) {
	if (y == m) return 0;

	int& res = was[y][p];
	if (res > -1) return res;
	res = 0;

	REP(np, (1<<n)) {
		int cc = check(np, p, y);
		if (cc > -1) res = max(res, go(y+1, np)+cc);
	}

	return res;


}

void testcase(int tst)
{
	ifs >> m >> n;
	a.assign(m, "");
	REP(j, m)
	{
		string s;
		ifs >> s;
		a[j] = s;
	}
	
	memset(was, -1, sizeof(was));
	int res = go(0, 0);

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
