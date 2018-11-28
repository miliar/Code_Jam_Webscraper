#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define Int signed long long int  /* 64b unix : %lld , %llu  */
// #define Int __int64            /* 64b win  : %I64d, %I64u */

#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf('\n');
#define SI size()
#define RET return
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))

#define VAR(a,T) typeof(T) a=(T)
#define BEG(c) (c).begin()
#define BEGR(c) (c).rbegin()
#define END(c) (c).end()
#define ENDR(c) (c).rend()
#define ALL(c) (c).begin(), (c).end()
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SSORT(c) stable_sort(ALL(c))
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)

#define EPS 1E-9
#define INF 1000000000
#define MOD (INF-401)
#define MOD_1 (MOD-1)
#define E  2.71828182845904523536028747135266249
#define PI 3.14159265358979323846264338327950288

typedef pair<int,int> pii;
typedef pair<Int,Int> pII;
typedef istringstream iss;
typedef ostringstream oss;
typedef vector<int>    vi;
typedef vector<vi>    vvi;
typedef vector<Int>    vI;
typedef vector<vI>    vvI;
typedef vector<string> vs;

inline   long gcd (long a, long b) { return (!b)?a:gcd(b,a%b); }
inline   long lcm (long a, long b) { return b*a/gcd(a,b); }
inline double lg2 (double a) { return log(a)/M_LN2; }
inline   long nCk (long n, long k) { long res=1; if (k<0||k>n) RET 0; FORU(i,1,min(k,n-k)) {res*=n-i+1; res/=i;} RET res; }
inline   long sgn (long n) { return (n>0)?1:((n<0)?-1:0); }

vs split (string s, string del = " ") { vs res;
  for (int p = 0, q; p < (signed)s.SI; p = q+del.SI) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = s.SI;
    if (q-p>0) res.PB(s.substr(p,q-p));
  } RET res;
}

#define DEBUG 1
#define MAX 1000

struct node {
  bool isLeaf;
  bool val;
  int gate; // 0-OR, 1-AND
  int chng; // 0-not, 1-is changeable

};

node BT [11111];
 int OG [11111];

bool value (int n) {
  if (!BT[n].isLeaf) {
    bool l = value(n<<1);
    bool r = value((n<<1)+1);
    if (BT[n].gate == 0) {
      BT[n].val = l|r;
    } else {
      BT[n].val = l&r;
    }
  }
  return BT[n].val;
}

int main () {

  int N;
  int M, V;
  int G, C;
  int val;

  scanf("%d\n",&N);
  FORU(i,0,N-1) {
    scanf("%d %d\n",&M,&V);
    FORU(j,1,(M-1)/2) {
      scanf("%d %d\n",&G,&C);
      BT[j].isLeaf = false;
      BT[j].gate = G;
      BT[j].chng = C;
      OG[j] = G;
    }
    FORU(j,(M-1)/2+1,M) {
      scanf("%d\n",&val);
      BT[j].isLeaf = true;
      BT[j].val = val;
    }

    int minFlips = INF;
    FORU(mask,0,(1<<((M-1)/2))-1) {
      FORU(j,1,(M-1)/2) {
        if (BT[j].chng == 1) {
          if (mask&(1<<(j-1))) {
            BT[j].gate = 1-BT[j].gate;
          }
        }
      }
      
      if (value(1) == (int)V) {
        int ones = 0;
        int tmp = mask;
        while (tmp) {
          if (tmp&1) ++ones;
          tmp >>= 1;
        }
        minFlips = min(minFlips, ones);
      }
      FORU(j,1,(M-1)/2) BT[j].gate = OG[j];
    }

    if (minFlips==INF) printf ("Case #%d: IMPOSSIBLE\n",i+1);
    else printf ("Case #%d: %d\n",i+1,minFlips);
  }

  return 0;
}
