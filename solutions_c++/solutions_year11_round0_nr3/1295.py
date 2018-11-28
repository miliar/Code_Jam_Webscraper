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
      int i, n;
      cin >> n;
      VI a(n);
      int s = 0;
      int m = 1000000;
      int sum = 0;
      for (i = 0; i < n; i++) {
         cin >> a[i];
         s ^= a[i];
         sum += a[i];
         m = a[i] < m ? a[i] : m;
      }   
      
      cout << "Case #" << sc+1 << ": ";
      if (!s) {
         cout << sum - m;
      } else cout << "NO";
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}