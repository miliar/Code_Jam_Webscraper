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


class person {
public:
  int index, r;
  double x, y;
  bool operator< (const person &drugi) const {
    if (r == drugi.r) return index<drugi.index;
    else return r<drugi.r;
  }
};
  vector<person> a;

bool distOK(person a, person b) {
  return ((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) >= ((double)(a.r+b.r)*(a.r+b.r)));
}
  
vector<double> solve(){
  vector<double> ret;
  int n, w, l;
  scanf("%d %d %d ", &n, &w, &l);
  bool reversed = false;
  if (w<l) {
    reversed = true;
    swap(w,l);
  }
//  cout << w << " " << l << endl;
  ret.resize(2*n);
  a.resize(n);
  for(int i=0;i<n;i++) {
    scanf("%d ", &a[i].r);
    a[i].index=i;
    a[i].x = a[i].y = -1;
  }
  sort (a.begin(), a.end());
  reverse(a.begin(), a.end());
  a[0].x = a[0].y = 0;
  if (n>1) { a[1].x = w, a[1].y = l; }
  double nextx, nexty;
  if (n>2){
    nexty=0;
    nextx = a[0].r+a[2].r;
  }
  for (int i=2;i<n;i++) {
    bool allOK=true;
    a[i].x = nextx;
    a[i].y = nexty;
    for (int j=i-1;j>=0;j--) if (!distOK(a[i],a[j])) {
      allOK=false;/*
      cout << a[i].x << " " << a[i].y << " " << a[i].r << endl;
      cout << a[j].x << " " << a[j].y << " " << a[j].r << endl;
      */
    }
    if (allOK) continue;
    nextx +=a[i].r/10.0;
    if (nextx > w) {nextx = 0; nexty+=a[i].r/10.0;}
    if (nexty > l) break;
    i--;
  }
  
  for (int i=0;i<n;i++) {
    if (!reversed) {
      ret[2*a[i].index] = a[i].x;
      ret[2*a[i].index+1] = a[i].y;
    }
    else {
      ret[2*a[i].index+1] = a[i].x;
      ret[2*a[i].index] = a[i].y;    
    }
  }

  return ret;
}


int main() {

  int _n=0;
  scanf("%d ", &_n);
  vector<vector<double> > sols;
  
  for (int i=0;i<_n;i++) {
    sols.push_back(solve());
  }
  for (int i=0;i<sz(sols);i++) {
    printf("Case #%d:", i+1);
    for (int j=0;j<sz(sols[i]);j++) printf(" %0.8lf", sols[i][j]);
    printf("\n");
  }

  return 0;

}