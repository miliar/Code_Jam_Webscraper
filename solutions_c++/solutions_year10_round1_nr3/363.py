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

// arya =1; 1 = arya wins

int play(int who, int A, int B) {
  int k = 0;
  int a, b;
  if (A <= 0 || B <= 0)
    return who;
  //  printf("A = %d, B = %d\n", A, B);
  for (a = A - (A/B)*B; a < A; a+=B) {
    if (play(!who,a,B) == who) {
      return who;
    }
  }
  for (b = B - (B/A)*A; b < B; b+=A) {
    if (play(!who,A,b) == who) {
      return who;
    }
  }
  return !who;
}

int bran(int A, int B) {
  int k = 0;
  int a, b;
  while (++k) {
    a = A - k*B;
    b = B - k*A;
    if (a <= 0 && b <= 0)
      break;
    //    if (a > 0 && arya(a,B))
      return 0;
      //    if (b > 0 && arya(A,b))
      return 0;
  }
  return 1;
}


int main() {
  int T;
  int A1, A2, B1, B2;
  int ia, ib;
  int x, r;
  scanf("%d",&T);
  For(t,1,T) {
    scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
    x = 0;
    for (ia = A1; ia <= A2; ia++)
      for (ib = B1; ib <= B2; ib++) {
        r = play(1,ia,ib);
//        if (r)
//          printf("%d, %d -> %d\n", ia, ib, r);
        x += r;
      }
    printf("Case #%d: %d\n",t,x);
  }
  return 0;
}
