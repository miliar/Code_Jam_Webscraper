// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

string want = "welcome to code jam";
string line;
int N;

int cnt[100][100];

int main() {
  getline(cin,line);
  stringstream(line) >> N;
  FOR(n,1,N) {
    getline(cin,line);
    int A = SIZE(want), B = SIZE(line);
    FOR(a,0,A) {
      FOR(b,0,B) {
        if (a==0 && b==0) { cnt[a][b]=1; continue; }
        if (a > b) { cnt[a][b]=0; continue; }
        cnt[a][b] = cnt[a][b-1];
        if (want[a-1]==line[b-1]) cnt[a][b] += cnt[a-1][b-1];
        cnt[a][b] %= 10000;
      }
    }
    printf("Case #%d: %04d\n",n,cnt[A][B]);
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
