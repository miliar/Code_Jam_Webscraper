/* AnilKishore * India */

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++)
#define EACH(it,v) for(typeof((v).begin()) it = (v).begin();it!=(v).end();it++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})

#define MX 100005

char B[5][5];

bool won(char c) {
  REP(r,4) {
    bool allc = true;
    REP(j,4) if(B[r][j]!=c && B[r][j]!='T') allc = false;
    if (allc) return true;
  }
  REP(cc,4) {
    bool allc = true;
    REP(i,4) if(B[i][cc]!=c && B[i][cc]!='T') allc = false;
    if (allc) return true;
  }
  bool allc = true;
  REP(i,4) if(B[i][i]!=c && B[i][i]!='T') allc = false;
  if (allc) return true;

  allc = true;
  REP(i,4) if(B[i][3-i]!=c && B[i][3-i]!='T') allc = false;
  return allc;
}

bool isSomeEmpty() {
  REP(i,4) REP(j,4) if(B[i][j] == '.') return true;
  return false;
}

int main()
{
  for(int kase=1,kases=SI;kase<=kases;kase++)
  {
    printf("Case #%d: ",kase);
    REP(i, 4) scanf("%s ",B[i]);
    if (won('X')) {
      puts("X won");
    } else if (won('O')) {
      puts("O won");
    } else if (isSomeEmpty()) {
      puts("Game has not completed");
    } else {
      puts("Draw");
    }
  }
  return 0;
}
