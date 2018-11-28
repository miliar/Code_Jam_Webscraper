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



const int N = 2000;
double L,W,x[N],y[N],r[N];
const double eps = 1e-3;


void place(int k)
{
  bool ok = false;
  while(!ok)
  {
    ok = true;
    x[k] = (rand()|(rand()<<15)) / RAND_MAX *W / RAND_MAX;
    y[k] = (rand()|(rand()<<15)) / RAND_MAX *L / RAND_MAX;

    forn(i,k)
      if((x[i]-x[k])*(x[i]-x[k]) + (y[i]-y[k])*(y[i]-y[k]) < (r[i] + r[k])*(r[i] + r[k])*(1+eps))
      {
        ok = false;
        break;
      }
  } 
}
 
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
  for(int test=1;test<=TESTS;test++)
  {
  	int n,w,l;
  	scanf("%d%d%d",&n,&w,&l);
  	W = w, L = l;
  	forn(i,n)     
  	{
  	  int R;
  	  scanf("%d",&R);
  	  r[i] = R;
  	}
  	forn(i,n)
  	  place(i);

  	forn(i,n) 
  	  forn(j,i)
  	    assert((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) > (r[i] + r[j])*(r[i] + r[j])*(1+eps));
  	   
    printf("Case #%d: ",test);
    forn(i,n)
      printf("%.6lf %.6lf ",x[i],y[i]);
    puts("");
  }
  return 0;
}