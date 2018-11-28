#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
const decimal EPS = 1e-8;

int memo[9][1000];

int nCases;

static inline int reduce(int n, int b){
  return n < b ? n*n : reduce(n/b, b) + (n%b)*(n%b);
}

static inline bool solve(int n, int b){
  int *m = memo[b-2];
  if(m[n] != -1){
    return m[n] == 1;
  }
  int nx = reduce(n, b);
  m[n] = nx;
  bool ret = true;
  if(nx != 1){
    ret = solve(nx, b);
  }
  if(ret){
    m[n] = 1;
  }
  return ret;
}

int ans[1 << 11];

int main(){
  memset(memo, -1, sizeof(memo));
  memset(ans, -1, sizeof(ans));
  scanf("%d ", &nCases);
  REP(ic, nCases){
    vector<int> a;
    int bitmap = 0;
    REP(i, 16){
      int n;
      char c;
      scanf("%d%c", &n, &c);
      if(n != 2 && n != 4){
        a.push_back(n);
        bitmap |= (1 << n);
      }
      if(c == '\n') break;
    }
    if(ans[bitmap] != -1){
      cout << "Case #" << ic+1 << ": " << ans[bitmap] << endl;
      continue;
    }
    for(int n = 2; ; n++){
      bool ok = true;
      REP(b, a.size()){
        int k = reduce(n, a[b]);
        if(k != 1 && !solve(k, a[b])){
          ok = false;
          break;
        }
      }
      if(ok){
        ans[bitmap] = n;
        cout << "Case #" << ic+1 << ": " << n << endl;
        break;
      }
    }
  }

  return 0;
}

