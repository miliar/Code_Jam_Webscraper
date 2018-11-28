#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <random>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a) 


int w, l;
int np;
double x[1000], y[1000], r[1000];
double mindst;

bool can_place(double cx, double cy, double cr)
{
	if (cx < 0 || cy < 0 || cx > w || cy > l) return false;

	mindst = min(cx*cx, cy*cy);
	mindst = min(mindst, (w-cx)*(w-cx));
	mindst = min(mindst, (l-cy)*(l-cy));
	REP(i,np) {
		double dst = (x[i]-cx)*(x[i]-cx) + (y[i]-cy)*(y[i]-cy) - (r[i]+cr)*(r[i]+cr);
		if ( dst < 1e-8 )
			return false;
		if (dst < mindst)
			mindst = dst;
	}

	return true;
}

int randomn(int m)
{
	int n = ((rand()&1023)<<20)|((rand()&1023)<<10)|((rand()&1023));
	return n%(m+1);
}

int main() 
{
	ifstream fin("B-small-attempt0.in");
	//ifstream fin("B-large.in");
	//ifstream fin("B.in");
	ofstream fout("B.out");

	int tc;

	int n;
	int rr[1000];

	fin >> tc;

	REP(tcase,tc) {
		fin >> n >> w >> l;

		REP(i,n) fin >> rr[i];

		np = 0;
		REP(i,n) {
			double bestx, besty, bestdst = 1e100, nx, ny;
			int cnt = 0;
			while (bestdst > 1e50 || cnt < 1000) {
				nx = randomn(w);
				ny = randomn(l);
				if (can_place(nx, ny, rr[i]) && mindst < bestdst) {
					bestdst = mindst;
					bestx = nx;
					besty = ny;
				}
				++cnt;
			}

			x[np] = bestx;
			y[np] = besty;
			r[np] = rr[i];
			++np;
		}

		fout.precision(12);
		fout << "Case #" << tcase+1 << ":";
		REP(i,n) fout << " " << x[i] << " " << y[i];
		fout << endl;
		cerr << tcase << " " << tc << endl;
	}

	fout.close();

	return 0;
}