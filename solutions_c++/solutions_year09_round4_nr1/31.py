#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define A first
#define B second
typedef long double ld;

int cas=0;
int N;
char matrix[64][64];
int where[64];
void doit() {
  scanf("%d",&N);
  FOR(i,N) scanf("%s",matrix[i]);

  CLR(where,-1);

  FOR(i,N) {
    FOR(j,N) if (where[j]==-1) {
      bool happy=1;
      FR(k,i+1,N) if (matrix[j][k]=='1') happy=0;
      if (happy) {
	where[j] = i;
	break;
      }
    }
  }

  int ans = 0;
  FOR(i,N) FR(j,i+1,N) {
    if (where[i]>where[j]) ++ans;
  }

  printf("Case #%d: %d\n",++cas,ans);
}

int zzzz;
int main() {
  scanf("%d ",&zzzz);
  FOR(i,zzzz) doit();
}
