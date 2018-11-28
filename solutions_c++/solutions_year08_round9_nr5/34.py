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

int rown, coln;
int cache[15][15][1<<15];

string cal[20];

int go(int r, int c, int m) {
   if (r == rown) return 0;
   if (c == coln) return go(r+1,0,m);

   int &ans=cache[r][c][m];
   if (ans >= 0) return ans;

   ans=0;
   if (cal[r][c] == '#' || cal[r][c] == '?') {
      int cnt=0;
      if (c>0 && (m & (1<<(c-1))))cnt++;
      if (r>0 && (m & (1<<c))) cnt++;
      //cout << "CNT="<<cnt<<endl;
      ans >?= 4 - 2*cnt + go(r, c+1, m | (1<<c));
   }

   if (cal[r][c] == '.' || cal[r][c] == '?') {
      ans >?= go(r, c+1, m & (~(1<<c)));
   }
   return ans;
}

int main() {
   int cases;
   cin >> cases;

   FC(cases) {
      cin >> rown >> coln;
      FI(rown) cin >> cal[i];

      NEG(cache);
      cout << "Case #" << (c+1) <<": "<<go(0,0,0)<<endl;
   }
}
