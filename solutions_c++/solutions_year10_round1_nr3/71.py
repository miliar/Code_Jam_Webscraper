#include <algorithm>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define debug(x) cerr << #x << " = " << (x) << endl;

const int MAX = 1000005;

int max_a_lose[MAX+1];

bool iswinning(int a, int b) {
   if (a < b) {
      swap(a, b);
   }
   return a > max_a_lose[b];
}

int calc_afixed(int a, int b1, int b2) {
   if (b1 > b2) return 0;
   int max_b_winning = distance(max_a_lose, lower_bound(max_a_lose, max_a_lose+MAX, a))-1;
   int res = max(0, min(max_b_winning, b2) - max(1, b1) + 1);
   return res;
}

int calc_bfixed(int a1, int a2, int b) {
   if (a1 > a2) return 0;
   int losing = max(0, min(a2, max_a_lose[b]) - a1 + 1);
   int res = a2-a1+1 - losing;
   return res;
}

int main(void) { 
   cin.sync_with_stdio(0);

   max_a_lose[0] = 0;
   
   for (int b=1; b<=MAX; ++b) {
      int lo = b, hi = 2*b-1;
      while (lo < hi) {
         int x = (lo+hi+1)/2;
         if (iswinning(b, x-b)) lo = x;
         else hi = x-1;
      }
      max_a_lose[b] = lo;
   }

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      int a1, a2, b1, b2;
      cin >> a1 >> a2 >> b1 >> b2;

      long long res = 0;
      for (int a=a1; a<=a2; ++a) {
         // debug(a);
         if (a >= b2) {
            res += calc_afixed(a, b1, b2);
         } else if (a <= b1) {
            res += calc_bfixed(b1, b2, a);
         } else {
            res += calc_afixed(a, b1, a);
            res += calc_bfixed(a+1, b2, a);
         }
      }
      
      cout << "Case #" << tt << ": " << res << endl;
   }

   return 0;
} 
