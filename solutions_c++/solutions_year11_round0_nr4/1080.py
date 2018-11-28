#include <iostream>
#include <vector>
using namespace std;

int A[2000];
double F[2000];

int main() {
  F[0] = F[1] = 0;
  double s = 0;
  for (int i = 2; i <= 1000; ++i) {
    double n = i;
    F[i] = 1 + 2.0*s/(n-1);
    s += F[i];
  }

  int T, N = 1, n;
  cin >> T;
  while (T-- && cin >> n) {
    for (int i = 0; i < n; ++i)
      cin >> A[i], --A[i];

    double ans = 0;
    vector<int> C(n, 0);
    for (int i = 0; i < n; ++i) {
      int sz = 0;
      for (int k = i; !C[k]; k = A[k])
        ++sz, C[k] = 1;

      if (sz > 1)
        ans += 1 + F[sz];
    }
    
    cout.setf(ios::fixed);
    cout.precision(6);
    cout << "Case #" << N++ << ": " << ans << endl;
  }
}
