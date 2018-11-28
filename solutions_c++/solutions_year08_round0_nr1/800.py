#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
using namespace std;
#define inf 1000000000
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a-1;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define SORT(a) sort(ALL(a))
#define SZ(a) a.size()
#define LEN(a) a.length()
#define pb push_back
typedef long long ll;
typedef double dbl;

ifstream fin("A-large.in");
ofstream fout("A-sol.txt");

int S,Q;
vector<string> engines,queries;
int memo[101][1001];

int check(int engine,int index){
  int &m=memo[engine][index];
  if(m!=-1) return m;
  if(index==Q) return 0;
  if(engines[engine]==queries[index]){
    int res=inf;
    REP(i,S) if(i!=engine) res=min(res,check(i,index));
    return m=res+1;
  }
  return m=check(engine,index+1);
}

void solve(){
  int res=inf;
  memset(memo,-1,sizeof(memo));
  REP(i,S) res=min(res,check(i,0));
  fout<<res<<endl;
}

main(){
  int N;
  string t; getline(fin,t);
  N=atoi(t.c_str());
  REP(i,N){
    getline(fin,t);
    S=atoi(t.c_str());
    REP(j,S){
      string s;
      getline(fin,s);
      engines.pb(s);
    }
    getline(fin,t);
    Q=atoi(t.c_str());
    REP(j,Q){
      string s;
      getline(fin,s);
      queries.pb(s);
    }
    fout<<"Case #"<<i+1<<": ";
    solve();
    engines.clear(); queries.clear();
  }
}
