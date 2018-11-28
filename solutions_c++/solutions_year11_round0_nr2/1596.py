#include <iostream>
#include <vector>

using namespace std;

void solve() {
  string str;

  char op[256][256] = {{0}};
  char co[256][256] = {{0}};

  int C;
  cin >> C;
  for (int i = 0; i < C; ++i) {
    cin >> str;
    int e1 = str[0];
    int e2 = str[1];
    co[e1][e2] = co[e2][e1] = str[2];
  }

  int D;
  cin >> D;
  for (int i = 0; i < D; ++i) {
    cin >> str;
    int e1 = str[0];
    int e2 = str[1];
    op[e1][e2] = op[e2][e1] = 1;
  }

  int n;
  cin >> n >> str;

  vector<char> ans(n);
  int p = 0;
  for (int i = 0; i < str.size(); ++i) {
    if (p == 0) {
      ans[p++] = str[i];
      continue;
    }

    char comb = co[ ans[p - 1] ][ str[i] ];
    if (comb != 0) {
      ans[p - 1] = comb;
      continue;
    } else {
      for (int j = 0; j < p; ++j)
        if (op[ ans[j] ][ str[i] ]) {
          p = 0;
          break;
        }

      if (p != 0)
        ans[p++] = str[i];
    }
  }

  cout << "[";
  for (int i = 0; i < p; ++i) {
    if (i != p - 1)
      cout << ans[i] << ", ";
    else
      cout << ans[i];
  }
  
  cout  << "]\n";
}

int main() {
  int tests;
  cin >> tests;

  for (int t = 1; t <= tests; ++t) {
    cout << "Case #" << t << ": ";
    solve();
  }

  return 0;
}

