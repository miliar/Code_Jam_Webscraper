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

#define maxn 110
#define maxl 1<<17

int n, k;
int pr[maxn][maxn];
int ans;
bool used[maxl];
vector<int> v;
bool Can[maxl];
int dp[maxl];


bool can(int i, int j){
	FOR(s, k) if(pr[i][s]==pr[j][s]) return false;
	FOR(s, k)if(s){
		if(pr[i][s-1]>pr[j][s-1] && pr[i][s]<pr[j][s]) return false;
		if(pr[i][s-1]<pr[j][s-1] && pr[i][s]>pr[j][s]) return false;
	}
	return true;
}

int bit(int x, int i){
	return ((x & (1<<i))==0) ? 0 : 1;
}

void precalc(){
	FOR(x, 1<<n){
		v.clear();
		bool f = true;
		FOR(j, n)if(bit(x, j)) v.PB(j);
		FOR(i, v.size()) FOR(j, v.size()) if(j>i) 
			if(!can(v[i], v[j])) {f = false; break;}
		Can[x] = f;
	}
}

int go(int mask){
	if(used[mask]) return dp[mask];
	used[mask] = true;
	if(Can[mask]) return dp[mask] = 1;	
	int ans = 1000;
	for (int s=mask; s; s=(s-1)&mask){
		int s1 = mask ^ s;
		if(s==mask || s1==mask) continue;
		//if((!Can[s]) || (!Can[s1])) continue;
		ans = min(ans, go(s)+go(s1));
	}	
	return dp[mask]=ans;
}

void solvecase(){
	CLR(used, false); CLR(dp, 0); CLR(Can, false);
	precalc();
	used[0] = true;
	dp[0] = 0;
	printf("%d\n", go((1<<(n))-1));
}

void solve(){
	int t;
	cin >> t;
	FOR(q, t){
		printf("Case #%d: ", q+1);
		cin >> n >> k;
		FOR(i, n) FOR(j, k) cin >> pr[i][j];
		solvecase();
	}
}

int main(){
	init();
	solve();
	return 0;
}