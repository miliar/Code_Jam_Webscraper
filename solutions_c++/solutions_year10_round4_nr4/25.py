#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

typedef long double ld;
inline ld sqr(ld a){return a*a;}
inline ld root(ld a){return a>0?sqrt(a):0;}
inline ld area(ld r,ld x){
  ld ans=0.0;
  bool inv=0;
  if (x>=r){
    x=2*r-x;
    inv=1;
  }
  x=r-x;
  ld y=root(sqr(r)-sqr(x)),a=acos(x/r);
  ans=a*sqr(r)-x*y;
  return inv?M_PI*sqr(r)-ans:ans;
}
#define EPS 1e-8
inline ld two(ld p,ld q,ld y){
  if(p<q)swap(p,q);
  if (y+EPS>p+q) return 0.0;
  if (y+q<p+EPS) return M_PI*sqr(q);
  ld t=(sqr(p)+sqr(y)-sqr(q))/2/y;  
  return area(p,p-t)+area(q,t-(y-q));
}

#define INF 1000000000
int N,M,x[5010],y[5010],sx[5010],sy[5010];
double r[5010];
double calc(int sx,int sy){
  FOR(i,N)r[i]=root(sqr(x[i]-sx)+sqr(y[i]-sy));
  if(N==2)return two(r[0],r[1],root(sqr(x[0]-x[1])+sqr(y[0]-y[1])));
  assert(0);
}
main(){
  int C;cin>>C;
  for(int z=1;z<=C;z++){
    cin>>N>>M;
    FOR(i,N)cin>>x[i]>>y[i];
    FOR(i,M)cin>>sx[i]>>sy[i];
    printf("Case #%d:",z);
    FOR(i,M)printf(" %.8lf",calc(sx[i],sy[i]));
    puts("");
  }
}
