using namespace std;
 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define UNIQUE(x) x.erase(unique(ALL(x)),x.end())
#define REP(x, hi) for (int x=0; x<(hi); x++)
#define REPD(x, hi) for (int x=((hi)-1); x>=0; x--)
#define FOR(x, lo, hi) for (int x=(lo); x<(hi); x++)
#define FORD(x, lo, hi) for (int x=((hi)-1); x>=(lo); x--)
#define FORALL(it,x) for (typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<string> VS;

const int inf = 999999999;

/////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 16;

int Y,X;
int cache[1<<MAX][MAX][MAX];
VS m;

int go (int msk, int y, int x) {

  if (y>=Y) return 0;
  if (x>=X) return go(msk,y+1,0);
  
  int &res = cache[msk][y][x];
  if (res!=-1) return res;

  if (m[y][x]!='#') { // make 0
    int tmp=0;
    if (x>0 && (msk&(1<<(x-1)))) tmp++;
    if (y>0 && (msk&(1<<(x)))) tmp++;

    int nmsk = msk;
    if (nmsk & (1<<x)) nmsk ^= 1<<x;
    tmp += go(nmsk,y,x+1);

    res = max(res, tmp);
  }

  if (m[y][x]!='.') { // make 1
    int tmp=0;
    if (x==0 || (x>0 && !(msk&(1<<(x-1))))) tmp++;
    if (y==0 || (y>0 && !(msk&(1<<(x))))) tmp++;

    int nmsk = msk;
    if (!(nmsk & (1<<x))) nmsk ^= 1<<x;
    tmp += go(nmsk,y,x+1);

    res = max(res, tmp);
  }

  return res;    
}

void solve () {

  cin>>Y>>X;
  m=VS(Y);
  REP(y,Y) {
    cin>>m[y];
    m[y]+=".";
  }
  m.PB(string(X+1,'.'));
  X++;
  Y++;

  memset(cache,-1,sizeof(cache));
  cout<<go(0,0,0);
}

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    printf ("Case #%i: ",run);
    solve();
    printf ("\n");
  }

  return 0;
}
