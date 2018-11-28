#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
const int MAXN = 1005;
int T, N, a[MAXN], totx, tot;
PII dp[MAXN];
/*int solve2(){
	vector<int> v;
	REP(i, N) v.push_back(a[i]);
	int ret = -INF;
	for(int mask = 1; mask < (1<<N) - 1; mask ++){
		int x = 0, y = 0;
		for(int i = 0; i < N; i ++){
			if(mask & (1<<i)) x ^= v[i];
			else y ^= v[i];  
		}
		if(x == y){
			tot = 0;
			REP(i, N) if(mask & (1<<i)) tot +=  v[i];
			ret = max(ret, tot);
		}
	}
	return ret;
}*/
PII go(int idx){
	if(idx == N){
		return PII(0, 0);
	}
	PII & ret = dp[idx];
	if(ret.first != -1) return ret;
	ret = go(idx + 1);
	for(int i = idx + 1; i <= N; i ++){
		PII next = go(i);
		if(a[idx] + next.first == tot) continue;
		//if splitted into two
		if(((a[idx] ^ next.second) ^ totx) == (a[idx] ^ next.second)){
			if(ret.second == -1){
				ret.second = a[idx] ^ next.second;
				ret.first = a[idx] + next.first;
			}
			if(ret.first < a[idx] + next.first){
				ret.first = a[idx] + next.first;
				ret.second = a[idx] ^ next.second;
			}
		}
	}
	return ret;
}
int solve(){
	REP(i, MAXN) dp[i] = PII(-1, -1);
	totx = 0, tot = 0;
	sort(a, a + N);
	REP(i, N) totx ^= a[i], tot += a[i];
	PII ret = go(0);
	/*for(int i = 0; i < N; i ++){
		PII p = go(i);
		if(p.second == -1) continue;
		if(ret.second == -1) ret = p;
		if(ret.first < p.first) ret = p;
		
	}*/
	if(ret.second == -1 || ret.second == 0 || ret.second == tot) return -INF;
	return ret.first; 
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c-large.out", "w", stdout);
	cin>>T;
	REP(t, T){
		cin>>N;
		REP(i, N){
			cin>>a[i];
		}
		int ret = solve();
		cout<<"Case #"<<(t+1)<<": ";
		if(ret == -INF){
			cout<<"NO\n";
		}
		else{
			cout<<ret<<"\n";
		}
	}
	cout.flush();
	return 0;
}
