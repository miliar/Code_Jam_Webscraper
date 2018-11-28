#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int INF = 1<<30;                
const double EPS = 1e-9;
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;

#define ALL(a) a.begin(),a.end()
#define PB push_back
#define MP make_pair
#define SZ(a) (int)a.size()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FOR(i,a,n) for(int i=(a);i<(n);++i)
#define FORD(i,a,n) for(int i=(a);i>=(n);--i)
#define REP(i,n) FOR(i,0,n) 


/// CODE HERE

const int N = 305;
struct node {	
	int x, y;
};

bool operator<(const node& a, const node& b) {
	if (a.x != b.x) return a.x < b.x;
	return a.y > b.y;
}

char color[N][256];
node a[N];
int n, m;
map<string,VI> ID;
string name[N];
node b[N];
int bn;

int calc() {
	sort(b, b+bn);
	int last = 1;
	int ans = 0;
	REP(i,bn) {
		if (last > 10000) break;
		if (last < b[i].x) return -1;
		int j = i;
		int next = 0;		
		for (; j < bn; ++j) {
			if (last < b[j].x) break;			
			next = max(next, b[j].y);			
		}
		i = j-1;			
		++ans;		
		last = next+1;
	}
	if (last > 10000) return ans;
	return -1;
}


int solve() {
	int best = 1000;
	REP(c1,m) REP(c2,c1) REP(c3,c2) {
		bn = 0;
		VI& a1 = ID[name[c1]];
		VI& a2 = ID[name[c2]];
		VI& a3 = ID[name[c3]];
		REP(i,SZ(a1)) b[bn++] = a[a1[i]];
		REP(i,SZ(a2)) b[bn++] = a[a2[i]];
		REP(i,SZ(a3)) b[bn++] = a[a3[i]];
		int cur = calc();
		if (cur != -1 && cur < best)
			best = cur;
	}
	REP(c1,m) REP(c2,c1){
		bn = 0;
		VI& a1 = ID[name[c1]];
		VI& a2 = ID[name[c2]];
		//VI& a3 = ID[color[c3]];
		REP(i,SZ(a1)) b[bn++] = a[a1[i]];
		REP(i,SZ(a2)) b[bn++] = a[a2[i]];
		//REP(i,SZ(a3)) b[bn++] = a[a3[i]];
		int cur = calc();
		if (cur != -1 && cur < best) best = cur;
	}
	REP(c1,m){
		bn = 0;
		VI& a1 = ID[name[c1]];
		//VI& a2 = ID[color[c2]];
		//VI& a3 = ID[color[c3]];
		REP(i,SZ(a1)) b[bn++] = a[a1[i]];
		//REP(i,SZ(a2)) b[bn++] = a[a2[i]];
		//REP(i,SZ(a3)) b[bn++] = a[a3[i]];
		int cur = calc();
		if (cur != -1 && cur < best) best = cur;
	}
	return best;
}


int main() {
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);

  int T; scanf("%d", &T);
  FOR(NT,1,T+1) {		
		scanf("%d\n", &n);		
		ID.clear();
		set<string> S;
		REP(i,n) {
			scanf("%s %d %d", color[i], &a[i].x, &a[i].y);
			ID[color[i]].PB(i);
			S.insert(color[i]);
		}		
		m = 0;
		for (set<string>::iterator it = S.begin(); it != S.end(); ++it)
			name[m++] = *it;
		
		
		printf("Case #%d: ", NT);
		int best = solve();
		if (best < 1000) printf("%d", best);
		else printf("IMPOSSIBLE");
		printf("\n");


  }


  return 0;
}