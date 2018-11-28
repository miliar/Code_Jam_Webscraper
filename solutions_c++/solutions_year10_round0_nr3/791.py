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
#include <cassert>
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

const int N = 1100;

int grupa[N];

LL licz(int &pos, int k, int n){
  LL mam = 0;
  REP(i,n)
    if (mam + grupa[pos] <= k){
      mam += grupa[pos];
      pos = (pos+1) % n;
    } else break;
  return mam;
}

int main(){
  int testy;
  scanf("%d",&testy);
  int numer = 0;
  while (testy--){
    LL res = 0;
    printf("Case #%d: ",++numer);
    int r,k,n;
    scanf("%d %d %d",&r,&k,&n);
    REP(i,n) scanf("%d",grupa+i);
    int pos = 0;
    REP(foo,n+2) if (r > 0){
      r--;
      res += licz(pos,k,n);
    }
    if (r > n){
      int start = pos;
      int tury = 0;
      LL suma = 0;
      do {
        tury++;
        r--;
        int x = licz(pos,k,n);
        res += x;
        suma += x;
        assert(r >= 0);
      } while (pos != start);
      int pelne = r / tury;
      res += suma * (LL)pelne;
      r = r % tury;
    }
    while (r > 0){
      r--;
      res += licz(pos,k,n);
    }
    printf("%lld\n", res);
  }
  return 0;
}
