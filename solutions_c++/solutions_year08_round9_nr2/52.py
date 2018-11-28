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

bool vis[110][110];

int dr[2], dc[2], rown, coln;
int go(int r, int c) {
    if (r<0 || c<0 || r>=rown || c>=coln || vis[r][c]) return 0;
    vis[r][c] = 1;
    int ans=1;
    FI(2) ans+=go(r+dr[i], c+dc[i]);
    return ans;
}

int main() {
   int cases;
   cin >> cases;

   FC(cases) {
      memset(vis,0,sizeof(vis));

      cin >> coln >> rown;

      int initc,initr;
      cin >> dc[0] >> dr[0] >> dc[1] >> dr[1]>>initc>>initr;
      int ans = go(initr,initc);

      cout << "Case #" << c+1 <<": "<<ans<<endl;
   }
}
