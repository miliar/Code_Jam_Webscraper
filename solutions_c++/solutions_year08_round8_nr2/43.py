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

int w[301][301][301];

void testcase(int tst)
{

	vector<pair< pair<int, int>, string>  > t;
	vector<pair< pair<int, int >, int> > e;

	int n;
	ifs >> n;


	VS cl;
	VI fn;

	
	ofs << "Case #" << tst+1 << ": ";

	REP(i, n) {

		string s;
		char buf[100];
		ifs >> buf;
		s = buf;

		if (find(ALL(cl), s) == cl.end())
			cl.pb(s);

		int a, b;
		ifs >> a >> b;

		if (find(ALL(fn), a) == fn.end())
			fn.pb(a);

		if (find(ALL(fn), b) == fn.end())
			fn.pb(b);

		t.pb(mp(mp(b, a), s));

	}

	sort(ALL(t));

	sort(ALL(fn));

	if (fn[0] != 1 || fn.back() != 10000) { ofs << "IMPOSSIBLE" << endl; return; }

	map<string, int> clm;
	REP(i, cl.sz)
		clm[cl[i]] = i;

	map<int, int> fnm;

	VI ind(fn.sz);

	REP(i, fn.sz) {
		fnm[fn[i]] = i;
		ind[i] = fn[i];
	}

	REP(i, t.sz) {
		e.pb(mp(mp(fnm[t[i].fs.fs], fnm[t[i].fs.sc]), clm[t[i].sc]));
	}

	memset(w, 1000, sizeof(w));

	int c = cl.sz;
	int k = fn.sz;

	VVI u(c+1, VI());
	REP(i, e.sz)
		u[e[i].sc].pb(i);


	REP(i, n) {
		REP(c2, c+1)
			REP(c1, c2+1) {
				
				int b = e[i].fs.fs;
				int a = e[i].fs.sc;
				int c = e[i].sc;

				int res = 1000;

				if (a == 0)
					res = 1;

				REP(l, u[c].sz) {
					
					int j = u[c][l];
					if (j >= i) continue;

					if (ind[e[j].fs.fs]+1 >= ind[a]) {
						res = min(res, w[j][min(c1,c2)][max(c1,c2)]+1);
					}

				}

				REP(l, u[c1].sz) {
					
					int j = u[c1][l];
					if (j >= i) continue;

					if (ind[e[j].fs.fs]+1 >= ind[a]) {
						res = min(res, w[j][min(c,c2)][max(c,c2)]+1);
					}

				}

				REP(l, u[c2].sz) {
					
					int j = u[c2][l];
					if (j >= i) continue;

					if (ind[e[j].fs.fs]+1 >= ind[a]) {
						res = min(res, w[j][min(c,c1)][max(c,c1)]+1);
					}

				}

				w[i][c1][c2] = res;
		}
//		cout << i << endl;
	}
	
	int res = 1000;
	REP(i, n)
		REP(c2, c+1)
			REP(c1, c2+1)
				if (ind[e[i].fs.fs] == 10000)
					res = min(res, w[i][c1][c2]);

	int o = 1;
	if (res < 1000) ofs << res << endl;
	else
		ofs << "IMPOSSIBLE" << endl;
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
