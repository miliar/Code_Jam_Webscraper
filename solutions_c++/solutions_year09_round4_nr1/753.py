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

const int N=64;

int main(){
  int C; cin >> C;
  REP(CC,C){
    int n; cin >> n;
    char c[N][N];
    REP(i,n) REP(j,n) cin >> c[i][j];

    int v[N];
    REP(i,n){
      v[i]=0;
      for(int j=n-1;j>=0;--j) if(c[i][j]=='1'){ v[i]=j; break; }
    }


    int cnt=0;
    REP(i,n){
      int p;
      FOR(j,i,n) if(v[j]<=i){ p=j; break; }
      for(int j=p-1;j>=i;j--){ swap(v[j],v[j+1]); cnt++; }
      // cout << i << ": " << p << ": " ;
      // pp(v,n);
    }

    printf("Case #%d: %d\n", CC+1, cnt);
  }
}
