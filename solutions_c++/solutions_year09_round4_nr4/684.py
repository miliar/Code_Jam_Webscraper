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
typedef long double ld;

#define sqr(z) (z)*(z)

ll calcdet(VVI &a) {

	ll res = 0;
	res += (ll)a[0][0]*a[1][1]*a[2][2];
	res -= (ll)a[0][0]*a[1][2]*a[2][1];
	res -= (ll)a[0][1]*a[1][0]*a[2][2];
	res += (ll)a[0][1]*a[1][2]*a[2][0];
	res += (ll)a[0][2]*a[1][0]*a[2][1];
	res -= (ll)a[0][2]*a[1][1]*a[2][0];
	return res;

}

bool calculatecenter(VI& x, VI& y, VI& r, ld& xc, ld& yc, ld& rc) {

	x.pb(x[0]);
	y.pb(y[0]);
	r.pb(r[0]);

	VVI a(3, VI(3, 0));
	VI b(3, 0);

	REP(i, 3) {

		int j = i+1;
		a[i][0] = 2*(x[i]-x[j]);
		a[i][1] = 2*(y[i]-y[j]);
		a[i][2] = 2*(r[j]-r[i]);
		b[i] = sqr(x[i]) - sqr(x[j]) + sqr(y[i]) - sqr(y[j]) + sqr(r[j]) - sqr(r[i]);

	}

	VVI c = a;

	ll d = calcdet(c);
	
	if (d == 0) return false;

	REP(i, 3)
		c[0][i] = b[i];
	ll xd = calcdet(c);
	c = a;

	REP(i, 3)
	c[1][i] = b[i];
	ll yd = calcdet(c);
	c = a;

	REP(i, 3)
	c[2][i] = b[i];
	ll rd = calcdet(c);
	c = a;

	xc = (ld)xd/d;
	yc = (ld)yd/d;
	rc = (ld)rd/d;

	return true;
}

void testcase(int tst)
{
	int n;
	VI x, y, r;

	ifs >> n;
	x.assign(n, 0);
	y.assign(n, 0);
	r.assign(n, 0);

	REP(i, n)
		ifs >> x[i] >> y[i] >> r[i];

/*	vector<pair<ld, pair<ld,ld> > > t;

	REP(i, n)
		t.pb(mp(r[i], mp(x[i], y[i])));

	REP(i, n)
		REP(j, i)
			REP(k, j) {
				
				ld xc, yc, rc;

				VI xn, yn, rn;
				xn.pb(x[i]); xn.pb(x[j]); xn.pb(x[k]);
				yn.pb(y[i]); yn.pb(y[j]); yn.pb(y[k]);
				rn.pb(r[i]); rn.pb(r[j]); rn.pb(r[k]);
				
				if (calculatecenter(xn, yn, rn, xc, yc, rc)) {
					t.pb(mp(rc, mp(xc, yc)));
				}
			} 


	bool found = false;
	ld res = 0;

	sort(ALL(t));
	REP(i, t.sz) {

		ld x1 = t[i].sc.fs;
		ld y1 = t[i].sc.sc;

		REP(j, i) {

			ld x2 = t[j].sc.fs;
			ld y2 = t[j].sc.sc;

			ld rr = max(t[i].fs, t[j].fs);

			bool ok = true;
			REP(k, n)
				if (!((sqr(x1-x[k]) + sqr(y1-y[k]) < sqr(rr-r[k]) + 1E-7) ||
					(sqr(x2-x[k]) + sqr(y2-y[k]) < sqr(rr-r[k]) + 1E-7))) {
						ok = false;
				}
			
			if (ok) {
				found = true;
				res = rr;
				break;
			}

		}
		if (found) break;
	} */

	ld res = 1E+20;

	if (n == 1) res = r[0];
	if (n == 2) res = max(r[0], r[1]);
	if (n == 3) {

		ld dst = max((ld)r[0], (ld)(sqrt((ld)(sqr(x[1]-x[2])+sqr(y[1]-y[2]))) + r[1] + r[2])/2);
		res = min(res, max((ld)r[0], (ld)(sqrt((ld)(sqr(x[1]-x[2])+sqr(y[1]-y[2]))) + r[1] + r[2])/2));
		res = min(res, max((ld)r[1], (ld)(sqrt((ld)(sqr(x[0]-x[2])+sqr(y[0]-y[2]))) + r[0] + r[2])/2));
		res = min(res, max((ld)r[2], (ld)(sqrt((ld)(sqr(x[0]-x[1])+sqr(y[0]-y[1]))) + r[0] + r[1])/2));

	}

	char buf[50];
	sprintf(buf, "%.6llf", res);

	ofs << "Case #" << tst+1 << ": " << buf << endl;
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
