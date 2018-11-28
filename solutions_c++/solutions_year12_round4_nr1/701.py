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
#define ibits(x) __builtin_popcount(x)
#define lbits(x) __builtin_popcountll(x)
#define mp make_pair
#define pb push_back
#define sz(a) ((int)((a).size()))
#define X first
#define Y second

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> ii;
/*-----------TEMPLATE---------------*/


const int N = (int)1e5;
int d[N],l[N],m[N],D,n;
bool can[N];
int main() 
{
  srand(time(NULL));
  #define TASK ""
  #ifdef HOME
  assert(freopen(TASK "in", "rt", stdin));
  assert(freopen(TASK "out", "wt", stdout));
  #endif
  int TESTS;
  scanf("%d",&TESTS);
  for(int test=0;test<TESTS;test++)
  {  
    scanf("%d",&n);
//    eprintf("%d\n",test);
    forn(i,n)
      scanf("%d %d",&d[i],&l[i]);
    scanf("%d",&D);
    d[n] = D;
    l[n] = 0;

    memset(can,0,sizeof can);
    memset(m,0,sizeof m);
    m[0] = d[0];
    can[0] = true;
    forn(i,n)
    {
      if(can[i])
      { 
//        eprintf("%d %d\n",i,m[i]);
        for(int j=i+1;j<=n && (d[i] + m[i] >= d[j]);j++)
        {
          can[j] = true;
          m[j] = min(l[j],max(m[j],d[j] - d[i]));
        }
        if (can[n]) 
          break;
      }
    }

    printf("Case #%d: ",test+1);
    if (can[n]) 
      puts("YES");
    else
      puts("NO");
  }
  return 0;
}