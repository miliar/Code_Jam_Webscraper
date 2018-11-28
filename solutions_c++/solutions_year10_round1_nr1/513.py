#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
string flipit(string a, int n) {
  int ret = 0;
  for (int x = 0; x <= n; x++) {
    if (a[x] != '.') {
      ret = 1;
      break;
    }
  }
  if (!ret) return a;
  while (a[n] == '.') a = "." + a;
  return a;
}
string stuff2[51];
int winner(int x, int y, int k, int n) {
  int a, b, c, d;
  a = b = c = d = 1;
  for (int z = 0; z < k; z++) {
    if (x + z >= n || stuff2[x+z][y] != stuff2[x][y]) a = 0;
    if (y + z >= n || stuff2[x][y+z] != stuff2[x][y]) b = 0;
    if (x + z >= n || y + z >= n || stuff2[x+z][y+z] != stuff2[x][y]) c = 0;
    if (x + z >= n || y - z < 0 || stuff2[x+z][y-z] != stuff2[x][y]) d = 0;
  }
  return a || b || c || d;
}
string solving() {
  int n, k;
  string stuff[51];
  cin >> n >> k;
  for (int x = 0; x < n; x++) {
    cin >> stuff[x];
    stuff[x] = flipit(stuff[x], n - 1);
  }
  for (int x = 0; x < n; x++) {
    stuff2[x] = "";
    for (int y = 0; y < n; y++) {
      stuff2[x] += stuff[n - y - 1][x];
      int xx = x;
      while (xx && stuff2[xx][y] == '.') {
        stuff2[xx][y] = stuff2[xx - 1][y];
        stuff2[--xx][y] = '.';
      }
    }
  }
  int red = 0, blue = 0;
  for (int x = 0; x < n; x++) {
    // cout << stuff2[x] << endl;
    for (int y = 0; y < n; y++) {
      if (stuff2[x][y] == 'R' && !red && winner(x, y, k, n)) red = 1;
      if (stuff2[x][y] == 'B' && !blue && winner(x, y, k, n)) blue = 1;
    }
  }
  if (red) {
    if (blue) return "Both";
    return "Red";
  }
  if (blue) return "Blue";
  return "Neither";
}
int main() {
  int n;
  cin >> n;
  for (int x = 1; x <= n; x++) cout << "Case #" << x << ": " << solving() << endl;
  return 0;
}

