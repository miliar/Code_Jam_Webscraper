/*-----------TEMPLATE---------------*/
//#pragma comment(linker, "/STACK:16777216")

#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdarg>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <functional>
#include <iterator>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define eprintf(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define forab(i, a, b) for (int i = (int)(a); i < ((int)(b)); ++i)
#define forit(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define forn(i, n) for (int i = 0; i < ((int)(n)); ++i)
#define forabok(i, a, b, ok) for (int i = (int)(a); i < ((int)(b)) && (ok); ++i)
#define foritok(it, v, ok) for (typeof((v).begin()) it = (v).begin(); it != (v).end() && (ok); ++it)
#define fornok(i, n, ok) for (int i = 0; i < ((int)(n)) && (ok); ++i)
#define mp make_pair
#define pb push_back
#define sz(a) ((int)((a).size()))
#define X first
#define Y second
#define ibits(x) __builtin_popcount(x)
#define lbits(x) __builtin_popcountll(x)

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> ii;
/*-----------TEMPLATE---------------*/


int main() 
{
  srand(time(NULL));
  #define TASK ""
  #ifdef HOME
  assert(freopen(TASK "in", "rt", stdin));
  assert(freopen(TASK "out", "wt", stdout));
  #endif
  int T;
  scanf("%d",&T);
  forn(t,T)
  {
    int n,s,p;
    scanf("%d%d%d",&n,&s,&p);
    int ans = 0;
    for(int i=0;i<n;i++)
    {
      int t;
      scanf("%d",&t);
      if (t % 3 == 0)
      {
        int x = t/3;
        // x + x + x  // x-1 + x + x+1
        if (x >= p)
          ans++;
        else if (x-1 >=0 && x+1 <= 10 && x+1 == p && s>0)
        {
          s--;
          ans++;
        }
      } 

      if (t % 3 == 1)
      {
        int x = t/3;
        // x + x + x+1  // x-1 + x+1 + x+1
        if (x+1 >= p)
          ans++;
      } 

      if (t % 3 == 2)
      {
        int x = t/3;
        // x + x + x+2  // x + x+1 + x+1
        if (x+1 >= p)
          ans++;
        else if (x+2 <= 10 && x+2 == p && s>0)
        {
          s--;
          ans++;
        }
      } 
      
    }

    printf("Case #%d: %d\n",t+1,ans);    
  }
  return 0;
}