#include <cstring>
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

char txt[1000];
int t[1000];

int main(){
  int testy;
  scanf("%d",&testy);
  REP(numer,testy){
    printf("Case #%d: ", numer+1);
    scanf("%s",txt);
    map<char,int> mapa;
    int n = strlen(txt);
    mapa[txt[0]] = 1;
    t[0] = 1;
    int wolne = 0;
    FOR(i,1,n-1){
      if (mapa.count(txt[i])) t[i] = mapa[txt[i]];
      else {
        t[i] = mapa[txt[i]] = wolne;
        if (wolne == 0) wolne = 2;
        else wolne++;
      }
    }
    if (wolne == 0) wolne = 2;
    LL wynik = 0;
    REP(i,n) wynik = wynik * wolne + t[i];
    printf("%lld\n",wynik);
  }
  return 0;
}
