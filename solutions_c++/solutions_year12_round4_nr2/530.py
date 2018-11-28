#define DEBUG 0
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

const int MAXN = 1000;
int N, W, L;
int r[MAXN+1];
pair<int,int> pos[MAXN+1];

struct timeval T;

bool check() {
  FOR (i,1,N) {
    FOR (j,1,N) {
      if (i == j) { continue; }
      double x = pos[i].first - pos[j].first;
      double y = pos[i].second - pos[j].second;
      double len = sqrt(x*x+y*y);
      if ((r[i] + r[j]) > len) { return false; }
    }
  }
  return true;
}

void rand_pos() {
  FOR (i,1,N) {
    pos[i].ST = rand()%W;
    pos[i].ND = rand()%L;
  }
}

void calculate() {
  rand_pos();
  while ( ! check()) {
    rand_pos();
  }
}

int main() {
  gettimeofday(&T,0);
  srand(T.tv_usec);
  int Z;
  scanf("%d", &Z);
  for (int T = 1; T <= Z; T++) {
    scanf("%d%d%d", &N, &W, &L);
    FOR (i,1,N) {
      scanf("%d", &r[i]);
    }

    printf("Case #%d: ", T);

    calculate();
    FOR(i,1,N) {
      printf("%d %d ", pos[i].ST, pos[i].ND);
    }

    printf("\n");
  }
  return 0;
}
