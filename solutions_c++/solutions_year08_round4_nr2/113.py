#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cassert>
using namespace std;

#define VV vector
#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND = 0;

#define DB(x) { if (COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

set <ll> TMP;
map <ll, int> X;
map <ll, int> Y;
vector <ll> RES;

int main(int argc, char **argv) {
	COND = argc >= 2 && argv[1][0] == 'q';
	int C; cin >> C;
	FOR (my, 1, C) {
	  ll N, M; ll A;
	  cin >> N >> M >> A;
	  
	  ll x1 = -1, y1 = -1, x2 = -1, y2 = -1;

	  TMP.clear(); X.clear(); Y.clear();
	  FOR (a, 0, N)
	  FOR (b, 0, M) {
	    ll tmp = (ll) a * b;
	    TMP.insert(tmp);
	    X[tmp] = a;
	    Y[tmp] = b;
	  }
	  
	  //a * b - a2 * b2 == A
	  //a * b == A + a2 * b2


	  FOR (a2, 0, N)
	  FOR (b2, 0, M) {
	    ll tmp = A + (ll) a2 * b2;
	    if (TMP.count(tmp)) {
	      x1 = a2; y2 = b2;
	      
	      x2 = X[tmp];
	      y1 = Y[tmp];

	      goto end;
	    }
	  }
	end:;
	  
	  
	  printf("Case #%d:", my);
	  if (x1 == -1) printf(" IMPOSSIBLE\n");
	  else {
	    assert(abs(x1 * y2 - x2 * y1) == A);
	    printf(" %d %d %lld %lld %lld %lld\n", 0, 0, x1, y1, x2, y2);	  
	  }
	}


	return 0;
}
