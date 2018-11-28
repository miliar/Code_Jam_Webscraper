#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

const int N = 1036;
int p[N];
int l[N];
int a[N];
int n;
double dp[N];

typedef pair<pii,int> T;
T pr[N];

bool cmp(T &a, T &b) {
	if (a.x.y == b.x.y) {
		if (a.x.x == b.x.x) return a.y < b.y;
		return a.x.x > b.x.x;
	}
	return a.x.y > b.x.y;
}

int main() {
	int T; cin >> T;
	FOE(ca, 1, T) {
		printf("Case #%d:", ca);
		cin >> n;
		FOR(i, 0, n) cin >> pr[i].x.x;//l[i];
		FOR(i, 0, n) cin >> pr[i].x.y;//p[i];
		FOR(i, 0, n) pr[i].y = i;
		
	//	FOR(i, 0, n) a[i] = i;
		sort(pr, pr+n, cmp);
		FOR(i, 0, n) printf(" %d", pr[i].y); puts("");
/*
		vi v;
		double best = 1e20;
		do {
			
		} while (next_permutation(a, a+n));
*/
	}
	return 0;
}
