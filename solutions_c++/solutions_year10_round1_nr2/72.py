#include <algorithm>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename U> inline void relaxmin( T &res, const U &x ) { if ( x < res ) res = x; }
#define MINUS1(v) memset(v, -1, sizeof v)

int D, I, M, N;
vector<int> val;
int memo[105][256];

int calc(int pos, int lastval) {
   if (pos == N) {
      return 0;
   }

   int &ret = memo[pos][lastval];
   if (ret != -1) {
      return ret;
   }

   ret = INT_MAX/4;

   // no-op
   if (abs(val[pos] - lastval) <= M) {
      relaxmin(ret, calc(pos+1, val[pos]));
   }

   // delete
   relaxmin(ret, D+calc(pos+1, lastval));

   for (int v=0; v<=255; ++v) {
      // modify
      if (abs(v-lastval) <= M) {
         relaxmin(ret, abs(v-val[pos]) + calc(pos+1, v));
      }

      // insert
      if (M != 0) {
         int hops = max(0, (abs(v-lastval)-1) / M);
         relaxmin(ret, hops*I + abs(v-val[pos]) + calc(pos+1, v));
      }
   }

   return ret;
}

int main(void) { 
   cin.sync_with_stdio(0);

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      cin >> D >> I >> M >> N;
      val.resize(N);
      for (int i=0; i<N; ++i) {
         cin >> val[i];
      }

      MINUS1(memo);
      int res = INT_MAX/4;
      for (int v=0; v<=255; ++v) {
         relaxmin(res, calc(0, v));
      }
      cout << "Case #" << tt << ": " << res << endl;
   }

   return 0;
} 
