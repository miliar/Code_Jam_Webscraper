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
#define LD long double
const double PI = 2*acos(0.0);
const double EPS = 1e-8;
const int INF = 1000000000;

LL n;
int tc, pd, pg;

bool ok(LL n, int pd, int pg){
	if (pg==0 && pd) return false;
	if (pg==100 && pd<100) return false;
	if (pg==0) return true;
	if (pg==100) return true;
	int wont = 0;
	int today = 1;
	if (pd > 0){
		wont = 1;
		while ((wont*(100-pd))%pd || 100*wont != pd*(wont+(wont*(100-pd))/pd)) ++wont;
		today = wont + (wont*(100-pd))/pd;
		if (today > n) return false;
	};
	return true;
};

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n >> pd >> pg;
		printf ("Case #%d: ", ic+1);
		if (ok(n, pd, pg)) printf ("Possible\n");
		else printf ("Broken\n");

	};
	return 0;
};