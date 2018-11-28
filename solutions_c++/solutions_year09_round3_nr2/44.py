#include <iostream>
#include <algorithm>
#include <set>
#include <sstream>
#include <cmath>
using namespace std;

#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ALL(s) s.begin(),s.end()
#define SZ(s) signed(s.size())
#define MP make_pair
typedef pair<int,int> PII;
typedef pair<int,char> PIC;
const int INF = 2000000000;

typedef long double ld;
typedef long long ll;

#define D(A) A

int main() {
  int ncases; scanf("%d", &ncases);
  FOR(casenum,ncases) {
    int N; cin>>N;
    ll r[3], v[3]; FOR(j,3) r[j]=v[j]=0;
    FOR(i,N) {
      FOR(j,3) { int x; cin>>x; r[j]+=x; }
      FOR(j,3) { int x; cin>>x; v[j]+=x; }
    }

    ld anst=0;
    ll t=0; FOR(j,3) t-=r[j]*v[j];
    ll V=0; FOR(j,3) V+=v[j]*v[j];
    if(t<=0 or V==0) anst=0;
    else anst = ld(t)/ld(V);

    ld s[3]; FOR(j,3) s[j] = ld(r[j] + v[j]*anst)/N;
    ld ansd = 0; FOR(j,3) ansd += s[j]*s[j];
    ansd = sqrtl(ansd);
    printf("Case #%d: %.8Lf %.8Lf\n", casenum+1, ansd, anst);
  }
  return 0;
}
