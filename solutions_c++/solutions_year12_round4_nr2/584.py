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
vector<pair<ll, int> > r;
vector<pair<ll, ll> > res;
int n;
ll w, l;
ll dx[] = {0 , 1, 1};
ll dy[] = {0, 0, 1};

bool place() {
  ll y = 0;
  ll x = 0;
  ll ny = 0;
  FOR(i,0,n) {
    if ((x==0?0:(x+r[i].first)) > w) {
      x = 0;
      y = ny;
    }
    DEB("Aplace %i %lli %lli l=%lli\n", i, r[i].first, (y==0?r[i].first:(y + r[i].first)),l);
    if ((y==0?0:(y + r[i].first)) > l) {
      return false;
    }

    DEB("place %i %lli %lli\n", i, x, y);

    res[r[i].second] = MP((x==0?0:(x+r[i].first)), (y==0?0:(y + r[i].first)));
    ny = max((y==0?r[i].first:(y + 2*r[i].first)), ny);
    x += 2*r[i].first;
  }
  return true;
}

bool testc(int tc)
{
  r.clear();
  res.clear();
  ll tmp;
  scanf("%i %lli %lli ", &n, &l, &w);
  res = vector<pair<ll, ll> >(n);
  FOR(i,0,n) {
    scanf("%lli ", &tmp);
    r.PB(MP(tmp,i));
  }

  while(1) {
    random_shuffle(r.begin(), r.end());
    DEB("new run\n");
    if (place()) break;
  }

  printf("Case #%i:", tc);
  FOR(i,0,n) printf(" %lli %lli", res[i].second, res[i].first);
  printf("\n");
}

int main()
{
  srand(123);
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);

  /*
    while(testc());
  */
  
  return 0;
}
