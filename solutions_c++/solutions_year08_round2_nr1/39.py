/* Peter Zielinski, Jagiellonian University, Poland */

#include <cstdio>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <deque>
#include <utility>
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long ll;

vector<int> iks, igrek;

int ile[100000][3][3];

void testcase() {
	iks.clear(); igrek.clear();
	ll n, A, B, C, D, x0, y0, M;
	scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
	iks.PB(x0); igrek.PB(y0);
	FOR(i,0,n-1) {
		x0 = (A*x0 + B)%M;
		y0 = (C*y0 + D)%M;
		iks.PB(x0);
		igrek.PB(y0);
	}
	FOR(i,0,n) FOR(j,0,3) FOR(k,0,3) ile[i][j][k] = 0;
	++ile[0][iks[0]%3][igrek[0]%3];
	FOR(i,1,n) {
		FOR(j,0,3) FOR(k,0,3) ile[i][j][k] = ile[i-1][j][k];
		++ile[i][iks[i]%3][igrek[i]%3];
	}
	ll res = 0;
	FOR(i,2,n)
			FOR(a,0,3) FOR(b,0,3) FOR(c,0,3) FOR(d,0,3) if( ((ll)a+c+iks[i])%3 == 0 && ((ll)b+d+igrek[i])%3 == 0) {
			if(a == c && b == d) res += (ll)ile[i-1][a][b]*(ile[i-1][c][d]-1);
			else res += (ll)ile[i-1][a][b]*ile[i-1][c][d];
		}
	res /= 2;
	printf("%lld", res);
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,0,t) {
	printf("Case #%d: ", i+1);
	testcase();
	printf("\n");
  }
  return 0;
}
