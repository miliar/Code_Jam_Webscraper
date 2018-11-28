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
      vector<int> b, o, bb, oo;
      for (i = 0; i < n; i++) {
         string s;
         int num;
         cin >> s >> num;
         if (s == "B") {b.PB(num); bb.PB(i);} else {o.PB(num); oo.PB(i);}
      }
      bb.PB(n+1); oo.PB(n+1);
      
      int posb = 1, poso = 1;      
      i = j = k = 0;
      while (i != b.size() || j != o.size()) {
         int ii = i;
         if (i < b.size()) {
            if (posb == b[i] && bb[i] < oo[j]) i++;
            else if (posb < b[i]) posb++;
            else if (posb > b[i]) posb--;
         }
         if (j < o.size()) {
            if (poso == o[j] && oo[j] < bb[ii]) j++;
            else if (poso < o[j]) poso++;
            else if (poso > o[j])poso--;
         }
         k++;
      }

      cout << "Case #" << sc+1 << ": ";
      cout << k;
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}