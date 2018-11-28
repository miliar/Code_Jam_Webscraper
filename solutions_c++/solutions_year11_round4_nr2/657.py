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
#define loop1(i,a,b) for (int i = (a); i < (int)(b); ++i)
#define Bounded(x,a,b) ((a) <= (x) && (x) <= (b))
#define db(x) #x << " = " << x
#define pdb(x) printf("#x = %d\n",x);
#define All(x) x.begin(),x.end()
#define sz(x) x.size()
typedef vector<int> Vi;
typedef pair<int,int> Pii;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;

void solve(int casenum) {
  int R, C, D; cin >> R >> C >> D;
  vector<Vi> w(R, Vi(C));
  loop(i,R) {
    string s; cin >> s;
    loop(j,C)
      w[i][j] = D + (s[j]-'0');
  }

  int max_size = 0;

  loop(cr, R) loop(cc, C) loop1(K, 3, 1+min(R, C)) {
    bool debug = cr==0 && cc == 0;

    if (cr+K > R || cc+K > C) continue;
    double comr = cr+0.5*K, comc = cc+0.5*K;

    double mr = 0, mc = 0;
    loop(i,K) loop(j,K) {
      if (i == 0 && j == 0) continue;
      if (i == 0 && j == K-1) continue;
      if (i == K-1 && j == 0) continue;
      if (i == K-1 && j == K-1) continue;
      mr += (comr - (i+cr+0.5)) * (double)w[cr+i][cc+j];
      mc += (comc - (j+cc+0.5)) * (double)w[cr+i][cc+j];
    }
    if (fabs(mr) < 1e-10 && fabs(mc) < 1e-10) {
      // fprintf(stderr, "Found, (%d,%d), k=%d\n", cr, cc, K);
      // loop(i,K) {
      //   loop(j,K)
      //     printf("%c", w[cr+i][cc+j]-D + '0');
      //   printf("\n");
      // }
      if (K > max_size)
        max_size = K;
    }
  }

  if (max_size == 0)
    printf("Case #%d: IMPOSSIBLE\n", casenum);
  else
    printf("Case #%d: %d\n", casenum, max_size);
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}

