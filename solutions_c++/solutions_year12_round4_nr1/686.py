#include <assert.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string>
#include <list>
#include <stack>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <list>
#define INF 0x3fffffff
#define LINF 0x3fffffffffffffffll
#define DINF 1e100
#define EPS 0.000000000001

typedef long long ll;
#define PII pair<int, int>
#define PLL pair<ll, ll>
#define PDD pair<double, double>
#define PIL pair<int, ll>
#define PLI pair<ll, int>
#define PID pair<int, double>
#define PDI pair<double, int>
#define PLD pair<ll, double>
#define PDL pair<double, ll>

#define NUL(x) memset(x, 0, sizeof(x))
#define MINUS(x) memset(x, 0xff, sizeof(x))
#define PQ(x) priority_queue< x >  //highest first
#define PQR(x) priority_queue< x , vector< x > , greater < x > > //lowest first
#define MP make_pair
#define PB push_back
#define IT(x) for (typeof((x).begin()) it = (x).begin() ; it != (x).end() ; it++)
#define IT2(x) for (typeof((x).begin()) it2 = (x).begin() ; it2 != (x).end() ; it2++)
#define FOR(i, a, b) for (int i = (a) ; i< (b) ; i++)
//#define DEB(x...) fprintf(stderr,x)
#define DEB

using namespace std;

map<int, int> ropes; //[pos]=len
map<int, map<int, bool> > mem;
int d;

bool memo(int pos, int len) {
  DEB("memo %i %i\n", pos, len);
  if (pos + len>=d) return true;
  if (mem.find(pos) != mem.end() && mem[pos].find(len)!=mem[pos].end())
    return mem[pos][len];
  
  map<int, int>::iterator it = ropes.upper_bound(pos + len);
  map<int, int>::iterator cur = ropes.find(pos);
  it--;
  bool poss = false;
  while(it != cur) {
    int tmp = min(it->first - pos, it->second);
    DEB("candidate %i %i\n", it->first, tmp);
    if (memo(it->first, tmp)) {
      poss = true;
      break;
    }

    it--;
  }
  mem[pos][len] = poss;
  return poss;
}
bool testc(int tc)
{
  ropes.clear();
  mem.clear();
  int n, a,b;
  scanf("%i ", &n);
  FOR(i,0,n) {
    scanf("%i %i ", &a, &b);
    ropes[a] = b;
  }
  scanf("%i ", &d);

  bool p = memo(ropes.begin()->first, ropes.begin()->first);
  printf("Case #%i: %s\n", tc, p?"YES":"NO");
}

int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);
  
  return 0;
}
