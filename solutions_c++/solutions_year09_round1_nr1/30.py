#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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

int sqr(int x) { return x*x; }

int step(int x, int b) {
  int y = 0;

  while (x) {
    y += sqr(x%b);
    x /= b;
  }
  return y;
}

bool unhappy[11][11814486];
bool thehappy[11][11814486];
bool happy(int x, int b) {
  set<int> seen;

  while (1) {
    if (seen.count(x) || unhappy[b][x]) {
      FORALL(yy,seen) unhappy[b][*yy] = 1;
      return 0;
    }
    if (x == 1 || thehappy[b][x]) {
      FORALL(yy,seen) thehappy[b][*yy] = 1;
      return 1;
    }
    seen.insert(x);

    x = step(x,b);
  }
}

char buf[256];

int cas=0;
void doit() {
  scanf("%[^\n] ",buf);

  vector<int> bs;
  int x;
  istringstream iss(buf);
  while (iss >> x) bs.PB(x);

  int ans = 2;

  while (1) {
    bool ok = 1;
    FORALL(b,bs) {
      if (!happy(ans,*b)) {
	ok = 0;
	break;
      }
    }
    if (ok) break;

    ++ans;
  }

  printf("Case #%d: %d\n", ++cas, ans);
  fprintf(stderr, "%d ", cas);
}

int T;
int main() {
  CLR(unhappy,0);
  CLR(thehappy,0);
  scanf("%d ",&T);
  FOR(i,T) doit();
}
