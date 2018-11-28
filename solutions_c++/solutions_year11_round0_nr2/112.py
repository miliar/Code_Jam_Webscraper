#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define popcount  __builtin_popcount
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define REP(var,ar)  for(int var=0,lim=(ar).size();var<lim;var++)
#define FOR(var,from,to) for(int var=(from),till=(to);var<=till;var++)
#define all(c)  (c).begin(),(c).end()
#define rall(c)  (c).rbegin(),(c).rend()
#define tr(c,i)  for(__typeof__((c).begin()) i=(c).begin(),till=(c).end(); i!=till; i++)
#define found(s,e)  ((s).find(e)!=(s).end())
#define mset(arr,val)  memset(arr,val,sizeof(arr))

typedef vector<int> Vi;
typedef vector<vector<int> > VVi;

typedef pair<int,int> ii;
typedef pair<char,char> cc;
#define cons(x,y) make_pair((x),(y))
#define car(x) ((x).first)
#define cdr(x) ((x).second)
#define caar(x) (x).first.first
#define cdar(x) (x).first.second
#define cadr(x) (x).second.first
#define cddr(x) (x).second.second

//#include "cout.h"

int main(){
  int T;cin>>T;
  rep(t,T){
//    cout << "--------" << endl;
//    printf("Case #%d: ", 1+t); cout<<endl;    

    map<cc,char> comb;
    int C;cin>>C; //0-1:36
    rep(c,C){
      string abc;cin>>abc;
      comb[cons(abc[0],abc[1])] = abc[2];
      comb[cons(abc[1],abc[0])] = abc[2];
    }

    set<cc> opp;
    int D;cin>>D; //0-1:28
    rep(d,D){
      string xy;cin>>xy;
      opp.insert(cons(xy[0],xy[1]));
      opp.insert(cons(xy[1],xy[0]));
    }

    int N;cin>>N; //1-10:100
    string seq;cin>>seq;

//    cout << comb << endl;
//    cout << opp << endl;

    vector<char> f;
    rep(n,N){
      char c=seq[n];
      int fl=f.size();
      if (fl==0) {
        f.pb(c); continue;
      }
      cc bc=cons(f[fl-1],c);
      if(found(comb,bc)){
        f[fl-1] = comb[bc];
      }else{
        bool is_opp=0;
        rep(j,fl){
          cc gc=cons(f[j],c);
          if(found(opp,gc)) {
            is_opp=1; break;
          }
        }
        if(is_opp){
          f.resize(0);
        }else{
          f.pb(c);
        }
      }
//      printf("  n=%d/%d: ", n, N); cout << f << endl;
    }

//    cout << N << " " << seq << " -> " << string(all(f)) << endl << endl;
    printf("Case #%d: [", 1+t); 
    int fl=f.size();
    rep(i,fl){
      if (i) printf(", ");
      putchar(f[i]);
    }
    printf("]\n");
    //printf("Case #%d: %d\n", 1+t, 0);
  }
  return 0;
}
