#include <iostream>
#include <fstream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <complex>
#include <cassert>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define EACH(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define FOR(i,k,n) for (int i=(k);i<(int)(n);i++)
#define FEQ(i,k,n) for(int i=(k);i<=(int)(n);i++)
typedef long long ll;
typedef complex<double> P;

int main()
{
  int tc;scanf("%d",&tc);
  for(int t=1;t<=tc;t++){
    int r,c;scanf("%d%d",&r,&c);
    char tiles[60][60];
    REP(i,r) scanf("%s",tiles[i]);
    int blue = 0;
    REP(i,r) REP(j,c) if (tiles[i][j] == '#') blue++;
    printf("Case #%d:\n",t);
    REP(i,r) REP(j,c){
      if (tiles[i][j] == '#'){
        if (i + 1 < r && j + 1 < c &&
            tiles[i+1][j] == '#' && tiles[i][j+1] == '#' && tiles[i+1][j+1] == '#'){
          tiles[i][j] = '/';
          tiles[i][j+1] = '\\';
          tiles[i+1][j] = '\\';
          tiles[i+1][j+1] = '/';
          blue -= 4;
        } else
          goto IMPOSSIBLE;
      }
    }
    if (blue != 0) goto IMPOSSIBLE;
    REP(i,r) puts(tiles[i]);
    continue;
  IMPOSSIBLE:
    puts("Impossible");
  }
  return 0;
}
