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

int n;
VI x,y,z,vx,vy,vz;

ld calclen(ld t) {

	ld res = 0.0;

	ld cr = 0.0;
	REP(i, n)
		cr += x[i] + t * vx[i];
	cr /= n;

	res += cr * cr;

	cr = 0.0;
	REP(i, n)
		cr += y[i] + t * vy[i];
	cr /= n;

	res += cr * cr;

	cr = 0.0;
	REP(i, n)
		cr += z[i] + t * vz[i];
	cr /= n;

	res += cr * cr;

	return sqrt(res);
}

void testcase(int tst)
{
	ifs >> n;

	x.assign(n, 0);
	y.assign(n, 0);
	z.assign(n, 0);
	vx.assign(n, 0);
	vy.assign(n, 0);
	vz.assign(n, 0);

	REP(i, n)
		ifs >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];

	ll vxs = 0;
	REP(i, n) vxs += vx[i];
	
	ll vys = 0;
	REP(i, n) vys += vy[i];

	ll vzs = 0;
	REP(i, n) vzs += vz[i];

	ll a = 0;
	REP(i, n) a += vxs * x[i];
	REP(i, n) a += vys * y[i];
	REP(i, n) a += vzs * z[i];

	ll b = 0;
	REP(i, n) b += vxs * vx[i];
	REP(i, n) b += vys * vy[i];
	REP(i, n) b += vzs * vz[i];

	ld tmin = 0.0, dmin = calclen(0.0);
	if (b != 0) {
		ld ntmin = - ((ld) a) / b;
		ld ndmin = calclen(ntmin);

		if (ntmin > 0.0 && ndmin < dmin - 1E-8) {
			dmin = ndmin;
			tmin = ntmin;
		}
	}

	char buf[50];
	sprintf(buf, "%.8llf %.8llf", dmin, tmin);


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
