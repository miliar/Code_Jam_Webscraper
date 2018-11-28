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

typedef pair<int,int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef vector<int>    VI;
typedef vector<string> VS;

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
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SSORT(c) stable_sort(ALL(c))
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)

#define dlong signed long long int  /* 64b for unix    : %lld , %llu  */
// #define dlong __int64            /* 64b for windows : %I64d, %I64u */

#define EPS 1E-9
#define INF 10^9
#define MOD (INF-401)
#define MOD_1 (MOD-1)
#define E  2.71828182845904523536028747135266249
#define PI 3.14159265358979323846264338327950288

inline   long gcd (long a, long b) { return (!b)?a:gcd(b,a%b); }
inline   long lcm (long a, long b) { return b*a/gcd(a,b); }
inline double lg2 (double a) { return log(a)/M_LN2; }
inline   long nCk (long n, long k) { long res=1; if (k<0||k>n) RET 0; FORU(i,1,min(k,n-k)) {res*=n-i+1; res/=i;} RET res; }
inline   long sgn (long n) { return (n>0)?1:((n<0)?-1:0); }

VS split (string s, string del = " ") {
  VS res;
  for (int p = 0, q; p < (signed)s.SI; p = q+del.SI) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = s.SI;
    if (q-p>0) res.PB(s.substr(p,q-p));
  } RET res;
}

int N;
int P, K, L;
vector<int> F;

int main () {
  
  int tmp = 0;

  scanf("%d\n",&N);
  FORU(i,0,N-1) {
    scanf("%d %d %d\n",&P,&K,&L);
    F.clear(); FORU(j,0,L-1) { scanf("%d\n",&tmp); F.PB(tmp); } SORT(F); REVERSE(F);    

    dlong lvl = 1;
    dlong res = 0;

    while (F[0] > 0) {
      int j = 0, k = K;
      while (F[j] > 0 && k > 0) {
        res += F[j]*lvl;
        F[j] = -1;
        ++j;
        --k;
      }
      SORT(F);
      REVERSE(F);
      ++lvl;
    }

    printf ("Case #%d: %I64d\n",i+1,res);
  }

  return 0;
}
