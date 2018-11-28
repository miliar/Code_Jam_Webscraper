using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(int i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 1000
#define GI ({int _; scanf("%d", &_);_;})
#define INF (LL)1e18
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;
typedef vector<int> VI;

int main() {
	LL kases = GI+1;	
	FOR(kase, 1, kases) {
		int n = GI, a[n], b[n], c=0;
		REP(i,n) a[i] = GI, b[i] = GI;
		REP(i,n) REP(j,i) if((a[i]-a[j])*(b[i]-b[j]) < 0) c++;



		printf("Case #%d: %d\n", kase, c);
	}
}
