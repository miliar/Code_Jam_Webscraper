#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <sstream>
#include <cstring>
using namespace std;

#define FALL(ii,vv) for (int (ii)=0; (ii)<(vv).size();(ii)++)
#define REP(i,b) for(int (i)=(0);(i)<(b);(i)++)
#define FUP(i,a,b) for(int (i)=(a); (i)<=(b); (i)++)
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef vector<int> vi;
typedef long long ll;

const int INF = 1000000007;
ll DP[1<<11][11][11];
int n;
int cost[11][1<<11];
int x[1<<11];

ll go(int pos,int faza,int wyzej_kupione){
	if (DP[pos][faza][wyzej_kupione] != -1)
		return DP[pos][faza][wyzej_kupione];
		
	if (faza == 0){
		int lol = max(x[2*pos],x[2*pos+1]);
		if (wyzej_kupione+1<lol) return 12345671234567LL;
		if (wyzej_kupione+1 == lol) return cost[faza][pos];
		return 0;
	}
	
	ll r1 = go(2*pos,faza-1, wyzej_kupione) + go(2*pos+1,faza-1, wyzej_kupione);
	ll r2 = go(2*pos,faza-1, wyzej_kupione+1) + go(2*pos+1,faza-1, wyzej_kupione+1) + cost[faza][pos];
	DP[pos][faza][wyzej_kupione] = min(min(r1,r2),12345671234567LL);
	return DP[pos][faza][wyzej_kupione];
}

int main(){
	int test;
	scanf("%d",&test);
	REP(tN,test){
		scanf("%d",&n);
		REP(i,1<<n){ scanf("%d",&x[i]); x[i]=n-x[i]; }
		
		REP(i,n) REP(j,1<<(n-i-1))
			scanf("%d",&cost[i][j]);
		
		REP(i,1<<n) REP(j,11) REP(k,11) DP[i][j][k] = -1;
		
		printf("Case #%d: %lld\n",tN+1,go(0,n-1,0));
	}
	return 0;
}
