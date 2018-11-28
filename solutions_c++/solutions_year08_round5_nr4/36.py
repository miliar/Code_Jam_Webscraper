#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cassert>
using namespace std;


#define VV vector
#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND = 0;

#define DB(x) { if (COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

#define SZ 111
int BAD[SZ][SZ];
int ST[SZ][SZ];
#define MOD 10007
int main(int argc, char **argv) {
  COND = argc >= 2 && argv[1][0] == 'q';
  int T; cin >> T;
  FOR (my, 1, T) {
    int H, W, R; cin >> H >> W >> R;
    CLR(BAD, 0); CLR(ST, 0);
    REP (i, R) { int x, y; cin >> x >> y;
      BAD[x][y] = 1;
    }
    ST[1][1] = 1;
    FOR (i, 1, H)
      FOR (j, 1, W) if (!BAD[i][j]){
        //1,2
        //2,1

        ST[i+2][j+1] = (ST[i+2][j+1] + ST[i][j]) % MOD;
        ST[i+1][j+2] = (ST[i+1][j+2] + ST[i][j]) % MOD;
      }
    printf("Case #%d: %d\n", my, ST[H][W]);
  }

  return 0;
}
