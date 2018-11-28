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
using namespace std;

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

#define SZ 1011

int ID[SZ];
int DP[SZ][SZ];
#define INF 0x3f3f3f3f
#define PII pair <int, int>

int main(int argc, char **argv) {
  COND = argc >= 2 && argv[1][0] == 'q';
  ios::sync_with_stdio(false);

  int N;
  scanf("%d\n", &N); 
  FOR (i, 1, N) {
    int ret = INF, S, Q;
    scanf("%d\n", &S);
    DB(S);
    map <string, int> s2i;
    REP (j, S) { char BUF[256]; scanf("%[^\r\n]\n", BUF);
      DB(BUF);
      s2i[BUF] = j;
    }    
    scanf("%d\n", &Q); 
    DB(Q);
    REP (j, Q) { char BUF[256]; scanf("%[^\r\n]\n", BUF);
      DB(BUF);
      ID[j] = s2i[BUF];
    }    

    REP (k, Q + 1) REP (j, S + 1) DP[k][j] = INF;
    REP (j, S + 1) DP[0][j] = 0;
    
    REP (k, Q) {
      vector <PII> QQ;
      REP (j, S) QQ.PB(PII(DP[k][j], j));
      sort(ALL(QQ));

      REP (j, S) {
	if (ID[k] != j) {
	  DP[k+1][j] = min(DP[k+1][j], DP[k][j]);
	  REP (p, 2) {
	    DP[k+1][j] = min(DP[k+1][j], QQ[p].X + 1);
	  }
	}
      }      
    }
    
    REP (j, S) {
      ret = min(ret, DP[Q][j]);
    }

    printf("Case #%d: %d\n", i, ret);
  }

  return 0;
}
