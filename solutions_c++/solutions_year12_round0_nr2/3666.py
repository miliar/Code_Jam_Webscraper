#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int S;
int P;
vector<int> Ti;

int solve() {
  int res = 0;
  for (auto s : Ti) {
    int d = s / 3;
    if (d >= P || (d==(P-1) && ((s%3) > 0))) {
      ++res;
      continue;
    }
    if (S <= 0) {
      continue;
    }
    if (s >= (P-1)*3-1 && d > 0) {
      --S;
      ++res;
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; ++tc) {
    Ti.clear();
    cin >> N;
    cin >> S;
    cin >> P;
    for (int i=0; i<N; ++i) {
      int t;
      cin >> t;
      Ti.push_back(t);
    }
    cout << "Case #" << tc << ": " << solve() << endl;
  }
}
