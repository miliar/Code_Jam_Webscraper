#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define For(i,a,b) for (int i = (a),_b = (b); i <= _b; i++)
#define Ford(i,a,b) for (int i = (a),_b = (b); i >= _b; --i)
#define Rep(i,n) for (int i = (0),_n = (n); i < _n; ++i)
#define Repd(i,n) for (int i = ((n)-1); i >= 0; --i)

#define SCAN(t,x) scanf("%" #t,&(x))

#define Fill(a,c) memset(&a, c, sizeof(a))

int N;

inline int idx(int i) {
  return i%N;
}

int main() {
  int T;
  int R, k, i, j, total, tr;
  int v[1234];
  scanf("%d",&T);
  For(t,1,T) {
    scanf("%d%d%d", &R, &k, &N);
    for (i=0; i<N; i++) scanf("%d", &v[i]);
    total = i = j = 0;
    Rep(r,R) {
      i = j = i%N;
      tr = 0;
      while (tr + v[idx(i)] <= k && (i < j+N)) {
        tr += v[idx(i++)];
      }
      //      printf("i = %d, tr = %d, j = %d\n",i,tr,j);
      total += tr;
    }
    printf("Case #%d: %d\n", t, total);
  }
  return 0;
}
