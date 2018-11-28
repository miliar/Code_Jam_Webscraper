// CPPFLAGS=-std=gnu++0x -W -Wall -g -O2
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
template<class T> bool in(T e, const set<T>& s) { return s.find(e) != s.end(); }

int B[1<<9][1<<9]; int R, C;
int UL[1<<9][1<<9]; // UL[i][j] is sum of B[0..i)[0..j)
int U[1<<9][1<<9];  // U[i][j] is sum of B[0..i)[j]
int L[1<<9][1<<9];  // L[i][j] is sum of B[i][0..j)

int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    int D; if (scanf("%d %d %d",&R,&C,&D)!=3) return 1;
    int i, j, k;
    for (i=0;i<R;++i) for (j=0;j<C;++j) {
      char c; if (scanf(" %c",&c)!=1) return 2;
      B[i][j] = c - '0';
    }
    UL[0][0]=0;
    for (i=1;i<=R;++i) UL[i][0] = 0;
    for (j=1;j<=C;++j) UL[0][j] = 0;
    for (i=1;i<=R;++i) for (j=1;j<=C;++j)
      UL[i][j] = UL[i-1][j] + UL[i][j-1] - UL[i-1][j-1] + B[i-1][j-1];
    for (j=0;j<C;++j) U[0][j] = 0;
    for (i=1;i<=R;++i) for (j=0;j<C;++j) U[i][j] = U[i-1][j] + B[i-1][j];
    for (i=0;i<R;++i) L[i][0] = 0;
    for (i=0;i<R;++i) for (j=1;j<=C;++j) L[i][j] = L[i][j-1] + B[i][j-1];
    for (k = min(R, C); k >= 3; --k) {
      int ii, jj;
      for (ii = 0; ii + k <= R; ++ii) {
        for (jj = 0; jj + k <= C; ++jj) {
          int a, b, c, d;
          a = UL[ii+k/2][jj+k/2]
              - UL[ii][jj+k/2] - UL[ii+k/2][jj]
              + UL[ii][jj];
          b = UL[ii+k][jj+k/2]
              - UL[ii+k-k/2][jj+k/2] - UL[ii+k][jj]
              + UL[ii+k-k/2][jj];
          c = UL[ii+k/2][jj+k]
              - UL[ii][jj+k] - UL[ii+k/2][jj+k-k/2]
              + UL[ii][jj+k-k/2];
          d = UL[ii+k][jj+k]
              - UL[ii+k-k/2][jj+k] - UL[ii+k][jj+k-k/2]
              + UL[ii+k-k/2][jj+k-k/2];
          a -= B[ii][jj];
          b -= B[ii+k-1][jj];
          c -= B[ii][jj+k-1];
          d -= B[ii+k-1][jj+k-1];
//printf("* k=%d ii=%d jj=%d a=%d d=%d b=%d c=%d\n",k,ii,jj,a,d,b,c);
          a = 2*a; b = 2*b; c = 2*c; d = 2*d;
          if (k&1) {
            a += U[ii+k/2][jj+k/2]-U[ii][jj+k/2];
            c += U[ii+k/2][jj+k/2]-U[ii][jj+k/2];
            b += U[ii+k][jj+k/2]-U[ii+k-k/2][jj+k/2];
            d += U[ii+k][jj+k/2]-U[ii+k-k/2][jj+k/2];
            a += L[ii+k/2][jj+k/2]-L[ii+k/2][jj];
            b += L[ii+k/2][jj+k/2]-L[ii+k/2][jj];
            c += L[ii+k/2][jj+k]-L[ii+k/2][jj+k-k/2];
            d += L[ii+k/2][jj+k]-L[ii+k/2][jj+k-k/2];
          }
//printf("k=%d ii=%d jj=%d a=%d d=%d b=%d c=%d\n",k,ii,jj,a,d,b,c);
          if (a==d && b==c) goto yes;
        }
      }
    }
    printf("IMPOSSIBLE\n");
    continue; // next test
yes:
    printf("%d\n",k);
  }
}
