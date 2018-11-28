#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

bool cc(char &ac, char &c) {
  return ac == c || ac == 'T';
}


bool rows(vector<string> &a, char &p) {
  bool r = false;
  int size = a.size();
  for (int i = 0; i < size; ++i) {
    bool rr = true;
    for (int j = 0; j < size; ++j) {
      if (!cc(a[i][j], p)) {
        rr = false;
        break;
      }
    }
    r = r || rr;
  }
  return r;
}


bool cols(vector<string> &a, char &p) {
  bool r = false;
  int size = a.size();
  for (int i = 0; i < size; ++i) {
    bool rr = true;
    for (int j = 0; j < size; ++j) {
      if (!cc(a[j][i], p)) {
        rr = false;
        break;
      }
    }
    r = r || rr;
  }
  return r;
}


bool diags(vector<string> &a, char &p) {
  bool r1 = cc(a[0][0], p) && cc(a[1][1], p) &&
    cc(a[2][2], p) && cc(a[3][3], p);
  bool r2 = cc(a[0][3], p) && cc(a[1][2], p) &&
    cc(a[2][1], p) && cc(a[3][0], p);
  return r1 || r2;
}

bool won(vector<string> &a, char p) {
  return rows(a, p) || cols(a, p) || diags(a, p);
}

bool complete(vector<string> &a) {
  for (int i = 0; i < a.size(); ++i) {
    for (int j = 0; j < a.size(); ++j) {
      if (a[i][j] == '.') return false;
    }
  }
  return true;
}

void solve(vector<string> &a, int tc) {
  bool xwon = won(a, 'X');
  bool owon = won(a, 'O');

  if (xwon)
    printf("Case #%d: X won\n", tc);
  else if (owon)
    printf("Case #%d: O won\n", tc);
  else if (!complete(a))
    printf("Case #%d: Game has not completed\n", tc);
  else
    printf("Case #%d: Draw\n", tc);
}


int main() {
  int TC;
  cin >> TC;
  for (int tc = 1; tc <=TC; ++tc) {
    // read input
    vector<string> a(4,"");
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        char c;
        cin >> c;
        a[i].push_back(c);
      }
    }
    solve(a, tc);
  }
  return 0;
}
