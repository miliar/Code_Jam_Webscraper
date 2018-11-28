#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>
 
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<climits>
 
#define oo            (int)13e7
#define s(n)          scanf("%d",&n)
#define sl(n)         scanf("%lld",&n)
#define sf(n)         scanf("%lf",&n)
#define fill(a,v)     memset(a, v, sizeof a)
#define ull           unsigned long long
#define ll            long long
#define bitcount      __builtin_popcount
#define all(x)        x.begin(), x.end()
#define pb( z )       push_back( z )
#define gcd           __gcd
using namespace std;

#define ld long double
int c, d;
const int mxn = 1<<20;
int p[256], v[256];
int pos[mxn];
int main(int argc, char** argv) {
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
  //freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
  //freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
  
  freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
  
  int runs; s(runs);
  for (int T=1; T <= runs; T++) {
    s(c); s(d);
    ll vsum = 0;
    int ptr = 0;
    for (int i=0; i < c; i++) {
      s(p[i]);
      s(v[i]);
      vsum += v[i];
      for (int j=0; j < v[i]; j++)
        pos[ptr++] = p[i];
    }
    //cout << ptr << endl;
   // for (int i=0; i < ptr; i++) cout << pos[i] << " "; cout<<endl;
    ld lo = 0, hi = ptr * (1.0) * d + 1e9;
    for (int its=0; its < 100; its++) {
      ld mid = (lo+hi)/2;
      ld prev = pos[0] - mid;
      bool good = 1;
      
      for (int p=1; p < ptr; p++) {
        ld greaterThan = prev + d;
        ld reachLeft = pos[p] - mid;
        ld reachRight = pos[p] + mid;
        ld pos = 0;
        if (greaterThan < reachLeft) {
          pos = reachLeft;
        } else if (greaterThan < reachRight) {
          pos = greaterThan;
        } else {
          good = 0;
          break;
        }
        prev = pos;
      } 
      if (good) {
        hi = mid;
      } else {
        lo = mid;
      }
    }
    printf("Case #%d: %.10lf\n", T, (double)(lo+hi)/2);
  }
	return 0;
}
