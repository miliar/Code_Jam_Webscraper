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

#define REP(i,n) for (int i = 0; i < n; ++i)
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define SQR(a) (a)*(a)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define SIZE(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define y1 yyyyyyyyyy1
#define LL long long
#define LD long double
const double PI = 2*acos(0.0);
const double EPS = 1e-8;
const int INF = 1000000000;

int n, tc, D;
int d[20000], l[20000], u[20000];

bool dfs (int v, int dst){
	if (d[v]+dst >= D) return true;
	if (u[v] >= dst) return false;
	u[v] = dst;
	for (int i = v-1; i>=0 && d[i]>=d[v]-dst; --i) if (dfs (i, MIN(l[i], d[v]-d[i]))) return true;
	for (int i = v+1; i<n && d[i]<=d[v]+dst; ++i) if (dfs (i, MIN(l[i], d[i]-d[v]))) return true;
	return false;
}

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n;
		REP(i,n) cin >> d[i] >> l[i];
		REP(i,n) u[i] = 0;
		cin >> D;
		cout << "Case #" << ic+1 << ": ";
		if (dfs (0, d[0])) cout << "YES\n";
		else cout << "NO\n";
	}
	return 0;
};