#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <cmath>
#include <cassert>

using namespace std;
typedef complex<double> P;

string solve(string s)
{
  int n = s.length();

  if (next_permutation(s.begin(), s.end())) {
    return s;
  }

  // not found
  sort(s.begin(), s.end());
  s = "0" + s;
  n = s.length();
  for (int i = 1; i < n; ++i) {
    if (s[i] != '0') {
      swap(s[0], s[i]); break;
    }
  }
  return s;
}

int main(void)
{
  int N; cin >> N;
  for (int i = 0; i < N; ++i) {
    string s; cin >> s;
    cout << "Case #" << (i + 1) << ": " << solve(s) << endl;
  }
    return 0;
}

