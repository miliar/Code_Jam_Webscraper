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

const int inf = (1<<31)-1;

/*
  3 2
  0 1
*/

int R,C;
int S[20][20],W[20][20],T[20][20];
bool mark[20][20][4];
int dist[20][20][4];

int cas=0;
void doit() {
  scanf("%d%d",&R,&C);

  CLR(mark,0);
  FOR(r,R) {
    FOR(c,C) {
      int x = scanf("%d%d%d",&S[R-r-1][c],&W[R-r-1][c],&T[R-r-1][c]);
      assert(x == 3);
      FOR(a,4) dist[R-r-1][c][a] = inf;
    }
  }
  assert(dist[R-1][C-1][2] == inf);

  priority_queue<pair<int,pair<pair<int,int>,int> > > q;
  q.push(MP(0,MP(MP(0,0),0)));
  dist[0][0][0] = 0;

  int prevt = 0;
  while (q.size()) {
    int t = -q.top().A;
    assert(t >= prevt);
    prevt = t;
    int r = q.top().B.A.A;
    int c = q.top().B.A.B;
    int a = q.top().B.B;
    q.pop();
    if (mark[r][c][a]) continue;
    mark[r][c][a] = 1;
    //fprintf(stderr, "AT: %d %d %d; time %d\n",r,c,a,t);

#define DOIT assert(0<=r2); assert(r2<R); assert(0<=c2); assert(c2<C); \
  assert(t2>t); assert(0<=a2 && a2<4); do { if (t2 < dist[r2][c2][a2]) { \
  assert(!mark[r2][c2][a2]); dist[r2][c2][a2] = t2; \
  q.push(MP(-t2,MP(MP(r2,c2),a2))); } } while(0)

    if ((a == 0 || a == 3) && c>0) { // left
      int r2 = r, c2 = c-1, a2 = a^1, t2 = t+2;
      DOIT;
    }
    if ((a == 1 || a == 2) && c+1<C) { // right
      int r2 = r, c2 = c+1, a2 = a^1, t2 = t+2;
      DOIT;
    }
    if ((a == 0 || a == 1) && r>0) { // down
      int r2 = r-1, c2 = c, a2 = 3-a, t2 = t+2;
      DOIT;
    }
    if ((a == 2 || a == 3) && r+1<R) { // up
      int r2 = r+1, c2 = c, a2 = 3-a, t2 = t+2;
      DOIT;
    }

    int len = S[r][c]+W[r][c];
    T[r][c] %= len;
    int now = ((t-T[r][c])%len+len)%len;
    assert(0 <= now && now < len);

    { // north-south
      int r2 = r, c2 = c, a2 = 3-a;
      int t2 = t+1;
      if (now >= S[r][c]) t2 += len - now;
      DOIT;
    }
    { // east-west
      int r2 = r, c2 = c, a2 = a^1;
      int t2 = t+1;
      if (now < S[r][c]) t2 += S[r][c] - now;
      DOIT;
    }
  }
  assert(mark[R-1][C-1][2]);
  int ans = dist[R-1][C-1][2];
  assert(0 <= ans && ans < inf);

  printf("Case #%d: %d\n", ++cas, ans);
}

int zzzz;
int main() {
  scanf("%d ",&zzzz);
  FOR(i,zzzz) doit();
}
