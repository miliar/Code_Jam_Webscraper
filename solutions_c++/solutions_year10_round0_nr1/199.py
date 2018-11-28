#include <iostream>
#include <inttypes.h>

using namespace std;

int main() {
  uint64_t N, k, p; cin >> N;

  for (int i=0; i<N; ++i) {
    cin >> k >> p;
    cout << "Case #" << (i+1) << ": ";
    bool ok = true;
    for (int j=0; j<k; ++j)
      ok = ok && ((p >> j) & 1ULL);
    cout << (ok ? "ON\n" : "OFF\n");
  }
}
