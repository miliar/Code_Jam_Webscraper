#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int tc, A, B, ans;
set <pair<int,int> > S;

int main() {
  scanf("%d ",&tc);
  for (int TC = 1; TC <= tc; TC++) {
    scanf("%d %d ",&A, &B);
    if (B < 10) {
      printf("Case #%d: 0\n", TC);
      continue;
    }
    S.clear();
    ans = 0;
    int maska = 10;
    while (maska <= A) maska *= 10;
    for (int i = 10; i < maska; i *= 10) {
      int maskb = maska / i;
      for (int j = A / i; j <= B/i; j++) {
        for (int k = B / maskb; k >= A / maskb; k--) {
          int n = j * i + k;
          int m = k * maskb + j;
          if (A <= n && n < m && m <= B) {
            //ans++;
            S.insert(make_pair(n,m));
            //printf ("%d %d\n",n,m);
          }
        }
      }
    }
    printf("Case #%d: %d\n", TC, S.size());
  }
  return 0;
}
