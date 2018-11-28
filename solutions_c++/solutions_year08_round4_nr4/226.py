#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>

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

int n, k, a[20];
string s, s1, t, t1;

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> k >> s; n = s.length();
      for (i = 1; i <= k; i++) a[i] = i;
      int ans = n;
      while (1) {
         s1 = "";
         for (i = 0; i < n/k; i++) {
            t = s.substr(i*k, k); t1 = t;
            for (j = 1; j <= k; j++) t1[j-1] = t[a[j]-1];
            s1 += t1;
         }
         j = 1;
         for (i = 1; i < n; i++) if (s1[i] != s1[i-1]) j++;
         if (j < ans) ans = j;
         if (!next_permutation(a+1, a+k+1)) break;
      }
      cout << "Case #" << sc << ": ";
      cout << ans;
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}