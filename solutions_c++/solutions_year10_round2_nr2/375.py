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
#define ALL(c) (c).begin(), (c).end()
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEFOP(T,O,E)    bool operator O(const T& a,const T& b){ return a.E O b.E; }
#define DEFOP2(T,O,E,F) bool operator O(const T& a,const T& b){ return make_pair(a.E,a.F) O make_pair(b.E,b.F); }

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
int to_i(const string& s){int n;sscanf(s.c_str(),"%d",&n);return n;}
string to_s(int n){char buf[32];sprintf(buf,"%d",n);return string(buf);}

const int inf=1<<20;

int main(){
  int C; cin >> C;
  REP(CC,C){
    int n,k,b,t;
    cin >> n >> k >> b >> t;
    vint x(n), v(n);
    REP(i,n) cin >> x[i];
    REP(i,n) cin >> v[i];

    vint g(n);
    REP(i,n) g[i]=((b-x[i])+v[i]-1)/v[i];

    vint c(n,0);
    REP(i,n){
      FOR(j,i+1,n) if(g[j]>t) c[i]++;
      if(g[i]>t) c[i]=inf;
    }
    
    sort(ALL(c));
    int ans=0;
    REP(i,k) ans+=c[i];
    if(ans>=inf)
      printf("Case #%d: IMPOSSIBLE\n", CC+1);
    else
      printf("Case #%d: %d\n", CC+1, ans);
  }
}
