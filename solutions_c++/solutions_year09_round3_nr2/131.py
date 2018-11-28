#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <time.h>
#include <algorithm> 
#include <iostream>  
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <cassert>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
#define FILL(a,b) memset(a, (b), sizeof(a));
typedef long long ll; 
const double EPS = 1e-9;

void openfiles() {
	#ifndef ONLINE_JUDGE
		freopen("B-large.in","rt",stdin);
		freopen("test.out","wt",stdout);   
	#endif
}

double get_dist ( double x, double y, double z ) {
	return sqrt ( x * x + y * y + z * z );
}

void solve() {
	int n;
	scanf("%d ",&n);
	double Vx = 0, Vy = 0, Vz = 0;
	double X = 0, Y = 0, Z = 0;
	for (int i = 0; i < n; i++) {
		int x, y, z, vx, vy, vz;
		scanf("%d %d %d %d %d %d ",&x, &y, &z, &vx, &vy, &vz);
		X += x; Y += y; Z += z; Vx += vx; Vy += vy; Vz += vz;
	}
	X /= n, Y /= n, Z /= n, Vx /= n, Vy /= n, Vz /= n;

	// special case - it's a dot!
	static int test = 0;
	if ( fabs ( Vx ) < EPS && fabs ( Vy ) < EPS  && fabs ( Vz ) < EPS ) {
		double dist = sqrt ( X * X + Y * Y + Z * Z );
		printf("Case #%d: %.8lf %.8lf\n", ++test, dist, 0 );
		return;
	}

	double mint = 0, maxt = 1e20;
	double diff = maxt - mint;
	while ( diff > EPS || maxt - mint > EPS ) {
		double left_t = mint + (maxt - mint) * 1 / 3.0;
		double right_t = mint + (maxt - mint) * 2 / 3.0;
		double left_dist = get_dist ( X + Vx * left_t, Y + Vy * left_t, Z + Vz * left_t );
		double right_dist = get_dist ( X + Vx * right_t, Y + Vy * right_t, Z + Vz * right_t );
		diff = fabs ( left_dist - right_dist );
		if ( left_dist > right_dist ) {
			mint = left_t;
		}
		else {
			maxt = right_t;
		}
	}

	double midt = mint + (maxt - mint) / 2;

	printf("Case #%d: %.8lf %.8lf\n", ++test, get_dist ( X + Vx * midt, Y + Vy * midt, Z + Vz * midt ), midt);
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}