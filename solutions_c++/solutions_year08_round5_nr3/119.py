#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define VI vector<int>
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 12;

string s;
char b[maxn][maxn];
int d[maxn][1 << maxn];
int n,m;

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, k, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> m >> n;
      memset(b,0,sizeof(b));
      for (i = 0; i < m; i++) {
         cin >> s;
         for (j = 0; j < n; j++) b[i][j] = s[j];
      }
      memset(d,0,sizeof(d));
      int ans = 0;
      for (i = 0; i < m; i++)
         for (j = 0; j < (1 << n); j++)
            for (k = 0; k < (1 << n); k++) {
               int ok = 1, addon = 0;
               for (int sc = 0; sc < n; sc++) 
                  if (k & (1 << sc)) {
                     addon++;
                     if (b[i][sc] != '.') {ok = 0; break;}
                     if (sc > 0 && (j & (1 << (sc-1))))  {ok = 0; break;}
                     if (sc < n-1 && (j & (1 << (sc+1))))  {ok = 0; break;}
                     if (sc < n-1 && (k & (1 << (sc+1))))  {ok = 0; break;}
                  }
               if (ok) {
                  d[i+1][k] = max(d[i+1][k], d[i][j] + addon);
                  if (d[i+1][k] > ans) ans = d[i+1][k];
               }   
            }
            
      cout << "Case #" << sc << ": ";
      cout << ans;
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}