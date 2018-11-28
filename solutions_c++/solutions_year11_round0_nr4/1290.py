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

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      int i, j, k, n;
      
      cin >> n;
      VI a;
      for (i = 0; i < n; i++) {
         cin >> j;
         a.PB(j-1);
      }
      
      VI vis(n);
      k = 0;
      for (i = 0; i < n; i++)
         if (!vis[i]) {
            j = i;
            int len = 0;
            while (!vis[j]) {
               vis[j] = 1;
               j = a[j];
               len++;
            }
            k += len > 1 ? len : 0;
         }

      cout << "Case #" << sc+1 << ": ";
      cout << k << ".0";
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}