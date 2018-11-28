/* Google Code Jam 2012 Round 1B. imiro. */
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

int ar[25], num[25];
bool found = 0;

void f(int id) {
	if(id==20) {
		int s1 = 0, s2 = 0;
	//	rep(i,20) printf("%d ", ar[i]); puts("");
		rep(i,20) {
			if(ar[i]==1) s1 += num[i];
			else if(ar[i]==2) s2 += num[i];
		}
	//	printf("%d %d\n", s1, s2);
		if(s1==s2 && s1 != 0) {
		//	printf("found %d %d\n", s1, s2);
		//	rep(i,20) printf("%d ", ar[i]); puts("");
			found = 1;
			vi ans, ans1;
			rep(i,20) if(ar[i]==1) ans.pb(num[i]);
			rep(i,20) if(ar[i]==2) ans1.pb(num[i]);
			rep(i,sz(ans)-1) printf("%d ", ans[i]); printf("%d\n", ans.back());
			rep(i,sz(ans1)-1) printf("%d ", ans1[i]); printf("%d\n", ans1.back());
			return;
		}
	//	puts("oi");
		return;
	}
	
	if(found) return;
	rep(i,3) {
		ar[id] = i;
		if(!found) f(id+1);
		else break;
	}
}

int main() {
	int T = SI;
	FOR(t,1,T) {
		int tmp = SI;
		rep(i,tmp) scanf("%d", &num[i]);
		printf("Case #%d:\n", t);
		found = 0;
		f(0);
	}
	return 0;
}