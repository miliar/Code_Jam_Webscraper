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

vector<int> primes;
const int mxn = 1<<20;
bool sv[mxn];
int vis[mxn], vid;

inline void prec() {
  for (int i=2; i < mxn; i++)
  if (!sv[i]) {
    primes.pb( i );
    for (int j=2*i; j < mxn; j += i)
      sv[j] = 1;
  }
}
ll n;
int cnt = 0;
ll go(ll p, int pos, int parity) {
  if (p > n || pos < 0) {
    ll ret = n/p;
    if (parity)
      ret = -ret;
    //cout << "ha " << ret << " " << n << " / " << p << endl;
    if (++cnt % 10000 == 0) {
      cout<< cnt << endl;
    }
    return ret;
  }
  return go(p, pos-1, parity) + go(p*primes[pos], pos-1, parity^1);
} 

int main(int argc, char** argv) {
  //sim();
  prec();
  //freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out2", "w", stdout);
  //freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out2", "w", stdout);
  //freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
  
  freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
  int T;
  cin>>T;
  for (int cs=1; cs <= T; cs++) {
    cin>>n;
    int pos = 0;
    ll powerSum = 0;
    while (pos < primes.size() && primes[pos]*(ll)primes[pos] <= n) {
      ll tmp = n;
      while (tmp/primes[pos]) {
        tmp /= primes[pos];
        powerSum++;
      }
      pos++;  
    }
    //ll otherPrimes = go(1, pos-1, 0);
    ll mn = pos + 1 ;
    ll mx = powerSum + 2;
    
    
    printf("Case #%d: %lld\n", cs, n == 1 ? 0 : mx - mn);
  }
}
