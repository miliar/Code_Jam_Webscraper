#include <vector>
#include <string>
#include <iostream>

using namespace std;
int check_string(const string& str, int t) {
  size_t p = str.find_first_of('.');
  if (p != string::npos) {
    return 2;
  }
  if (str == "OOOO" || str == "TOOO" || str == "OTOO" ||
      str == "OOTO" || str == "OOOT") {
    cout << "Case #" << t << ": O won\n";
    return 1;
  }
  if (str == "XXXX" || str == "TXXX" || str == "XTXX" ||
      str == "XXTX" || str == "XXXT") {
    cout << "Case #" << t << ": X won\n";
    return -1;
  }
  return 0;
}

void solve(int t) {
  vector<string> map;
  bool pending = false;
  for (int i = 0; i < 4; ++i) {
    string row;
    cin >> row;
    map.push_back(row);
  }
  // Rows
  for (int r = 0; r < 4; ++r) {
    int w = check_string(map[r], t);
    if (w == 2) { pending = true;
    } else if (w == 1 || w == -1) { return; }
  }
  // Cols
  for (int c = 0; c < 4; ++c) {
    string col = map[0].substr(c, 1u) + map[1].substr(c, 1u) + map[2].substr(c, 1u) + map[3].substr(c, 1u);
    int w = check_string(col, t);
    if (w == 2) { pending = true; }
    else if (w == 1 || w == -1) { return; }
  }
  // Diag
  string diag;
  int w;
  diag = map[0].substr(0, 1) + map[1].substr(1, 1) + map[2].substr(2, 1) + map[3].substr(3, 1);
  w = check_string(diag, t);
  if (w == 2) { pending = true; }
  else if (w == 1 || w == -1) { return; }

  diag = map[0].substr(3, 1) + map[1].substr(2, 1) + map[2].substr(1, 1) + map[3].substr(0, 1);
  w = check_string(diag, t);
  if (w == 2) { pending = true; }
  else if (w == 1 || w == -1) { return; }

  if (pending) {
    cout << "Case #" << t << ": Game has not completed\n";
  } else {
    cout << "Case #" << t << ": Draw\n";
  }
}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    solve(t + 1);
  }
  return 0;
}
