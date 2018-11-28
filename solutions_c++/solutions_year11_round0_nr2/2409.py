#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;

void Solve() {
  int C, D, N;
  string result;
  vector<string> combine;
  vector<string> opposite;
  string invoke;
  cin >> C;
  for(int i = 0; i < C; ++i) {
    string S;
    cin >> S;
    combine.push_back(S);
  }
  cin >> D;
  for(int i = 0; i < D; ++i) {
    string S;
    cin >> S;
    opposite.push_back(S);
  }
  cin >> N;
  cin >> invoke;
  for(int i = 0; i < N; ++i) {
    result += invoke[i];
    if (result.size() < 2) {
      continue;
    }
    int l = result.size() - 1;
    for(int j = 0; j < C; ++j) {
      if ((result[l] == combine[j][0] && result[l - 1] == combine[j][1]) ||
        (result[l] == combine[j][1] && result[l - 1] == combine[j][0])) {
        string s = "";
        s += combine[j][2];
        result.replace(l - 1, 2, s);
        break;
      }
    }
    for(int j = 0; j < D; ++j) {
      if (result.size() < 2) {
        break;
      }
      int l = result.size() - 1;
      char opp;
      if (result[l] == opposite[j][0]) {
        opp = opposite[j][1];
      } else if (result[l] == opposite[j][1]) {
        opp = opposite[j][0];
      } else {
        continue;
      }
      for(int k = 0; k < l; ++k) {
        if (result[k] == opp) {
          result = "";
          break;
        }
      }
    }
  }
  cout << "[";
  for(int i = 0; i < result.size(); ++i) {
    cout << result[i];
    if (i + 1 < result.size()) {
      cout << ", ";
    }
  }
  cout << "]" << endl;
}

int main() {
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    cout << "Case #" << i + 1 << ": ";
    Solve();
  }
  return 0;
}
