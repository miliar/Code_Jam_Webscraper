// GCJ 2012 Round 2. imiro.
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

#define MAX 10005
#define HINF 1111000111

int reach[MAX], length[MAX], dist[MAX];
int n, D;

int main() {
	int T = SI;
	FOR(tc,1,T) {
		printf("Case #%d: ", tc);
		n = SI;
		rep(i,n) scanf("%d%d", &dist[i], &length[i]);
		scanf("%d", &D);
		
		for(int i=n-1;i >= 0;--i) {
			reach[i] = (D-dist[i] > length[i] ? HINF : D-dist[i]);
			for(int j=i+1;j < n;++j) {
				if( reach[j] <= min(dist[j]-dist[i], length[j]) && // reach bisa dicapai dengan tali selanjutnya
					(reach[j] <= length[i]) && // reach bisa dicapai
					(dist[j]-dist[i] <= length[i]) ) // jarak bisa ditempuh
					reach[i] = min( reach[i], max(reach[j], dist[j]-dist[i]) );
			}
		}
		
	//	rep(i,n) printf("%d ", reach[i]); puts("");
		
		puts( (dist[0] >= reach[0] && reach[0] <= D) ? "YES" : "NO");
	}
	return 0;
}