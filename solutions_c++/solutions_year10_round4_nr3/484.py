#include<iostream>
using namespace std;

const int maxn = 100+3;

int cases, n, now, ans;
int a[maxn][maxn], b[maxn][maxn];
int x1, x2, y1, y2;

int main()
{
    freopen("C0.in","r",stdin);
    freopen("C1.out","w",stdout);

    cin >> cases;
    for (int p = 1; p <= cases; ++p) {
      cout << "Case #" << p << ": ";
      
      memset(a,0,sizeof(a));
      memset(b,0,sizeof(b));
      ans = 0;
      
      cin >> n;
      for (int i = 1; i <= n; ++i) {
        cin >> x1 >> y1 >> x2 >> y2;
        for (int x = x1; x <= x2; ++x)
          for (int y = y1; y <= y2; ++y)
            a[x][y] = 1;
      }
      
      now = 0;
      for (int i = 1; i <= 100; ++i)
        for (int j = 1; j <= 100; ++j)
          now += a[i][j];
      while (now) {
        ++ans; now = 0;
        for (int i = 1; i <= 100; ++i)
          for (int j = 1; j <= 100; ++j)
            if ((a[i-1][j] == 0)&&(a[i][j-1] == 0))
              b[i][j] = 0;
            else if ((a[i-1][j] == 1)&&(a[i][j-1] == 1)){
              b[i][j] = 1;
            }
            else {
              b[i][j] = a[i][j];
            }

        for (int i = 1; i <= 100; ++i)
          for (int j = 1; j <= 100; ++j) {
            now += b[i][j];
            a[i][j] = b[i][j];
          }
      }
      
      cout << ans;
      cout << endl;
    }

    return 0;
}
