#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
using namespace std;

int N, A, B;

int n_pairs(int i) {
  ostringstream fmt;
  fmt << i;
  string s = fmt.str();
  int r = 0;
  vector<bool> u(B, false);
  for (int j = 0; j < s.length(); ++j) {
    istringstream is(s);
    int p;
    is >> p;
    rotate(s.begin(), s.begin() + 1, s.end());
    if (p > i && p <= B && !u[p]) {
      r += 1;
      u[p] = true;
    }
  }
  return r;
}

int main(int argc, char* argv[]) {
  cin >> N;
  for (int t = 1; t <= N; ++t) {
    cin >> A >> B;
    int r = 0;
    for (int i = A; i <= B; ++i) {
      r += n_pairs(i);
    }
    cout << "Case #" << t << ": " << r << endl;
  }
}