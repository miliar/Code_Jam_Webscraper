/* GCJ 2012 1C - imiro */
#define OYE using namespace std
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>

OYE;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<char> vc;
typedef vector<string> vs;

#define SQR(a) ((a)*(a))
#define REP(i,s,n) for(int (i)=(s), _n = (n);(i)<_n;(i)++)
#define FOR(i,s,n) for(int (i)=(s), _n = (n);(i)<=_n;(i)++)
#define rep(i,n) REP(i,0,n)

#define All(v) (v).begin(), (v).end()
#define Reversed(v) (v).rbegin(), (v).rend()
#define sz(v) (int) v.size()

#define mp make_pair
#define pb push_back
#define ji first
#define ro second

#define SI ({int x; scanf("%d", &x); x;})

inline void OPEN(string a, bool out = false) {
	freopen(string(a + ".in").c_str(), "r", stdin);
	if(out) freopen(string(a + ".out").c_str(), "w", stdout);
}

#define EPS 1e-7

#define MAX 1005
vi G[MAX];
bool found, visit[MAX];
int N;

void dfs(int v) {
	if(visit[v]) { found = 1; return; }
	visit[v] = 1;
	rep(i,sz(G[v])) dfs(G[v][i]);
}

int main() {
	int TT = SI;
	FOR(T,1,TT) {
		printf("Case #%d:", T);
		N = SI;
		FOR(i,1,N) G[i].clear();
		FOR(i,1,N) {
			int num = SI;
			while(num--) {
				int a = SI;
				G[a].pb(i);
			}
		}
		
		found = 0;
		FOR(i,1,N) {
			memset(visit,0,sizeof visit);
			dfs(i);
			if(found) { puts(" Yes"); break; }
		}
		
		if(!found) puts(" No");
	}
}