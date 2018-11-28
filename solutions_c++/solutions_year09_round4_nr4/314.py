#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std; 

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define clr(a, v) memset((a), (v), sizeof(a))
#define forn(i, n) for (int i = 0; i < (n); ++i)

int x[32], y[32], r[32];
int n;

int main() {
 freopen("d.in", "r", stdin);
 freopen("d.out", "w", stdout);

 int nt; scanf("%d", &nt);

 for (int tc=1; tc<=nt; ++tc) {
  scanf("%d", &n);

  forn (i, n) scanf("%d %d %d", &x[i], &y[i], &r[i]);
  double res=1e10;

  if (n==1)
   res=r[0];
  if (n==2) {
   res=max(r[0], r[1]);
   
  } else {

  forn (i, n) forn (j, n) if (i!=j) forn (k, n) if (k!=i && k!=j) {   
   double d=hypot(1.0*x[i]-x[j], 1.0*y[i]-y[j]);   
   d+=r[i]+r[j];
   d*=0.5;   
   double cur=r[k];
   d=max(d, 1.0*r[i]);
   d=max(d, 1.0*r[j]);   
   res=min(res, max(d, cur));


  
  }
  }

 



  printf("Case #%d: %.8f\n", tc, res);



 }

 return 0;
}
