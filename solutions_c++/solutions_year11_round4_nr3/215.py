#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;
#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FCC(i,a,b) for(int i=a,_b=b;i<=_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ROF(i,n) for(int i=n-1;i>=0;--i)
#define SZ(v) (signed(v.size()))
#define FOZ(i,v) FOR(i,SZ(v))
#define ALL(s) s.begin(),s.end()
#define LET(a,b) typeof(b) a=b
#define FOREACH(it,s) for(LET(it,s.begin());it!=s.end();++it)

typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define D(A) A

const int INF = 2000000000;
typedef long long ll;
typedef long double ld;
const ld FINF = 1e8;
const ld eps = 1e-9;

const int MAX = 1000000;
bool isp[MAX];
ll primes[MAX];
int nprimes = 0;


int main() {
  FCO(i,2,MAX) isp[i] = true;
  FCO(i,2,MAX) if(isp[i]) {
    primes[nprimes++] = i;
    for(ll j=ll(i)*i; j<MAX; j+=i) isp[j] = false;
  }

  int ncases; scanf("%d", &ncases);
  FOR(casenum, ncases) {
    ll ans = 0;
    ll N; cin>>N;
    //cerr<<N<<endl;
    FOR(i,nprimes) {
      ll p = primes[i];
      if(p*p>N) break;
      ll n = N;
      ll k = 0;
      while(n>=p) {
        n/=p;
        ++k;
      }
      if(k!=0) {
        //cerr<<"For prime "<<p<<" power is "<<k<<endl;
        ans += k - 1;
      }
    }
    if(N>1) ans += 1;
    printf("Case #%d: %Ld\n", casenum+1, ans);
  }
  return 0;
}
