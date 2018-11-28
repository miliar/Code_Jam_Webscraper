#include<iostream>
using namespace std;

const int maxn = 50+3;

int cases;
int n, m, z;

string a[maxn];
bool red, blue, p1, p2, p3, p4;

int main()
{
    freopen("A1.in","r",stdin);
    freopen("A.out","w",stdout);
    
    cin >> cases;
    for (int q = 1; q <= cases; ++q) {
      cout << "Case #" << q << ": ";
      cin >> n >> m;
      for (int i = 0; i < n; ++i)
        cin >> a[i];
      
      for (int i = 0; i < n; ++i) {
        z = n-1;
        for (int j = n-1; j >= 0; --j)
          if (a[i][j] != '.') {
            a[i][z] = a[i][j];
            if (j < z) a[i][j] = '.';
            z = z-1;
          }
      }
      
      red = false; blue = false;
      
      for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) if (a[i][j] != '.'){

          p1 = true;
          for (int k = 1; k < m; ++k) {
            if ((j+k >= n)||(a[i][j+k] != a[i][j])) {
              p1 = false; break;
            }
          }
          
          p2 = true;
          for (int k = 1; k < m; ++k) {
            if ((i+k >= n)||(a[i+k][j] != a[i][j])) {
              p2 = false; break;
            }
          }
          
          p3 = true;
          for (int k = 1; k < m; ++k) {
            if ((i+k >= n)||(j+k >= n)||(a[i+k][j+k] != a[i][j])) {
              p3 = false; break;
            }
          }
          
          p4 = true;
          for (int k = 1; k < m; ++k) {
            if ((i+k >= n)||(j-k < 0)||(a[i+k][j-k] != a[i][j])) {
              p4 = false; break;
            }
          }

          if (a[i][j] == 'B')
            blue |= p1|p2|p3|p4;
          else
            red  |= p1|p2|p3|p4;
        }
      
      if (blue&red) cout << "Both";
      else if (blue) cout << "Blue";
      else if (red) cout << "Red";
      else cout << "Neither";
      
      cout << endl;
    }
    return 0;
}
