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

const int mxn = 10007;
ll d[mxn], l[mxn];
ll maxRight[mxn];
bool dp[mxn];
int n, D;

int main(int argc, char** argv) {
	
  int runs; s(runs);
  for (int C=1; C <= runs; C++) {
    s(n);
    for (int i=0; i < n; i++) {
      sl(d[i]); sl(l[i]);
    }
    s(D);
    fill(maxRight, 0);
    maxRight[0] = d[0] + min(d[0], l[0]);
    bool yes = 0;
    for (int p=0; p < n; p++) {
      for (int np=p+1; np < n; np++) {
        if (maxRight[p] >= d[np]) {
          ll diff = d[np] - d[p];
          maxRight[np] = max(maxRight[np], min(l[np], diff) + d[np]);
        } else {
          break;
        }
      }
      if (maxRight[p] >= D) {
        yes = 1; break; 
      }
    }
    printf("Case #%d: %s\n", C, yes ? "YES" : "NO");
  }
	return 0;
}
