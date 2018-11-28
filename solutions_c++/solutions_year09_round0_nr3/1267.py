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
#include <cstdlib>
#include <cstring>
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
const int MOD = 10000;
char txt[N];
string s = "welcome to code jam";
int t[N][N];

int licz(int a,int b){
  if (b == SIZE(s)) return 1;
  if (txt[a] == '\0') return 0;
  int &res = t[a][b];
  if (res >= 0) return res;
  res = 0;
  if (txt[a] == s[b]) res += licz(a+1,b+1);
  res += licz(a+1,b);
  res %= MOD;
  return res;
}

int main(){
  int testy;
  fgets(txt,999,stdin);
  sscanf(txt,"%d",&testy);
  REP(foo,testy){
    printf("Case #%d: ",foo+1);
    fgets(txt,999,stdin);
    memset(t,0xff,sizeof(t));
    printf("%04d\n",licz(0,0));
  }
  return 0;
}
