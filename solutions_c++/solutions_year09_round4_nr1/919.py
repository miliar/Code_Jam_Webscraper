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

const int maxn = 50;

int a[maxn];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int i, j, k;
   int t; cin >> t;
   for (int sc = 0; sc < t; sc++) {
      int n;
      cin >> n;
      VS s(n);
      for (i = 0; i < n; i++) {
         string tmp;
         cin >> tmp;
         s[i] = tmp;
         a[i] = -1;
         for (j = 0; j < n; j++)
            if (s[i][j] == '1') a[i] = j;
      }
      
      int ans = 0;
      for (i = 0; i < n; i++) {
         k = -1;
         for (j = i; j < n; j++) {
            if (a[j] <= i) {
               k = j; break;
            }
         }
         for (j = k; j > i; j--) {
            ans++;
            swap(s[j], s[j-1]);
            swap(a[j], a[j-1]);
         }
      }
      
      cout << "Case #" << sc+1 << ": " << ans << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}