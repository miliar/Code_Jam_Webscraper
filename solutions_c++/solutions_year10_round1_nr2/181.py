#include <cstdio>
#include <algorithm>

using namespace std;

const int inf = 99999999;

int D, I, M, N;
int d[101][256];
int a[101];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int cs;
  scanf("%d", &cs);
  for (int r = 1; r <= cs; ++r) {
    scanf("%d %d %d %d", &D, &I, &M, &N);
    for (int i = 1; i <= N; ++i)
      scanf("%d", &a[i]);
    
    fill(d[0], d[1], 0);
    fill(d[1], d[N + 1], inf);
    for (int i = 1; i <= N; ++i) {
      for (int j = 0; j <= 255; ++j) {
        d[i][j] = (i - 1) * D + min(abs(j - a[i]), D + I);
        if (i != 1) {
        
          // del
          d[i][j] = min(d[i][j], d[i - 1][j] + D);
        }
        for (int k = 0; k <= 255; ++k) {
          if (abs(k - j) <= M) {
            d[i][j] = min(d[i][j], d[i - 1][k] + min(abs(j - a[i]), D + I));
          }
          if (M == 0) continue;
          int l = abs(k - j);
          int ic = l / M;          
          if (ic * M < l) ic++;
          ic--;
          if (ic > 0) {
            d[i][j] = min(d[i][j], I * ic + d[i - 1][k] + min(abs(j - a[i]), D + I));
          }
        }
      }
    }
    int res = i * D;
    for (int i = 0; i <= 255; ++i)
      res = min(res, d[N][i]);
      
    printf("Case #%d: %d\n", r, res);
  }
  return 0;
}