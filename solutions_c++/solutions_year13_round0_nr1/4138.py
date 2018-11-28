#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <iostream>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define sz(a) (int)((a).size())
#define all(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;

vector<string> outcomes = {
  "Game has not completed",
  "X won",
  "O won",
  "Draw"
};

vector<string> m(4);

int check(int x0, int y0, int dx, int dy) {
  int num = 0;
  for (int i = 0; i < 4; ++i) {
    int x = x0 + i * dx;
    int y = y0 + i * dy;
    if (x > 3 || y > 3 || x < 0 || y < 0) return 0;

    if (m[x][y] =='X') num++;
    if (m[x][y] =='O') num--;
    if (m[x][y] =='T') num += 10;
  }

  if (num == 4 || num == 13) return 1;
  if (num == -4 || num == 7) return 2;
  return 0;
}

int main() {
  int t;
  cin >> t;
  for (int q = 1; q <= t; q++) {
    for (int i = 0; i < 4; ++i) {
      cin >> m[i];
    }

    int state = 0;
    for (int i = 0; i < 7; ++i) {
      state |= check(max(0, i - 3), max(0, 3 - i), 1, 0);
      state |= check(max(0, i - 3), max(0, 3 - i), 0, 1);
    }
    state |= check(0, 0, 1, 1);
    state |= check(3, 0, -1, 1);

    if (state == 0 && (m[0] + m[1] + m[2] + m[3]).find(".") == string::npos)
      state = 3;

    cout << "Case #" << q << ": " << outcomes[state] << endl;
  }

  return 0;
}
