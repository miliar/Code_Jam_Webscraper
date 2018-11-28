#include <iostream>
#include <set>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    unsigned long A, B;
    cin >> A >> B;
    unsigned long count = 0;
    for (unsigned long n = A; n < B; ++n) {
      set<unsigned long> ms;
      unsigned long x = 1;
      while (x <= n) x *= 10;
      unsigned long y = 10;
      while (y < n) {
        unsigned long n_head = n - (n%y);
        unsigned long n_tail = (x/y) * (n % y);
        unsigned long m = n_tail + n_head/y;
        if ((n < m) && (m <= B)) {
          ms.insert(m);
        }
        y *= 10;
      }
      count += ms.size();
    }
    cout << "Case #" << t << ": " << count << '\n';
  }
  return 0;
}
