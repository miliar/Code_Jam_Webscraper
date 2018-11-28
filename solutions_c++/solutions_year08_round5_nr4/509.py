#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <sys/time.h>
#include <regex.h>

using namespace std;

#define DEBUG(x) cout << #x << ": " << x << endl

#define sz(a) int((a).size())

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define REPD(i,n) for(int i=(n)-1;i>=0;--i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACHD(it,c) for(typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)

#define ALL(c) (c).begin(),(c).end()

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

typedef pair<int,int> II;

typedef long long llong;

#define MOD 10007

int A[120][120];

int main(int argc, char *argv[]) {
   ios_base::sync_with_stdio(false);

   int TC;
   cin >> TC;

   for (int tc = 1; tc <= TC; ++tc) {
      int H, W, R;
      cin >> H >> W >> R;
      memset(A, 0, sizeof(A));
      for (int i = 0; i < R; ++i) {
         int r, c;
         cin >> r >> c;
         A[r][c] = -1;
      }
      A[1][1] = 1;
      for (int r = 2; r <= H; ++r) {
         for (int c = 2; c <= W; ++c) {
            if (A[r][c] < 0) continue;
            if (r >= 1 && c >= 2 && A[r-1][c-2] > 0) {
               A[r][c] += A[r-1][c-2];
               A[r][c] %= MOD;
            }
            if (r >= 2 && c >= 1 && A[r-2][c-1] > 0) {
               A[r][c] += A[r-2][c-1];
               A[r][c] %= MOD;
            }
         }
      }

      cout << "Case #" << tc << ": " << A[H][W] << endl;
   }

   return 0;
}
