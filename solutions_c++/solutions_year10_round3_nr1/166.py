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

const int maxn = 1024;

int a[maxn], b[maxn];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      int i, j, k, n;
      cin >> n;
      for (i = 0; i < n; i++) {cin >> a[i] >> b[i];}
      
      k = 0;
      for (i = 0; i < n; i++)
         for (j = 0; j < n; j++) if (i != j)
            if (a[i] < a[j] && b[i] > b[j]) k++;
   
      cout << "Case #" << sc+1 << ": ";
      cout << k;
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}