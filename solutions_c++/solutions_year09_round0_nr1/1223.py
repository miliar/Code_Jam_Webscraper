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

char txt[6100];
set<string> slowa; //i ich prefiksy

int parsuj(string s, string pref){
  int res = 0;
  if (!slowa.count(pref)) return 0;
  if (SIZE(s) == 0) return 1;
  if (s[0] == '('){
    int end = 1;
    while (s[end] != ')') end++;
    FOR(i,1,end-1){
      res += parsuj(s.substr(end+1), pref+s[i]);
    }
  } else {
    res += parsuj(s.substr(1), pref+s[0]);
  }
  return res;
}

int main(){
  slowa.insert("");
  int l, d, n;
  scanf("%d %d %d",&l,&d,&n);
  REP(i,d){
    scanf("%s",txt);
    string s = txt;
    while (SIZE(s) > 0){
      slowa.insert(s);
      s = s.substr(0, SIZE(s)-1);
    }
  }
  REP(foo,n){
    printf("Case #%d: ",foo+1);
    scanf("%s",txt);
    string s = txt;
    printf("%d\n", parsuj(s, ""));
  }
  return 0;
}
