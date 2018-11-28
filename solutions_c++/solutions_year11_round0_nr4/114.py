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
#define cons(x,y) make_pair((x),(y))
#define car(x) ((x).first)
#define cdr(x) ((x).second)
#define caar(x) (x).first.first
#define cdar(x) (x).first.second
#define cadr(x) (x).second.first
#define cddr(x) (x).second.second

//#include "cout.h"

int main(){
  int T;cin>>T; //1-100
  rep(t,T){
    int N;cin>>N; //1-10:1000
    vector<int> od(N); int wo=0;
    rep(n,N){
      cin>>od[n]; if(od[n]!=1+n)wo++;
    }

//   cout << od << endl;
//  printf("Case #%d: %8.6f\n", 1+t, (double)wo);
    printf("Case #%d: %d.000000\n", 1+t, wo);
  }
  return 0;
}
