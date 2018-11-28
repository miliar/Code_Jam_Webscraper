#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int64;
template<typename Set, typename Element> inline bool inset( const Set &S, const Element &E ) { return S.find(E) != S.end(); }

int main(void) { 
   cin.sync_with_stdio(0);

   int CASES; cin >> CASES;
   for ( int tt=1; tt<=CASES; ++tt ) { // caret here
      int64 R, K, n; cin >> R >> K >> n;
      vector<int64> g(n);
      for (int i=0; i<n; ++i) cin >> g[i];

      int pos = 0, cycle_start = -1;
      vector<int64> yield;
      map<int, int> when;

      for (int iter=0; iter<R; ++iter) {
         when[pos] = iter;
         int i;
         int64 sum = 0;
         for (i=pos;;) {
            if (sum + g[i] > K) {
               break;
            }
            sum += g[i];
            
            if (++i == n) {
               i = 0;
            }
            if (i == pos) {
               break;
            }
         }

         yield.push_back(sum);
         pos = i;
         if (inset(when, pos)) {
            cycle_start = when[pos];
            break;
         }
      }

      int64 total;
      if (cycle_start == -1) {
         total = accumulate(yield.begin(), yield.end(), 0LL);
      } else {
         vector<int64>
            head(yield.begin(), yield.begin() + cycle_start),
            cycle(yield.begin() + cycle_start, yield.end());
         total =
            accumulate(head.begin(), head.end(), 0LL) + 
            (R - head.size()) / cycle.size() * accumulate(cycle.begin(), cycle.end(), 0LL) +
            accumulate(cycle.begin(), cycle.begin() + (R - head.size()) % cycle.size(), 0LL);
      }
      cout << "Case #" << tt << ": " << total << "\n";
   }

   return 0;
} 
