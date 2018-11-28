#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

int bylo[1010];
long long euros[1010];

int grps[1010];
int n, k, r;

int main(){
  int te;
  scanf("%d", &te);
  FOR(ii, 1, te){
    scanf("%d%d%d", &r, &k, &n);
    REP(i, n) scanf("%d", &grps[i]);
    REP(i, n+1) bylo[i] = -1;
    long long euro = 0LL;
    int it = 0;
    int poz = 0;
    while (bylo[poz] == -1 && it < r){
      bylo[poz] = it++;
      euros[poz] = euro;
      int npoz = poz, wsiada = 0;
      while (npoz < poz + n){
        if (wsiada + grps[npoz % n] > k)
          break;
        wsiada += grps[npoz % n];
        npoz++;
      }
      euro += wsiada;
      poz = npoz % n;
    }
    if (it < r){
      int diff = it - bylo[poz];
      long long eurodiff = euro - euros[poz];
      int obroty = (r - it) / diff;
      euro += (long long)obroty * eurodiff;
      it += obroty * diff;
    }
    while (it < r){
      int npoz = poz, wsiada = 0;
      while (npoz < poz + n){
        if (wsiada + grps[npoz % n] > k)
          break;
        wsiada += grps[npoz % n];
        npoz++;
      }
      euro += wsiada;
      poz = npoz % n;
      it++;
    }
    printf("Case #%d: %lld\n", ii, euro);
  }
  return 0;
}
