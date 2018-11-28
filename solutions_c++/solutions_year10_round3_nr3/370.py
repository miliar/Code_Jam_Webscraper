#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1E-9
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define RET return
#define CO(x) cout << x;
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))

#define VAR(a,T) __typeof(T) a=(T)
#define BEG(c) (c).begin()
#define BEGR(c) (c).rbegin()
#define END(c) (c).end()
#define ENDR(c) (c).rend()
#define ALL(c) BEG(c), END(c)
#define POS(c,x) ((c).find(x) != END(c))
#define CLR(c) memset(c, 0, sizeof(c))
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SSORT(c) stable_sort(ALL(c))
#define ZERO(i,v) (((i)<0)?(0):(v))
#define REP(i,e) for(int i = 0; i < (e); ++i)
#define REPD(i,e) for(int i = e-1; i >= 0; --i)
#define REPB(i,e) for(int i=0, b=1; i<(signed)(e); ++i, b<<=1)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)
#define TLE FORU(yy,0,1000000000) FORU(xx,0,1000000000) cout << "\n";
#define TCM template <class K,class V>
#define TCT template <class T>
#define V(T) vector<T>

typedef long long LL; typedef unsigned long long ULL; typedef long double LD;
typedef V(int) vi; typedef V(vi) vvi;
typedef V(char) vc; typedef V(vc) vvc;
typedef V(string) vs; typedef pair<int,int> pii;
typedef istringstream iss; typedef ostringstream oss;

const int INF = 2000000000; const LL INFLL = LL(INF) * LL(INF);

TCM void SMU (const map<K,V> &m) {VELU(it,m){CO(it->ST)CO(" ")CO(it->ND)NL}}
TCM void SMD (const map<K,V> &m) {VELD(it,m){CO(it->ST)CO(" ")CO(it->ND)NL}}
TCT void SS (const set<T> &s) {VELU(it,s){CO(*it)CO(" ")}NL}
TCT void SSP (const set<T> &s) {VELU(it,s){CO("("<<(it->ST)<<","<<(it->ND)<<")")}NL}
TCT void SV (const V(T) &v) {VELU(it,v){CO(*it)CO(" ")}NL}
TCT void SVS (const V(T) &v) {VELU(it,v){CO(*it)}NL}
TCT void SVV (const V(V(T)) &v) {VELU(it,v){SVS<T>(*it);}NL}

TCT bool OrdAsc (const T &a, const T &b) {return a < b;}
TCT bool OrdDes (const T &a, const T &b) {return a > b;}
TCT bool OrdXY (const T &a, const T &b) {if (a->x==b->x) RET a->y<b->y; RET a->x<b->x;}
TCT bool OrdYX (const T &a, const T &b) {if (a->y==b->y) RET a->x<b->x; RET a->y<b->y;}
TCT string t2s(T x) {ostringstream o; o << x; return o.str();}
TCT T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
TCT inline int size (const T&c) {return c.size();}

vs split (string s, string del = " ") { vs res;
  int ss = s.size(), sdel = del.size();
  for (int p = 0, q; p < ss; p = q+sdel) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
    if (q-p>0) res.push_back(s.substr(p,q-p));
  } return res;
}

int R,C;
int vis[512][512];
int smc[512][512];
map<int,int> res;

int big=0, by, bx;

void calc(vvi &B) {  
  REPD(r,R) {
    REPD(c,C) {
      if (!vis[r][c]) {
        if (r == R-1 || c == C-1) { smc[r][c] = 1; continue; }
        if (!vis[r+1][c+1]) {
          if (B[r][c] == B[r+1][c+1]) {        
            int a = smc[r+1][c+1]+1, av = 1, ah = 1;
            FORU(y,r+1,r+a-1) if (vis[y][c] || B[y][c] == B[y-1][c]) { break; } else { ++av; }
            FORU(x,c+1,c+a-1) if (vis[r][x] || B[r][x] == B[r][x-1]) { break; } else { ++ah; }               
            smc[r][c] = min(a, min(av,ah));
          } else smc[r][c] = 1;                          
        } else smc[r][c] = 1;     
      }
    }  
  }
    
  big = 0; by = -1; bx = -1;
  REP(r,R) { REP(c,C) {
    if (smc[r][c] > big) {
      big = smc[r][c];
      by = r; bx = c;
    }   
  }}
    
  //REP(r,R) { REP(c,C) { cout << smc[r][c]; } cout << endl; }
}

struct comp {
  bool operator () (const pii e1, const pii e2) {     
    if (e1.ST < e2.ST) return false;
    if (e1.ST > e2.ST) return true;    
    int y1 = e1.ND >> 12; int x1 = e1.ND & ((1<<12)-1);
    int y2 = e2.ND >> 12; int x2 = e2.ND & ((1<<12)-1);
    if (y1 < y2) return true;
    if (y1 > y2) return false;
    return x1 < x2;   
  }
};

int main() {

  int T;  
  string line;

  scanf("%d",&T); getline(cin, line);
  FORU(testcase,1,T) {
    scanf("%d %d\n",&R,&C); 
    res.clear(); CLR(vis); 
    vvi B(R,vi(C));    
    REP(i,R) {
      getline(cin, line);
      REP(j,C/4) {
        char ch = line[j]; int chi = 0;
        if ('A' <= ch && ch <= 'F') chi = 10+(ch-'A'); else chi = ch-'0';                
        if (chi & (1<<3)) B[i][j*4+0] = 1;
        if (chi & (1<<2)) B[i][j*4+1] = 1;
        if (chi & (1<<1)) B[i][j*4+2] = 1;
        if (chi & (1<<0)) B[i][j*4+3] = 1;       
      }
    }       
    
    int cut = 0; int cnt = 0;
    while (cut < R*C) {
      CLR(smc); calc(B);
      //cout << big << " " << by << " " << bx << endl;
      FORU(y,by,by+big-1) FORU(x,bx,bx+big-1) vis[y][x] = 1;
      cut += big*big;
      if (res.find(big) != END(res)) {
        res[big] += 1;
      } else {
        res.insert(MP(big,1));
      }
      //cnt += 1;
      //if (cnt == 20) break;
    }        
    
    printf("Case #%d: %d\n",testcase,res.size());
    SMD<int,int>(res);        
  }

  return 0;
}
