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

const int N = 1100;
int wiezien[N];
int n;
map<PII,int> mapa;

int licz(int a,int b){
  if (a > b) return 0;
  if (mapa.count(MP(a,b))) return mapa[MP(a,b)];
  int res = 1000000000;
  int ilu = 0;
  REP(i,n) if (wiezien[i] >= a && wiezien[i] <= b){
    res = min(res,b-a + licz(a,wiezien[i]-1) + licz(wiezien[i]+1,b));
    ilu++;
  }
  if (ilu == 0) res = 0;
  return mapa[MP(a,b)] = res;
}

int main(){
  int testy;
  scanf("%d",&testy);
  REP(numer,testy){
    printf("Case #%d: ", numer+1);
    int p;
    scanf("%d %d",&p,&n);
    REP(i,n) scanf("%d",wiezien+i);
    sort(wiezien, wiezien+n);
    mapa.clear();
    int wynik = licz(1,p);
    printf("%d\n",wynik);
  }
  return 0;
}
