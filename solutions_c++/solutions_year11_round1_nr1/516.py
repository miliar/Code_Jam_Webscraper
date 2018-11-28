//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl; 
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

int t;
long long int n,pd,pg;
int ok = 1,krot;
int main() {
  scanf("%d",&t);
  FOR(i, 1, t) {
    ok = 0;
    scanf("%lld %lld %lld",&n,&pd,&pg);
    if(pg == 100 && pd < 100) ok = 0;
    else if(pg == 0 && pd > 0) ok = 0;
    else {
      if(n >= 100) ok = 1;
      else {
	FOR(j, 1, n) {
	  if( (pd * j) % 100 == 0) ok = 1;
	}
      }
    }
    if(ok) printf("Case #%d: Possible\n",i);
    else printf("Case #%d: Broken\n",i);

    
  }

  return 0;
}
