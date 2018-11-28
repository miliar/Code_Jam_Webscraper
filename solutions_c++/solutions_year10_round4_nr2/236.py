#include "stdio.h"
#include "stdlib.h"
#include "string.h"
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

const int maxn = 1 << 12;
const int inf = 1000000000;

int M[maxn], need[maxn], a[12][maxn], vis[12][maxn];
int d[12][maxn][12];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      memset(vis, 0, sizeof(vis));
      int i, j, k, h, p, n;
      cin >> p;     
      n = 1 << p;
      for (i = 0; i < n; i++) {cin >> M[i]; need[i] = p - M[i];}
      for (i = 1; i <= p; i++)
         for (j = 0; j < (1 << (p-i)); j++) cin >> a[i][j];
      
      for (i = 0; i < 12; i++)
         for (j = 0; j < maxn; j++)
            for (k = 0; k < 12; k++) 
               d[i][j][k] = inf;
      
      for (j = 0; j < n; j++)
         d[0][j][need[j]] = 0;
      for (i = 1; i <= p; i++)
         for (j = 0; j < (1 << (p-i)); j++)
            for (k = 0; k < 12; k++)            
               for (h = 0; h < 12; h++) {
                  int mk = max(k, h);
                  d[i][j][mk] = min(d[i][j][mk], d[i-1][j*2][k] + d[i-1][j*2+1][h]);
                  int mk1 = max(mk-1, 0);
                  d[i][j][mk1] = min(d[i][j][mk1], d[i-1][j*2][k] + d[i-1][j*2+1][h] + a[i][j]);
               }       
                  
      cout << "Case #" << sc+1 << ": ";
      cout << d[p][0][0];
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}