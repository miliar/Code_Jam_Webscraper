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

int main() {
  int T;
  unsigned long K, mask;
  int i, N;
  scanf("%d",&T);
  For(t,1,T) {
    scanf("%d%lu", &N, &K);
    mask = 1;
    for (i=0;i<N;i++) {
      if (! ((mask<<i) & K))
        break;
    }
    printf("Case #%d: %s\n", t, (i==N) ? "ON" : "OFF");
  }
  return 0;
}
