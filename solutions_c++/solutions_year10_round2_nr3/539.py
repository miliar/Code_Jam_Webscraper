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
#define REPB(i,e) for(int i=0, b=1; i<(signed)(e); ++i, b<<=1)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)
#define TLE FORU(yy,0,1000000000) FORU(xx,0,1000000000) cout << "\n";
#define TCT template <class T>

typedef long long LL; typedef unsigned long long ULL; typedef long double LD;
typedef vector<int> vi; typedef vector<vi> vvi;
typedef vector<string> vs; typedef pair<int,int> pii;

const int INF = 2000000000; const LL INFLL = LL(INF) * LL(INF);

TCT bool OrdAsc (const T &a, const T &b) {return a < b;}
TCT bool OrdDes (const T &a, const T &b) {return a > b;}
TCT bool OrdXY (const T &a, const T &b) {if (a->x==b->x) RET a->y<b->y; RET a->x<b->x;}
TCT bool OrdYX (const T &a, const T &b) {if (a->y==b->y) RET a->x<b->x; RET a->y<b->y;}
TCT string t2s(T x) {ostringstream o; o << x; return o.str();}
TCT T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
TCT inline int size (const T&c) {return c.size();}

#define MOD (100003)

string i2bs (unsigned long n, long b=32) {
  string res = "00000000000000000000000000000000";
  int c = b; --b;
  while (n) {res[b] += (n&1); --b; n >>= 1;}
  return res.substr(0,c);
}

int N;

bool check(int set, int num) {    
  if (num == 1) return true;
  int rank = 0;
  FORU(i,2,num) {
    if (set & 1<<(i-1)) ++rank;  
  }       
  if (!(set & 1<<(rank-1))) return false;     
  return check(set,rank);    
}

int main() {

  int T;
  string line;

  scanf("%d",&T); getline(cin, line);
  FORU(testcase,1,T) {
    scanf("%d",&N); int res = 0;
    LL S = 0;
    
    FORU(i,1,(1<<N)-1) {      
      if ((i & (1<<(N-1))) && (i&1)) {
        // cout << i2bs(i) << endl;
        if (check(i,N)) {                  
          ++res;        
        }
      }
      res %= MOD;
    }     
    
    printf("Case #%d: %d\n",testcase,res);
  }

  return 0;
}
