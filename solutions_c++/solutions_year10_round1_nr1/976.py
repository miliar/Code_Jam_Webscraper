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

const int N=1024;
char v[N][N];

bool check(int ci,int cj,int c,int n,int k){
  static const int DI[]={0,1,1,1};
  static const int DJ[]={1,1,0,-1};
  REP(d,4){
    int i=ci,j=cj;
    REP(l,k){ 
      if(!(0<=i && i<n && 0<=j && j<n)) goto end;
      if(v[i][j]!=c) goto end;
      i+=DI[d], j+=DJ[d];
    }
    return true;
  end:;
  }
  return false;
}

bool cmp(const char& a,const char& b){ return isalpha(a) < isalpha(b); }

int main(){
  int C; cin >> C;
  REP(CC,C){
    int n,k;
    cin >> n >> k;
    memset(v,'.',sizeof v);
    REP(i,n) REP(j,n) cin >> v[i][j];
    REP(i,n) stable_sort(v[i],v[i]+n,cmp);

    bool r=false,b=false;
    REP(i,n) REP(j,n){
      r=r||check(i,j,'R',n,k);
      b=b||check(i,j,'B',n,k);
    }

    printf("Case #%d: %s\n", CC+1, r==b ? (r ? "Both" : "Neither") : (r ? "Red" : "Blue"));
  }
  
}
