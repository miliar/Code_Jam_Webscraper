#include <iostream>
#include <vector>

#define rep(i, n) for(int i = 0; i < n; i++)

using namespace std;

vector<string> f;

vector<string> convert(vector<string> g, char c) {
  rep(i, 4) {
    rep(j, 4) {
      if(g[i][j] == c || g[i][j] == 'T') {
        g[i][j] = 'o';
      }
      else {
        g[i][j] = '.';
      }
    }
  }

  return g;
}

bool win(vector<string> g) {

  bool ok;

  rep(i, 4) {
    if(g[i] == "oooo") return true;
  }
  rep(j, 4) {
    ok = true;
    rep(i, 4) {
      if(g[i][j] != 'o') ok = false;
    }
    if(ok) return true;
  }

  ok = true;
  rep(k, 4) {
    if(g[k][k] != 'o') ok = false;
  }
  if(ok) return true;

  ok = true;
  rep(k, 4) {
    if(g[k][3-k] != 'o') ok = false;
  }
  if(ok) return true;

  return false;
}

int solve() {
  if(win(convert(f, 'X'))) return 0;
  if(win(convert(f, 'O'))) return 1;

  int cnt = 0;
  rep(i, 4) {
    rep(j, 4) {
      if(f[i][j] != '.') cnt++;
    }
  }

  return cnt == 16 ? 2 : 3;
}

int main() {

  int T;
  cin >> T;

  string ans[4] = {
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
  };

  rep(t, T) {

    f = vector<string>(4);
    rep(i, 4) {
      cin >> f[i];
    }
    
    cout << "Case #" << (t + 1) << ": " << ans[solve()] << endl;
  }

  return 0;
}
