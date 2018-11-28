#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>

#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cstring>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
#define FOR(i,b,e) for(int i=(int)(b);i<(int)(e);i++)
#define FORC(i,b,e,c) for(int i=(int)(b);i<(int)(e)&&(c);i++)
#define ALL(c) (c).begin(), (c).end()
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<long long> vll;
typedef vector<string> vstring;
typedef vector<double> vdouble;

template<class T>void pp(T v,int n){ REP(i,n)cout<<v[i]<< ' ' ; cout << endl;}
template<class T>void pp(T v){ EACH(it,v) cout << *it << ' ' ; cout << endl; }
template<class T>T& ls(T& a,T b){ if(b<a) a=b; return a;}
template<class T>T& gs(T& a,T b){ if(b>a) a=b; return a;}

struct cir{ double x,y,r; };

double calc(cir a,cir b){
  a.x-=b.x; a.y-=b.y;
  return sqrt(a.x*a.x + a.y*a.y) + a.r + b.r;
}

double compute(vector<cir> &v){
  const int n=v.size();
  if(n==1) return v[0].r;
  if(n==2) return max(v[0].r, v[1].r);
  double a=max(v[0].r, calc(v[1],v[2])/2);
  double b=max(v[1].r, calc(v[2],v[0])/2);
  double c=max(v[2].r, calc(v[0],v[1])/2);
  return min(a,min(b,c));
}

int main(){
  int C; cin >> C;
  REP(CC,C){
    int n; cin >> n;
    vector<cir> v(n);
    REP(i,n) cin >> v[i].x >> v[i].y >> v[i].r;
    
    double result=compute(v);
    printf("Case #%d: %.12lf\n",CC+1, result);
  }
}
