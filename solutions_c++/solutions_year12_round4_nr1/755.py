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

void solve(int casenum) {
  dprintf("================================================================================% 3d\n", casenum);
  int N; cin >> N;
  int d[N], l[N]; loop(i,N) cin >> d[i] >> l[i];
  int D; cin >> D;

  int R[N]; loop(i,N) R[i] = 0;
  R[0] = d[0];
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j) {
      if (d[j] > d[i] + R[i]) break;
      R[j] = max(R[j], min(l[j], d[j] - d[i]));
    }
  bool possible = false;
  loop(i,N)
    if (d[i] + R[i] >= D) {
      possible = true;
      break;
    }

  
   if (possible)
    printf("Case #%d: YES\n", casenum);
  else
    printf("Case #%d: NO\n", casenum);


  // int i = 0, L = d[0];
  // bool finished = false;
  // while (i < N && !finished) {
  //   int j, j_next = -1;
  //   dprintf("Vine (%d,%d,%d)\n", i, d[i], L);
  //   for (j = i+1; j < N; ++j) {
  //     if (d[j] > d[i] + L) break;
  //     dprintf("  -> (%d,%d,%d)\n", j, d[j], l[j]);
  //     //if (l[j] >= d[j] - d[i]) {
  //       dprintf("    (yes)\n");
  //       j_next = j;
  //       //}
  //   }
  //   if (j_next == -1) {
  //     finished = true;
  //     break;
  //   }
  //   L = min(l[j_next], d[j_next] - d[i]);
  //   i = j_next;
  //   dprintf("-> (%d/%d,%d)\n", i, d[i], L);
  // }

  //  if (D > d[i] + L)
    // printf("Case #%d: NO\n", casenum);
  // else
  //   printf("Case #%d: YES\n", casenum);
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}
