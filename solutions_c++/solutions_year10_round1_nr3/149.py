#include <iostream>
using namespace std;

#define PHI 1.6180339887

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    long long A1, A2, B1, B2;
    cin >> A1 >> A2 >> B1 >> B2;

    long long res = 0;
    for(long long i = A1; i <= A2; i++) {
      long long lb = (long long)(i / PHI);
      long long ub = (long long)(i * PHI) + 1;
      res += max(0LL, min(B2, lb) - B1 + 1);
      res += max(0LL, B2 - max(B1, ub) + 1);
    }

    printf("Case #%d: %lld\n", c, res);
  }
  return 0;
}
