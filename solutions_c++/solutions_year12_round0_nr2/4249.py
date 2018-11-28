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
#define DEB(x...) fprintf(stderr,x)
//#define DEB

using namespace std;

#define MAXN 105
int sum,n,s,p;

bool testc(int tc=0) {
  scanf("%i %i %i ", &n, &s, &p);
  int res = 0;
  int cnt = 0;
  FOR(i,0,n) {
    scanf("%i ", &sum);

    int val = sum/3;
    //    DEB("sum=%i val=%i s=%i p=%i res=%i\n", sum, val, s, p, res);
    if (val*3 == sum) {
      if (val >= p) res++;

      if (val != 0 && val != 10) {
        if (val+1 == p) cnt++;
      }
    } else if (2*(val+1)+val == sum) {
      assert(val<10);
      if (val+1>=p) res++;
      
      if (val+1!=10) {
        if (p == val+2) cnt++;
      }
    } else {
      assert(2*val + val+1 == sum);

      if (val+1 >= p) res ++;
    }
  }

  res += min(s, cnt);
  printf("Case #%i: %i\n", tc, res);
}


int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);

  return 0;
}
