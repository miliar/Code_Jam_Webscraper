#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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
#include <cassert>
#include <queue>
#include <cstring>
using namespace std;

#define loop(i,n) for (int i = 0; i < (int)(n); ++i)
#define loopa(i,a,b) for (int i = (a); i <= (b); ++i)
#define Bounded(x,a,b) ((a) <= (x) && (x) <= (b))
#define db(x) #x << " = " << x
#define pdb(x) printf("#x = %d\n",x);
#define All(x) x.begin(),x.end()
#define sz(x) x.size()
typedef vector<int> Vi;
typedef pair<int,int> Pii;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;
typedef long long int Int;
typedef vector<Int> VInt;
typedef long long int ll;
typedef long double ld;
#define Car(x) (x).first
#define Cdr(x) (x).second
#define Caar(x) (x).first.first
#define Cdar(x) (x).first.second
#define Cadr(x) (x).second.first
#define Cddr(x) (x).second.second

const bool debug = false;
#define dprintf debug && printf

ll d2(ll* x, ll* y, int i, int j) {
  ll dx = x[i] - x[j], dy = y[i] - y[j];
  return dx*dx + dy*dy;
}

void solve(int casenum) {
  dprintf("================================================================================% 3d\n", casenum);

  int N, W, L; cin >> N >> W >> L;
  ll r[N]; loop(i,N) cin >> r[i];

  ll X[N], Y[N];

  X[0] = 0, Y[0] = 0;
  int count = 1;

  for (; count < N; ++count) {

    bool success = false;

    dprintf("Placing %d\n", count);
    for (int plan = 0; plan < (1<<count); ++plan) {
      ll x = 0, y = 0;
      loop(i,count) {
        if ((plan>>i)%2) x = max(x, X[i] + r[i] + r[count]);
        else y = max(y, Y[i] + r[i] + r[count]);
      }
      dprintf("  - plan %d -> (%lld,%lld)\n", plan, x, y);
      if (x <= W && y <= L) {
        X[count] = x, Y[count] = y;
        dprintf("Put circle %d at (%lld,%lld)\n", count, x, y);
        success = true;
        break;
      }
    }

    if (!success) dprintf("FAILED\n");
    
  }

  printf("Case #%d:", casenum);
  loop(i,N) printf(" %lld %lld", X[i], Y[i]);
  printf("\n");
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}
