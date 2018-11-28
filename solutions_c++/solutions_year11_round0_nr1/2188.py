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
#define DEFOP(T,O,E)    bool operator O(const T& a,const T& b){ return a.E O b.E; }
#define DEFOP2(T,O,E,F) bool operator O(const T& a,const T& b){ return make_pair(a.E,a.F) O make_pair(b.E,b.F); }
#define RALL(c) (c).rbegin(), (c).rend()

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
inline int to_i(const string& s){int n;sscanf(s.c_str(),"%d",&n);return n;}
inline string to_s(int n){char buf[32];sprintf(buf,"%d",n);return string(buf);}

int move(vector<pair<int,int> >&a, int &ap, int &ai, 
         vector<pair<int,int> >&b, int &bp, int &bi){
  int t = abs(ap - a[ai].second) + 1;
  ap = a[ai].second;
  ai++;
  
  int dir = bp < b[bi].second ? +1 : -1;
  REP(i,t) if(bp != b[bi].second) bp += dir;
  return t;
}

int compute(){
  vector<pair<int,int> > o, b;
  int n; cin >> n;
  REP(i,n){ 
    char c; int t; cin >> c >> t; 
    if(c=='O') o.push_back(make_pair(i,t));
    else       b.push_back(make_pair(i,t));
  }

  o.push_back(make_pair(1<<20,1));
  b.push_back(make_pair(1<<20,1));

  int op = 1, bp = 1, oi = 0, bi = 0;
  int res = 0;
  REP(iter,n){
    if(o[oi].first < b[bi].first) res += move(o,op,oi,b,bp,bi);
    else                          res += move(b,bp,bi,o,op,oi);
  }

  return res;
}

int main(){
  int Case; cin >> Case;
  REP(CaseCount,Case){
    cout << "Case #" << CaseCount+1 << ": " << compute() << endl;
  }
}
