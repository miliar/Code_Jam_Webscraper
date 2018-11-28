#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <list>
#include <stack>
#include <set>
#include <map>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof( V.begin() ) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

void testcase(int v) {
	printf("Case #%d: ", v);
	LL r, k, n;
	scanf("%lld %lld %lld", &r, &k, &n);
	vector<LL> peo, sums;
	vector<int> dist;
	peo.resize(2*n);
	sums.resize(2*n);
	dist.resize(2*n);
	REP(i,n) {
		LL s;
		scanf("%lld", &s);
		peo[i] = peo[i+n] = s;
	}
	
	REP(i,n) {
		int latacz = i+1;
		LL tmp_sum = peo[i];
		while(latacz-i+1 <= n && tmp_sum + peo[latacz] <= k) {
			tmp_sum += peo[latacz];
			++latacz;
		}
		dist[i] = latacz%n;
		sums[i] = tmp_sum;
	}
	
	int aktual = 0;
	LL result = 0;
	REP(i,r) {
		result += sums[aktual];
		aktual = dist[aktual];
	}
	
	printf("%lld\n", result);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i,t) testcase(i+1);
	return 0;
}

