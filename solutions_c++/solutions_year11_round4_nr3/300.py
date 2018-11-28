#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "C"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int gcd(int a, int b) {
  if (!b) {
    return a;
  }
  return gcd(b, a % b);
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  const int MAXN = 1000001;
  vector<bool> is_cons(MAXN, false);
  vector<int> primes;
  is_cons[1] = true;
  for (int i = 2; i < MAXN; ++i) {
    if (!is_cons[i]) {
      primes.push_back(i);
      for (ll j = ll(i) * i; j < MAXN; j += i) {
        is_cons[j] = true;
      }
    }
  }
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int n;
    cin >> n;
    int min_times = 0;
    int max_times = 1;
    for (int i = 2; i <= n; ++i) {
      if (!is_cons[i]) {
        ++min_times;
        ++max_times;
      } else {
        bool p_power = false;
        for (int j = 0; j < primes.size(); ++j) {
          if (i % primes[j] == 0) {
            int i_copy = i;
            while (i_copy > 1 && i_copy % primes[j] == 0) {
              i_copy /= primes[j];
            }
            if (i_copy == 1) {
              p_power = true;
              break;
            }
          }
        }
        if (p_power) {
          ++max_times;
        }
      }
    }
    int res = max_times - min_times;
    if (n == 1) {
      res = 0;
    }
    cout << "Case #" << test_index + 1 << ": " << res << endl;
    cerr << "Case #" << test_index + 1 << ": " << res << endl;
  }
  return 0;
}
