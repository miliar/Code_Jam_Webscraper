#include <iostream>
#include <vector>
using namespace std;

// --------------------------------------------------------------
// brute force to check for correctness
// --------------------------------------------------------------
const uint32_t one = 1;
inline void set_bit(uint32_t* n, int b, bool v) {
  uint32_t one = 1;
  if (v) {
    *n |= one << b;
  } else {
    *n &= ~(one << b);
  }
}

inline bool get_bit(uint32_t n, int b) {
  return n & (one << b);
}

bool run_test_simple(int n, int k) {
  uint32_t states = 0x0;
  uint32_t power = 0x1;  // power from socket

  for (int i = 0; i < k; ++i) {
    // snap fingers to switch states
    for (int s = 0; s < n; ++s) {
      if (get_bit(power, s)) {
        set_bit(&states, s, !get_bit(states, s));
      }
    }

    // switch who has power
    for (int s = 1; s < n; ++s) {
      set_bit(&power, s, get_bit(power, s-1) && get_bit(states, s-1));
    }
  }

  return get_bit(power, n-1) && get_bit(states, n-1);
}

// --------------------------------------------------------------
// fast computation
// --------------------------------------------------------------

bool run_test(int n, int k) {
  uint32_t pow = one << n;
  return (k % pow) == (pow - 1);
}

void unit_test() {
  for (int n = 1; n < 10; ++n) {
    cerr << "n = " << n << endl;
    for (int k = 0; k < 5000; ++k) {
      if (run_test(n, k) != run_test_simple(n, k)) {
        cerr << "BROKEN" << endl;
        exit (1);
      }
    }
  }
  exit(0);
}


int main() {
  // unit_test();

  int t = -1;
  if (!(cin >> t) || t <= 0) {
    return 1;
  }
  int n, k;
  for (int cnum = 1; cnum <= t && cin >> n >> k; ++cnum) {
    cout << "Case #"  << cnum << ": ";
    bool res = run_test(n, k);
    cout << (res ? "ON" : "OFF") << endl;
  }
  return 0;
}
