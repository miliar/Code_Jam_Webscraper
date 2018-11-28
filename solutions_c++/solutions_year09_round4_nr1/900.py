#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
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
#define rep(i,m,n) for(int i = m; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
const decimal EPS = 1e-8;

int nCases;
int N;
int a[40];

int solve(int x){
  if(x == 1) return 0;
  int ret = 100000;
  void *bk = malloc(sizeof(a));
  memcpy(bk, a, sizeof(a));
  REP(i, x){
    if(a[i] > N-x+1) continue;
    rep(j, i, N-1){
      swap(a[j], a[j+1]);
    }
    ret = min(ret, i + solve(x-1));
    memcpy(a, bk, sizeof(a));
  }
  free(bk);
  return ret;
}

int main(){
  scanf("%d ", &nCases);
  REP(ic, nCases){
    cin >> N;
    REP(i, N){
      int maxj = 0;
      REP(j, N){
        char c;
        cin >> c;
        if(c == '1') maxj = j+1;
      }
      a[i] = maxj;
    }
    int ret = solve(N);

    cout << "Case #" << ic+1 << ": " << ret << endl;
  }

  return 0;
}

