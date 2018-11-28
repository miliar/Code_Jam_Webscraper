#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define maxn 128
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

#define offset 10000
#define zero(x) (fabs(x)<eps)
#define x real()
#define y imag()
typedef complex<double> point;
double cp(point a,point b) {
  return a.x*b.y-a.y*b.x;
}
int dots_inline(point p1,point p2,point p3){
  return zero(cp(p1-p3,p2-p3));
}
int dot_online_in(point p,point l1,point l2){
  return zero(cp(p-l1,p-l2))&&(l1.x-p.x)*(l2.x-p.x)<eps&&
    (l1.y-p.y)*(l2.y-p.y)<eps;
}
int same_side(point p1,point p2,point l1,point l2){
  return cp(l1-l2,p1-l2)*cp(l1-l2,p2-l2)>eps;
}
int intersect_in(point u1,point u2,point v1,point v2){
  if (!dots_inline(u1,u2,v1)||!dots_inline(u1,u2,v2))
    return !same_side(u1,u2,v1,v2)&&!same_side(v1,v2,u1,u2);
  return dot_online_in(u1,v1,v2)||dot_online_in(u2,v1,v2)||
    dot_online_in(v1,u1,u2)||dot_online_in(v2,u1,u2);
}

int n;
point P[maxn];
double R[maxn];

double solve() {
  if(n==1) return R[0];
  if(n==2) return max(R[0],R[1]);
  if(n==3) {
    double sol = inf;
    REP(i,n) FOR(j,i+1,n-1) {
      int k;
      for(k=0;k<n;k++) if(k!=i&&k!=j) break;
      double r1 = (abs(P[i]-P[j])+R[i]+R[j])/2;
      sol <?= max(r1,R[k]);
    }
    return sol;
  }
  else return inf;
}

int main() {
  int T;
  cin>>T;
  FOR(K,1,T) {
    cin>>n;
    REP(i,n) {
      double xx,yy;
      cin>>xx>>yy>>R[i];
      P[i]=point(xx,yy);
    }
    cout << "Case #"<<K<<": "<<solve()<<endl;
  }
}
