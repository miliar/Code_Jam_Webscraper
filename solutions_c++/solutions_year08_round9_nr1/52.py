#include <iostream>
#include <cstdio>

#include <map>
#include <queue>
#include <set>
#include <vector>
#include <string>

#include <cmath>
#include <algorithm>
#include <sstream>
#include <ctype.h>

#define FOR(i,a,b) for (int i=(a); i<(int)(b); i++)
#define FI(b)      FOR(i,0,b)
#define FJ(b)      FOR(j,0,b)
#define FK(b)      FOR(k,0,b)
#define FC(b)      FOR(c,0,b)
#define EACH(x,it) for(__typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

#define ZERO(x) memset((x),0,sizeof(x))
#define NEG(x) memset((x),-1,sizeof(x))

#define ASIZE(x) sizeof(x) / sizeof(x[0])

using namespace std;

int want[5010][3];

int main() {
   int cases;
   cin >> cases;

   FC(cases) {
      int N;
      cin >> N;

      for(int i=0; i<N; i++) FJ(3) cin >> want[i][j];

      int got[3],ans=0;
      FI(N) FJ(N) {
          got[0] = want[i][0];
          got[1] = want[j][1];
          got[2] = 10000-got[0]-got[1];

          int cur=0;
          FK(N) if (got[0] >= want[k][0] && got[1] >= want[k][1] && got[2] >= want[k][2]) cur++;
          ans >?= cur;
      }

      cout << "Case #" << c+1 <<": " << ans<<endl;
   }
}
