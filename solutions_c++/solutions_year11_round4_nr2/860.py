#include <cstdio>
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long double ld;

const int Maxn = 505;

int t, r, c, d, mass[Maxn][Maxn];
char mas[Maxn][Maxn];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> r >> c >> d;
        for (int i = 0; i < r; i++)
           for (int j = 0; j < c; j++)
              cin >> mas[i][j];
        for (int i = 0; i < r; i++)
           for (int j = 0; j < c; j++) mass[i][j] = mas[i][j] - '0';
        int best = 0;
        for (int i = 0; i < r; i++)
           for (int j = 0; j < c; j++)
              for (int siz = 3; i + siz <= r && j + siz <= c; siz++) {
                  
                  if (siz <= best) continue;
                  
                  int i2 = i + siz - 1, j2 = j + siz - 1;
                  int tocon = siz / 2;
                  
                  int col = 0;
                  int m = 0;
                  for (int curj = j + 1; curj < j2; curj++) {
                      col += curj * mass[i][curj];
                      m += mass[i][curj];
                  }
                  for (int curi = i + 1; curi < i2; curi++)
                     for (int curj = j; curj <= j2; curj++) {
                         col += curj * mass[curi][curj];
                         m += mass[curi][curj];
                     }
                  for (int curj = j + 1; curj < j2; curj++) {
                      col += curj * mass[i2][curj];
                      m += mass[i2][curj];
                  }
                  
                  if ((j + j2) * m != 2 * col) continue;
                  
                  col = 0;
                  m = 0;
                  for (int curi = i + 1; curi < i2; curi++) {
                      col += curi * mass[curi][j];
                      m += mass[curi][j];
                  }
                  for (int curj = j + 1; curj < j2; curj++)
                     for (int curi = i; curi <= i2; curi++) {
                         col += curi * mass[curi][curj];
                         m += mass[curi][curj];
                     }
                  for (int curi = i + 1; curi < i2; curi++) {
                      col += curi * mass[curi][j2];
                      m += mass[curi][j2];
                  }
                        
                  if ((i + i2) * m == 2 * col) best = siz;
              }
        cout << "Case #" << tc << ": ";
        if (best > 0) cout << best << endl;
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
