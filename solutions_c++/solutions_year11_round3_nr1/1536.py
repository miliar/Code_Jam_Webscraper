#include <cstdio>
#include <iostream>
#include <cmath>
#include <stack>
#include <vector>
#include <algorithm>
#include <string>

typedef long long ll;
using namespace std;

int main () {
  int i = 0, j = 0, k = 0, l = 0, m = 0, n = 0;
  double x = 0, y = 0, z = 0;
  string s;
  char c;
  cin >> i;
  while (i--) {
    cin >> j >> k;
    int a[100] = {0}, b[100] = {0};
    char map[100][100];
    for (int l = -1; ++l < j; )
      for (int m = -1; ++m < k; ) {
        cin >> c;
        if (c == '#') a[l]++, b[m]++;
        map[l][m] = c;
      }
    cout << "Case #" << ++m << ":" << endl;
    for (int l = -1; ++l < j; )
      if (a[l] % 2 == 1) goto next;
    for (int m = -1; ++m < k; )
      if (b[m] % 2 == 1) goto next;
    for (int l = -1; ++l < j; )
      for (int m = -1; ++m < k; ) {
        if (l < j - 1 && m < k - 1 && map[l][m] == '#') {
          if (map[l][m + 1] == '#' && map[l + 1][m] == '#' && map[l + 1][m + 1] == '#') {
            map[l][m] = map[l + 1][m + 1] = '/';
            map[l][m + 1] = map[l + 1][m] = '\\';
          } else {
            goto next;
          }
        }
      }

    for (int l = -1; ++l < j; cout << endl)
      for (int m = -1; ++m < k; ) 
        cout << map[l][m];
    goto end;
next:;
    cout << "Impossible" << endl;
end:;
  }

}
