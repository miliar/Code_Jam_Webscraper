#define _GLIBCXX_DEBUG_ 1

#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>
#include <complex>

#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cstring>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
#define FOR(i,b,e) for(int i=(int)(b);i<(int)(e);i++)
#define ALL(c) (c).begin(), (c).end()
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define RALL(c) (c).rbegin(), (c).rend()
#define ALLA(a,n) ((a)+0), ((a)+n)

using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<long long> vll;
typedef vector<string> vstring;
typedef vector<double> vdouble;

template<class T>void pp(T v,int n){ REP(i,n)cout<<v[i]<< ' ' ; cout << endl; }
template<class T>void pp(T v){ EACH(it,v) cout << *it << ' ' ; cout << endl;  }
template<class T>T& ls(T& a,T b){ if(b<a) a=b; return a; }
template<class T>T& gs(T& a,T b){ if(b>a) a=b; return a; }
inline ll to_i(const string& s){ll n;sscanf(s.c_str(),"%lld",&n);return n;}
inline string to_s(ll n){char buf[32];sprintf(buf,"%lld",n);return string(buf);}

struct __scanner__{ bool e; operator bool(){ return e; } } IN = { false };
inline __scanner__& operator>>(__scanner__& in,int &n)
{ in.e = scanf("%d",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,ll &n)
{ in.e = scanf("%lld",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,double &n)
{ in.e = scanf("%lf",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,char &n)
{ in.e = scanf(" %c",&n)==1; return in; }
inline __scanner__& operator>>(__scanner__& in,string &n) // BUFFER SIZE!
{ static char buf[1000000]; in.e = scanf(" %s",buf)==1; n = buf; return in; } 

int main(){
  int C; cin >> C;
  REP(Case,C){
    int d, c, n;
    vint v;
    cin >> c >> d;
    REP(i,c){
      int a,b; cin >> a >> b;
      REP(j,b) v.push_back(a);
    }
    n = v.size();
    
    double lb = 0, ub = 1e9;
    REP(iter,100){
      double m = (lb + ub) / 2;
      double p = -1e10;
      bool ok = true;

      REP(i,n){
        double l = v[i] - m, r = v[i] + m;
        if(r < p){ ok = false; break; }
        p = max(p, l) + d;
      }

      if(ok) ub = m; else lb = m;
    }
    
    printf("Case #%d: %.12lf\n",Case+1, ub);
  }
}
