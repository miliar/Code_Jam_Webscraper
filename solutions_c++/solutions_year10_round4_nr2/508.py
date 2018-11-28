#include<iostream>
using namespace std;

const int maxn = 1024+3;

int n, cases;
int two[11];
int a[maxn];
int f[11][maxn][11];
int g[11][maxn];

int main()
{
    freopen("B1.in","r",stdin);
    freopen("B.out","w",stdout);

    two[0] = 1;
    for (int i = 1; i < 11; ++i) two[i] = two[i-1]*2;

    cin >> cases;
    for (int p = 1; p <= cases; ++p) {
      cout << "Case #" << p << ": ";

      cin >> n;
      for (int i = 1; i <= two[n]; ++i) cin >> a[i];
      for (int i = n-1; i >= 0; --i) {
        for (int j = 1; j <= two[i]; ++j)
          cin >> g[i][j];
      }

      memset(f,60,sizeof(f));
      for (int i = 1; i <= two[n]; ++i)
        for (int j = 0; j <= a[i]; ++j)
          f[n][i][j] = 0;
          
      for (int k = n-1; k >= 0; --k) {
        for (int i = 1; i <= two[k]; ++i) {
          for (int j = k; j >= 0; --j) {
            f[k][i][j] = g[k][i];
            f[k][i][j] += f[k+1][i*2-1][j]+f[k+1][i*2][j];
            f[k][i][j] <?= f[k+1][i*2-1][j+1]+f[k+1][i*2][j+1];
            f[k][i][j] <?= f[k][i][j+1];
          }
        }
      }

      cout << f[0][1][0];

      cout << endl;
    }

    return 0;
}
