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

TCM void SM (const map<K,V> &m) {VELU(it,m){CO(it->ST)CO(": ")CO(it->ND)NL}NL}
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

int YL[1010];
int YR[1010];

int main() {

  int T,N;
  string line;

  scanf("%d",&T); getline(cin, line);
  FORU(testcase,1,T) {
    scanf("%d\n",&N);
    CLR(YL); CLR(YR);
    REP(i,N) scanf("%d %d\n",&YL[i],&YR[i]);
    int res = 0;
    
    REP(i,N) {     
     if (YL[i] < YR[i]) {
       REP(j,N) {
         if (j == i) continue;
         if (YL[j] > YL[i] && YR[j] < YR[i]) ++res;
       }       
     } else {
       REP(j,N) {
         if (j == i) continue;
         if (YL[j] < YL[i] && YR[j] > YR[i]) ++res;
       }       
     }          
    }    
    
    printf("Case #%d: %d\n",testcase,res/2);
  }

  return 0;
}
