#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define FORD(i,a,b) for (int i = (int)(a)-1; i >= (int)(b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,a) FORD(i,a,0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define SIZE(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-12;
const int INF = 1000000000;

int tc, n;
int v[1000];
double d, x[1000], lo, hi, mi;

bool ok (double mi){
	double tx = -1e14;
	REP(i,n){
		if (tx < x[i]-mi) tx = x[i]-mi;
		tx += d*(v[i]-1);
		if (tx>x[i]+mi) return false;
		tx += d;
	};
	return true;
};

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n >> d;
		REP(i,n) cin >> x[i] >> v[i];
		lo = 0;
		hi = 1e14;
		while (true){
			mi = (lo+hi)/2;
			if (mi==lo || mi==hi) break;
			if (ok (mi)) hi = mi;
			else lo = mi;
		};
		printf ("Case #%d: %.8lf\n", ic+1, (lo+hi)/2);
	};
	
	return 0;
};