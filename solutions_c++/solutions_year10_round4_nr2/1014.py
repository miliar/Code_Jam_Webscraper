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

int rec(vint &v,int s,int l){
  int c=0; FOR(i,s,s+l) c=gs(c,v[i]);
  if(c==0) return 0;
  FOR(i,s,s+l) v[i]--;
  return rec(v,s,l/2) + rec(v,s+l/2,l/2) + 1;
}

int solve_small(vint &v,int n){
  REP(i,v.size()) v[i]=n-v[i];
  return rec(v,0,v.size());
}

int main(){
  int C; cin >> C;
  REP(CC,C){
    int n; cin >> n;
    vint v(1<<n);
    REP(i,1<<n) cin >> v[i];
    vint u(1,-1); int t;
    REP(i,n) REP(j,1<<(n-i-1)) cin >> t,u.push_back(t);
    printf("Case #%d: %d\n", CC+1, solve_small(v,n));
  }
}
