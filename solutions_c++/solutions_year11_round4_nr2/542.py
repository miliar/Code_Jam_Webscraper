#include <iostream> 
#include <vector> 
#include <string> 
#include <math.h> 
#include <algorithm>
#include <map>
#include <set> 

#define sz(x) ((int)x.size()) 
#define all(x) (x).begin(), (x).end() 
#define pb(x) push_back(x) 
#define mp(x, y) make_pair(x, y) 

typedef long long int64; 
using namespace std;

int n, m;
vector<vector<int64> > a, sum, sum1, sum2;

bool check(int64 i, int64 j, int64 k) {
     int64 x = sum1[i + k - 1][j + k - 1];
     if (i > 0)
          x -= sum1[i - 1][j + k - 1];
     if (j > 0)
          x -= sum1[i + k - 1][j - 1];
     if (i > 0 && j > 0)
         x += sum1[i - 1][j - 1];
         
     x -= i * a[i][j];
     x -= (i + k - 1) * a[i + k - 1][j];
     x -= i * a[i][j + k - 1];
     x -= (i + k - 1) * a[i + k - 1][j + k - 1];
     
         
     int64 y = sum2[i + k - 1][j + k - 1];
     if (i > 0)
          y -= sum2[i - 1][j + k - 1];
     if (j > 0)
          y -= sum2[i + k - 1][j - 1];
     if (i > 0 && j > 0)
         y += sum2[i - 1][j - 1];
         
     
     y -= j * a[i][j];
     y -= j * a[i + k - 1][j];
     y -= (j + k - 1) * a[i][j + k - 1];
     y -= (j + k - 1) * a[i + k - 1][j + k - 1];
     
     
     int64 w = sum[i + k - 1][j + k - 1];
     if (i > 0)
          w -= sum[i - 1][j + k - 1];
     if (j > 0)
          w -= sum[i + k - 1][j - 1];
     if (i > 0 && j > 0)
         w += sum[i - 1][j - 1];
     
     
     w -= a[i][j];
     w -= a[i + k - 1][j];
     w -= a[i][j + k - 1];
     w -= a[i + k - 1][j + k - 1];
     
     
     int64 x_ok = 2 * i + k - 1;
     int64 y_ok = 2 * j + k - 1;
     
     // cout << i << " " << j << " " << k << " " << x << " " << y << " " << w << endl;
     
     if (2 * x == w * x_ok && 2 * y == w * y_ok)
          return true;
     return false;

}

bool ok(int64 k) {
    for (int64 i = 0; i + k - 1 < n; ++i)
        for (int64 j = 0; j + k - 1 < m; ++j)
             if (check(i, j, k))
                 return true;
    return false;     
}

void solve() {
     int64 d;
     cin >> n >> m >> d;
     a.assign(n, vector<int64> (m, 0));
     for (int64 i = 0; i < n; ++i) {
         string s;
         cin >> s;
         for (int64 j = 0; j < m; ++j)
             a[i][j] = (int64)(s[j] - '0');
     }
     for (int64 i = 0; i < n; ++i)
         for (int64 j = 0; j < m; ++j)
             a[i][j] += d;
             
     sum.assign(n, vector<int64> (m, 0));
     sum[0][0] = a[0][0];
     for (int64 i = 1; i < n; ++i)
         sum[i][0] = sum[i - 1][0] + a[i][0];
     for (int64 j = 1; j < m; ++j)
         sum[0][j] = sum[0][j - 1] + a[0][j];
     for (int64 i = 1; i < n; ++i)
         for (int64 j = 1; j < m; ++j)
             sum[i][j] = a[i][j] + sum[i - 1][j] - sum[i - 1][j - 1] + sum[i][j - 1];
     
     sum1.assign(n, vector<int64> (m, 0));
     for (int64 i = 1; i < n; ++i)
         sum1[i][0] = sum1[i - 1][0] + i * a[i][0];
     for (int64 j = 1; j < m; ++j)
         sum1[0][j] = sum1[0][j - 1] + 0 * a[0][j];
     for (int64 i = 1; i < n; ++i)
         for (int64 j = 1; j < m; ++j)
             sum1[i][j] = i * a[i][j] + sum1[i - 1][j] - sum1[i - 1][j - 1] + sum1[i][j - 1];
     
     sum2.assign(n, vector<int64> (m, 0));
     for (int64 i = 1; i < n; ++i)
         sum2[i][0] = sum2[i - 1][0] + 0 * a[i][0];
     for (int64 j = 1; j < m; ++j)
         sum2[0][j] =  sum2[0][j - 1] + j * a[0][j];
     for (int64 i = 1; i < n; ++i)
         for (int64 j = 1; j < m; ++j)
             sum2[i][j] = j * a[i][j] + sum2[i - 1][j] - sum2[i - 1][j - 1] + sum2[i][j - 1];
     
     int64 left = 3;
     int64 right = min(n, m);
     int64 ans = 0;
     for (int64 k = min(n, m); k >= 3; --k) {
                   if (ok(k)) {
                       ans = k;
                       break; 
                   }
              }
     if (ans == 0)
         cout << "IMPOSSIBLE" << endl;
     else
         cout << ans << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        cout << "Case #" << test + 1 << ": ";
        solve();
    }
    
    int x;
    cin >> x;
    return 0;
}
