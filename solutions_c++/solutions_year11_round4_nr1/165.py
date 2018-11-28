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

const int mxn = 1024;
int B[mxn], E[mxn], w[mxn];

int X, S, R, t, N;
struct segment {
  int start, end, increase;
  segment(int _s, int _e, int _i) {
    start = _s;
    end = _e;
    increase = _i;
  }
  
  bool operator < (const segment& s) const {
    return increase > s.increase;
  }
};
int main(int argc, char** argv) {
  //freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
  //freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
  //freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
  
  freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
  
  int T;
  s(T);
  for (int cs=1; cs <= T; cs++) {
    
    cin>>X>>S>>R>>t>>N;
    priority_queue< segment > parts;
    int prevEnd = 0;
    for (int i=0; i < N; i++) {
      cin>>B[i]>>E[i]>>w[i];
      if (B[i] > prevEnd) {
        parts.push( segment( prevEnd, B[i], 0 ) );
      }
      parts.push( segment( B[i], E[i], w[i] ) );
      prevEnd = E[i];
    }
    if (prevEnd < X)
      parts.push( segment(prevEnd, X, 0) );
    //sort( all(parts) );
    double left = t;
    double total = 0;
    while (parts.size() > 0) {
      segment p = parts.top(); parts.pop();
      double dist = (p.end - p.start + 0.);
      double Trun = min(left,  dist / ( R + p.increase ));
      double runDist = Trun * ( R + p.increase );
      double walkDist = dist - runDist;
      double Twalk = walkDist / ( S + p.increase );
      
     // cout << p.start << " to " << p.end << " "  << runDist << " " << walkDist <<" " << Trun << " " << Twalk << endl;
      total += Trun + Twalk;
      left -= Trun;
    }
    printf("Case #%d: %.10lf\n", cs, total); 
  }
  
	return 0;
}
