/* */
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
#define MAX 105

int S, P, data[MAX], n;

int main() {
	int TT = SI;
	FOR(T,1,TT) {
		scanf("%d%d%d", &n, &S, &P);
		rep(i,n) data[i] = SI;
		int ans = 0;
		rep(i,n) {
			int k = data[i] / 3;
			if(data[i]%3) ++k;
			if(k >= P) ++ans;
			else if(S && data[i]%3 != 1 && k+1 >= P && 
					data[i] != 0 && data[i] != 1 && data[i] != 29 && data[i] != 30) { ++ans; --S; }
		}
		printf("Case #%d: %d\n", T, ans);
	}
	return 0;
}