#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 512;
const int mod = 10000;

int d[maxn][maxn];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int i, j, k;
   int t; cin >> t;
   string s; getline(cin, s);
   for (int sc = 0; sc < t; sc++) {
      getline(cin, s);
      int n = s.length();
      string a = "welcome to code jam";
      int m = a.length();
      
      memset(d, 0, sizeof(d));
      d[0][0] = 1;
      for (i = 0; i < n; i++) {
         for (j = 0; j < m; j++) {
            d[i+1][j] = (d[i+1][j] + d[i][j]) % mod;
            if (s[i] == a[j])
               d[i+1][j+1] = (d[i+1][j+1] + d[i][j]) % mod;
         }
         d[i+1][m] = (d[i+1][m] + d[i][m]) % mod;
      }   
      
      int ans = d[n][m];
      cout << "Case #" << sc+1 << ": ";
      k = 1000;
      for (i = 0; i < 4; i++) {
         cout << ans/k; 
         ans %= k;
         k /= 10;
      }
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}