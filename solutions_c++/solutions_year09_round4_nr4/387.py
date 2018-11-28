#pragma comment(linker,"/STACK:32000000")
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <queue>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <string>

using namespace std;

#define infile ".in"
#define outfile ".out"
#define FOR(i, n) for (int i = 0; i <(n); i++)
#define DFOR(i, n) for (int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()
#define LL long long
#define SQR(x) ((x) * (x))
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define CLR(a, b) memset((a), (b), sizeof(a))
#define SS stringstream
#define PII pair<int, int>
#define VPII vector < PII >

void init(){
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);
}

#define maxn 50

int n;
double x[maxn], y[maxn], r[maxn];

double getr(int i, int j){
	return (sqrt((double)SQR(x[i]-x[j])+SQR(y[i]-y[j]))+r[i]+r[j])*0.5;
}


double solvecase(){
	if(n==1) return r[0];
	if(n==2) return max(r[0], r[1]);
	double ans = max(getr(0, 1), r[2]);
	ans = min(ans, max(getr(0, 2), r[1]));
	ans = min(ans, max(getr(1, 2), r[0]));
	return ans;
}

void solve(){
	int t;
	cin >> t;
	FOR(q, t){
		printf("Case #%d: ", q+1);
		cin >> n;
		FOR(i, n) cin >> x[i] >> y[i] >> r[i];
		double ans = solvecase();
		printf("%.6lf\n", ans);
	}
}

int main(){
	init();
	solve();
	return 0;
}