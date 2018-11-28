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

/*

int compute(int n,vint v){
  if(v.empty())   return 0;
  if(v.size()==1) return n-1;
  int a=v.size()/2, b=(v.size()+1)/2;
  int c;
  if(abs(v[a]*2-n)<abs(v[b]*2-n)) c=a; else c=b;
  vint va(v.begin(),v.begin()+b);
  vint vb(v.begin()+b+1,v.end());
  return compute(v[c]-1,va)+compute(n-v[c]-1,vb)+n-1;
}
*/

int calc(int n,vint &v){
  vint stop;
  int result=0;
  stop.push_back(0); stop.push_back(n+1);
  REP(i,v.size()){
    vint::iterator it=lower_bound(ALL(stop),v[i]);
    result+=(*it)-*(it-1)-2;
    stop.insert(it,v[i]);
  }
  return result;
}

int compute(int n,vint &v){
  int result=1<<20;
  do ls(result,calc(n,v)); while(next_permutation(ALL(v)));
  return result;
}


int main(){
  int C; cin >> C;
  REP(CC,C){
    int n,t; cin >> n >> t ;
    vint v(t);
    REP(i,t) cin >> v[i];
    sort(ALL(v));


    printf("Case #%d: %d\n",CC+1,compute(n,v));
  }

}
