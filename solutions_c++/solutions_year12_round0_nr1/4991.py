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


char s[6][1000];
char q[50][1000];
int p[40];
map<char,char>f;
map<char,bool>was;
int main() 
{
  srand(time(NULL));
  #define TASK ""
  #ifdef HOME
  assert(freopen(TASK "in", "rt", stdin));
  assert(freopen(TASK "out", "wt", stdout));
  #endif
f[' ']=' ';f['a']='y';f['b']='h';f['c']='e';f['d']='s';f['e']='o';f['f']='c';f['g']='v';f['h']='x';f['i']='d';f['j']='u';f['k']='i';f['l']='g';f['m']='l';f['n']='b';f['o']='k';f['p']='r';f['q']='z';f['r']='t';f['s']='n';f['t']='w';f['u']='j';f['v']='p';f['w']='f';f['x']='m';f['y']='a';f['z']='q';
  int T;
  scanf("%d ",&T);
  forn(t,T)
  {
    gets(q[t]);
    printf("Case #%d: ",t+1);
    forn(i,strlen(q[t]))
    {
      printf("%c",(char)f[q[t][i]]);
    }
    puts("");
  }
  return 0;
}