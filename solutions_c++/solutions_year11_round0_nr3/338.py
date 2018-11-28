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
int a[1000];

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n;
		REP(i,n) cin >> a[i];
		sort (a, a+n);
		int ans = 0;
		REP(i,n) ans += a[i]; ans -= a[0];
		int r = 0;
		REP(i,n) r ^= a[i];
		printf ("Case #%d: ", ic+1);
		if (r) printf ("NO\n");
		else printf ("%d\n", ans);
	};
	return 0;
};