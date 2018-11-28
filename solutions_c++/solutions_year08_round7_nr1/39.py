#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/
#define PB push_back
#define CS c_str()
#define EL printf("\n")
#define SIZE(x) (int)((x).size())

#define ALL(v) (v).begin(), (v).end()
#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define VAR(a,b) __typeof (b) a=b
#define FORE(i,a)  for(VAR(i,a.begin()); i!=a.end(); ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))
#define SORT(x) sort( (x).begin(), (x).end() ) 


typedef vector<int> VI;
typedef vector<string> VS;
VS split2(string s, char c){
  string tmp="";
  VS ret; int n = s.length(); 
  REP(i,n+1){
	if(i<n && s[i] != c) tmp += s[i];
	else if(tmp.length()>0) { ret.PB(tmp); tmp=""; }
  }
  return ret;  
}
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

int N;
map<string, int > name;
map<string, VS> edge;
VS xx;
const int MAX = 2000;
int vis[MAX], deg[MAX];
int go(string s)
{
   if(islower(s[0])) return 0;
   VI v;
   FORE(i, edge[s]) {
      string z = *i;
      //if(isupper(z[0])) ++deg[ name[s]]; 
      if(isupper(z[0])) { v.PB(go(z)); ++deg[name[s]]; }
      //ret = max( ret, go(z));
   }
  
  SORT(v);
  reverse(ALL(v));
  
  int ret = deg[name[s]] + 1;
  REP(i, SIZE(v)) ret = max(ret, v[i]+i);
  
  /*
  printf("s = '%s'\n", s.CS);
  REP(i, SIZE(v)) printf("%d ", v[i]); EL;
  printf("ret = %d\n", ret); */
//  if(SIZE(v) == 0) return 1;
  return ret;
}


  bool ready[20], in_bowl[20];
  int calc(void)
  {
    int ret  = 0;
    REP(i, N) ret += in_bowl[i];
    return ret;
  }

void brut(void)
{
  int p[20];
  REP(i, N) p[i] = i;
  int ret = INF;
  do {
    
    REP(i, N) ready[i] = 0;
    REP(i, N) in_bowl[i] = 0;
    bool bad = 0;
    int mx = 0;

    REP(i, N) {
      int v = p[i];
      if(islower(xx[v][0])) { ready[v] = 1; continue; }
      else {
        bool ok = true;
        FORE(i, edge[xx[v]]) {
          string s = *i;
          if(isupper(s[0]) && !ready[ name[s] ]) ok = false;
        }
        if(!ok)   bad = 1;
        else {
          in_bowl[v] = 1;
          int mx = max(mx, calc());
          FORE(i, edge[xx[v]]) in_bowl[ name[*i]] = 0;
        }
      }
    }
    
    if(!bad) ret = min(ret, mx);
  }while(next_permutation(p,p+N));
  
  printf("%d\n", ret);
}   

void solve(void)
{
  scanf("%d\n", &N);
  char buff[4000];
  name.clear();
  edge.clear();
  xx.clear();
  REP(i,N) {
   gets(buff);
   VS v = split2(string(buff), ' ');
   name[v[0]] = i;
   xx.PB(v[0]);
   FOR(i, 2, SIZE(v)-1) edge[v[0]].PB( v[i]);
  }
  RESET(vis,0); 
  RESET(deg, 0);

  //brut();
  printf("%d\n", go( xx[0] ) );
}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
