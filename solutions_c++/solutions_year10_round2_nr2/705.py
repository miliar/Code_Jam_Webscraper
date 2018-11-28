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
#define GI ({LL _; scanf("%Ld", &_);_;})
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
		LL n = GI, k =GI, b = GI, t = GI, x[n], v[n];
		REP(i,n) x[i] = GI;
		REP(i,n) v[i] = GI;
//		REP(i,n) cout << (double)(b-x[i])/v[i] <<" "; cout << endl;
		LL N = 1<<n, fullans=INF;
		REP(i,N) {
			LL sw = 0, ans =0, valid=0;
			for(int j= n-1; j>=0;j--) if((i&(1<<j)) && (LL)(b-x[j]) <= (LL)(t) * (LL)v[j]) {
				ans += sw;
				valid++;
			}
			else sw++;
			if(valid == k) {
				fullans = min(ans,fullans);
			}
		}
		printf("Case #%d: ", kase);
		if(fullans == INF) printf("IMPOSSIBLE\n");
		else cout << fullans << endl;
		

	}
}
