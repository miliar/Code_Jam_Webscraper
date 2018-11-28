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
    printf("Case #%d:\n",Case+1);

    static char v[128][128];
    int n; cin >> n;
    REP(i,n) REP(j,n) cin >> v[i][j];
    vector<double> wp(n), owp(n), oowp(n), rpi(n);

    REP(i,n){
      int a = 0, s = 0;
      REP(j,n){ if(isdigit(v[i][j])) s++; if(v[i][j]=='1') a++; }
      wp[i] = (double) a / s;
    }

    REP(i,n){
      owp[i] = 0;
      int cnt = 0;
      REP(j,n) if(i!=j && isdigit(v[i][j])){
        int a = 0, s = 0;
        REP(k,n) if(i!=k){
          if(isdigit(v[j][k])) s++;
          if(v[j][k]=='1') a++;
        }
        owp[i] += (double) a / s;
        cnt++;
      }
      owp[i] /= cnt;
    }

    REP(i,n){
      double s = 0; int cnt = 0;
      REP(j,n) if(isdigit(v[i][j])) s+=owp[j], cnt++;
      oowp[i] = s / cnt;
    }
    
    REP(i,n){
      rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
    }
    

    // pp(wp);
    // pp(owp);
    // pp(oowp);
    // pp(rpi);
    
    REP(i,n) printf("%.12lf\n",rpi[i]);
  }
}
