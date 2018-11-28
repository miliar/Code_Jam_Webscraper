#include <cstdio>

long long xV [100000];
long long yV [100000];

long long result;
 long long n, A, B, C, D, X, Y, M;

void read() {
  scanf("%Ld %Ld %Ld %Ld %Ld %Ld %Ld %Ld",&n, &A, &B, &C, &D, &X, &Y, &M);
  for (long long c = 0; c < n; c++) {
    xV[c] = X;
    yV[c] = Y;
    X = (A * X + B) % M;
    Y = (C * Y + D) % M;
  }
}

void solve() {
  long long c, d, e;
  result = 0;
  for (c = 0; c < n; c++) {
    for (d = c + 1; d < n; d++) {
      for (e = d + 1; e < n; e++) {
        if (((xV[c] + xV[d] + xV[e])%3) == 0) {
          if (((yV[c] + yV[d] + yV[e])%3) == 0) {
            result++;
          }
        }
      }
    }
  }
}

int main() {
  int numOfTests;
  scanf("%d",&numOfTests);
  for (int c = 1; c <= numOfTests; c++) {
    read();
    solve();
    printf("Case #%d: %Ld\n",c, result);
  }
}
