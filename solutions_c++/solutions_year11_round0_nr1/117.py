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
int solve(const vector<ii>& seq)
{
  int N = seq.size(); int t=0;
  int pos[2] = { 1, 1 }, dur[2] = { 0, 0 };
  rep(n,N){
    t++;
    int r=seq[n].first;
    int p=seq[n].second;
    int dis=abs(pos[r]-p); 
//    printf("Time=%d; (%d±%d %d±%d), %c to %d, dist %d\n",
//            t, pos[0],dur[0], pos[1],dur[1], r?'B':'O', p, dis);
    if (dis <= dur[r]){
      // put
      pos[r]=p;
      dur[r]=0; dur[1-r]++;
//      printf("  ... can push at %d. now (%d±%d, %d±%d)\n",
//             t, pos[0],dur[0], pos[1],dur[1]);
    }else{
      // need to wait
      int wait=dis-dur[r];
      t += wait;
      pos[r]=p;
      dur[r]=0; dur[1-r]+=1+wait;
//      printf("  ... can push at %d (waiting %d). now (%d±%d, %d±%d)\n",
//             t, wait, pos[0],dur[0], pos[1],dur[1]);
    }
  }
  return t;
}

int main(){
  int T;cin>>T;
  rep(t,T){
    int N;cin>>N;
    vector<ii> seq(N);
    rep(n,N){
      char r;int p; cin>>r>>p;
      seq[n] = make_pair(r=='B', p);
    }
    printf("Case #%d: %d\n", 1+t, solve(seq));
  }
  return 0;
}
