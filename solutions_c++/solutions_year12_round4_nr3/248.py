#define DEBUG 1
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <sys/time.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
const int INF = 2000000001;
#define FOR(x,b,e) for(int x=(b);x<=(e);++x)
#define FORD(x,b,e) for(int x=(b);x>=(e);--x)
#define REP(x,n) for(int x=0;x<(n);++x)
#define ALL(c) c.begin(),c.end()
#define VAR(x,c) __typeof(c) x=(c)
#define FOREACH(x,c) for(VAR(x,(c).begin());x!=(c).end();++x)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define dbg(...) \
  do { if (DEBUG) fprintf(stderr, __VA_ARGS__); } while (0)

const int MAXN = 2000;

int N;
int l[MAXN+1];
int h[MAXN+1];

void rand_h() {
  FOR(i,1,N) {
    h[i] = rand()%400;
  }
}

int check() {
  FOR(i,1,N-1) {
    FOR(j,i+1,N) {
      if (j != l[i]) {
        int x1 = j-i;
        int y1 = h[j]-h[i];
        int x2 = l[i]-i;
        int y2 = h[l[i]]-h[i];
        if (x1*y2 - x2*y1 <= 0) {
          return 0;
        }
      }
    }
  }
  return 1;
}

void calculate() {
  rand_h();
  while (! check()) { rand_h(); }
}

struct timeval T;

int main() {
  gettimeofday(&T,0);
  srand(T.tv_usec);
  int Z;
  scanf("%d", &Z);
  for (int T = 1; T <= Z; T++) {
    scanf("%d", &N);
    FOR (i,1,N-1) {
      scanf("%d", &l[i]);
      h[i] = 0;
    }
    h[N] = 0;

    printf("Case #%d: ", T);

    bool flag = true;
    FOR(i,1,N-1) {
      FOR(j, i+1, l[i]-1) {
        if (l[j] > l[i]) { flag = false; }
      }
    }
    
    if (flag) {
      calculate();
      FOR (i,1,N) {
        printf("%d ", h[i]);
      }
    } else {
      printf("Impossible");
    }
    
    printf("\n");
  }
  return 0;
}
