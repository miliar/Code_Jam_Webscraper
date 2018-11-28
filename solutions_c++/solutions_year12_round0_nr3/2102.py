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

set<pair<int,int> > s;
char x[10];

int main() {
	int TT = SI;
	FOR(T,1,TT) {
		int a = SI, b = SI, num, ans = 0;
		s.clear();
		FOR(i,a,b) {
			sprintf(x, "%d", i);
			int n = strlen(x);
			//printf("a %s\n", x);
			for(int j=n-1; j; --j) { // geser, dengan elemen asli ke-j jadi awal
				char c = x[n-1];
				for(int k=n-1; k; --k) x[k] = x[k-1];
				x[0] = c;
				//printf(" - %s\n", x);
				
				if(c != '0') {
					sscanf(x, "%d", &num);
					if(num != i && a <= num && num <= b && i < num && s.count( mp(num,i) ) == 0) {
				//		if(s.count( mp(num,i) ) != 0) printf("%d %d\n", num, i);
						s.insert( mp(num,i) );
						++ans;
					}
				}
			}
		}
		printf("Case #%d: %d\n", T, ans);
	}
	return 0;
}