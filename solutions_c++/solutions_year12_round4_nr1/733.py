#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
#define sz(X) ((int)(X).size())
#define FOREACH(i,c) for( c.begin()::typeid i=(c.begin());i!=(c).end();++i)
#define IN(_lower,_variable,_higher) (((_lower)<=(_variable)) && ((_variable)<=(_higher)))
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORU(v,p,k) for(int v=p;v<k;++v)
#define FORD(v,p,k) for(int v=(p)-1;v>=k;--v)
#define FORLLU(v,p,k) for(LL v=p;v<k;++v)
#define FORLLD(v,p,k) for(LL v=(p)-1;v>=k;--v)
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
#define junik(X) {sort( (X).begin(), (X).end() ); (X).erase( unique( (X).begin(), (X).end() ), (X).end() ); }
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))


class vine {
  public:
  int d, l;
  bool operator<(const vine &drugi) const {
    if (d<drugi.d) return true;
    if (d>drugi.d) return false;
    return l<drugi.l;
  }
};

vector<vine> a;
int d[10000];
bool solve() {
  int n;
  a.clear();
  memset(d,0, sizeof(d));
  
  scanf("%d ", &n); 
  a.resize(n);
  for (int i=0;i<n;i++) {
    scanf("%d %d ", &a[i].d, &a[i].l );
  } 
  int goal=0;
  scanf("%d ", &goal);
  

//  cout << endl;

  d[0]=a[0].d;
  for (int i=0;i<n;i++) {
//    cout << d [i] << endl;
    for (int j=i+1;j<n;j++) {
      if (d[i]+a[i].d<a[j].d) break;
//      cout << i << " " << d[i] << " " <<a[i].d << " " <<a[i].l << endl;
//      cout << j << " " << d[j] << " " << a[j].d << " " << a[j].l << endl;
      d[j]=max(d[j], min(a[j].l, (a[j].d-a[i].d)));
//      cout << " --> " << d[j] << endl;
    }
    if (d[i] + a[i].d>=goal) return true;
  }
  
  
  return false;
}

int main() {

  int _n=0;
  scanf("%d ", &_n);
  vector<bool> sols;
  
  for (int i=0;i<_n;i++) {
    sols.push_back(solve());
  }
  for (int i=0;i<sz(sols);i++) {
    printf("Case #%d: %s\n", i+1, (sols[i])?"YES":"NO");
  }

  return 0;

}