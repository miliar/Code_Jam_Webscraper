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

vstring get(){
  string s; cin >> s;
  REP(i,s.size()) if(s[i]=='/') s[i]=' ';
  istringstream sin(s);
  vstring v;
  while(sin >> s) v.push_back(s);
  return v;
}

int main(){
  int C; cin >> C;
  REP(CC,C){
    int a,b; cin >> a >> b;
    set<vstring> s;
    REP(i,a){
      vstring v=get();
      while(v.size()) s.insert(v), v.pop_back();
    }

    int ans=0;
    REP(i,b){
      vstring v=get();
      while(v.size()){ if(s.insert(v).second) ans++; v.pop_back(); }
    }
    printf("Case #%d: %d\n", CC+1, ans);
  }
}
