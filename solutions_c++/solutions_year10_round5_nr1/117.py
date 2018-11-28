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

const int maxn = 10000;

int seq[maxn];
int primes[maxn];
int q[16];

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int i, j, k;
   primes[0] = 0;
   for (i = 2; i < maxn; i++) {
      if (!seq[i]) {
         seq[i] = 2;
         primes[++primes[0]] = i;
         j = i+i;
         while (j < maxn) {
            seq[j] = 1;
            j += i;
         }
      }
   }
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      int d;
      cin >> d >> k;
      
      cout << "Case #" << sc+1 << ": ";

      int maxx = 0;
      for (i = 0; i < k; i++) {
         cin >> q[i];
         if (q[i] > maxx) maxx = q[i];
      }
      int deg10 = 1;
      for (i = 0; i < d; i++) deg10 *= 10;

      if (k > 1) {
         set<int> ans;
         for (i = 1; i <= primes[0]; i++) {
            int p = primes[i];
            if (p <= maxx) continue;
            if (p > deg10) break;
            for (int a = 0; a < p; a++) {
               int b = q[1] - (a*q[0]) % p;
               while (b < 0) b += p;
               int ok = 1;
               for (j = 2; j < k; j++)
                  if (q[j] != (a*q[j-1] + b) % p) {
                     ok = 0; break;
                  }
               if (ok) {
                  ans.insert((a*q[k-1] + b) % p);
                  if (ans.size() > 1) break;
               }
            }
            if (ans.size() > 1) break;
         }
         if (ans.size() != 1) cout << "I don't know.";
         else cout << *(ans.begin());
      } else cout << "I don't know.";

      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}