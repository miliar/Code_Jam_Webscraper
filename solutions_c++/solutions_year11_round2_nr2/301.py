#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PI;
typedef vector<PI> VPI;
typedef unsigned long long ull;
typedef long long ll;
typedef long double LD;

#define FOR(i, n) for(typeof(n) i=0;i<(n);++i)
#define REP(i,s,n) for(typeof(n) i=s;i<=n;++i)
#define SZ(x) ((int)(x).size())
#define LOOP(i,x) FOR(i,SZ(x))
#define IT(it,x) for(typeof((x).begin()) it = (x).begin();it!=(x).end();++it)
#define ALL(x) (x).begin(), (x).end()
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define INF 2000000999
#define EPS 1e-8

#define MX 1000005
int pt[MX], n, D;

bool ok(LD t) {
	LD cur = pt[0] - t, nxt, tmp;
	//cout << t << ": " << cur << " ";
	REP(i, 1, n - 1) {
		tmp = cur + D;
		if(tmp < pt[i]) {
			nxt = max(pt[i] - t, tmp);
		} else {
			nxt = min(pt[i] + t, tmp);
		}
		//cout << nxt << " ";
		if(fabs(cur - nxt) + EPS < D)
			return false;
		cur = nxt;		
	}
	
	return true;
}

LD solve() {
	LD lo = 0, hi = 1e12;
	
	for(int iter = 100; fabs(hi - lo) > EPS && iter--; ) {
		LD m = (lo + hi) / 2;
		if(ok(m))
			hi = m;
		else
			lo = m + EPS;
		//cout << endl;
	}
	
	return (lo + hi) / 2;
}

int main() {
	//freopen("sample.txt", "r", stdin);freopen("out-sample.txt", "w", stdout);
	//freopen("B-small-attempt0.in", "r", stdin);freopen("out-small.txt", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("out-large.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for(int kase = 1; kase <= T; ++kase) {
		cerr << kase << endl;
		printf("Case #%d: ", kase);
		int C, P, V;
		scanf("%d %d", &C, &D);
		n = 0;
		FOR(i, C) {
			scanf("%d %d", &P, &V);
			FOR(j, V)
				pt[n + j] = P;
			n += V;
		}
		
		cout.precision(7); cout.setf(ios::fixed,ios::floatfield);
		cout << solve() << endl;
	}
	return 0;
}
