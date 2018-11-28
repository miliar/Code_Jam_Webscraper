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
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef double dbl;

ifstream fin("A.in");
ofstream fout("A.out");

struct pt{
  ll x,y;
};

bool operator==(const pt p1,const pt p2){
  if(p1.x==p2.x) return p1.y==p2.y;
  return false;
}

int n,m; //n is number of trees: max 100000
vector<pt> pts;

bool good(ll x1,ll y1,ll x2,ll y2,ll x3,ll y3){
  ll x=x1+x2+x3; ll y=y1+y2+y3;
  if(x%3 || y%3) return false;
  return true;
}

void go(){
  ll ct=0;
  REP(i,n-2)
    FOR(j,i+1,n-1)
    FOR(k,j+1,n){
    ll x1,x2,x3; ll y1,y2,y3;
    x1=pts[i].x; x2=pts[j].x; x3=pts[k].x;
    y1=pts[i].y; y2=pts[j].y; y3=pts[k].y;
    if(good(x1,y1,x2,y2,x3,y3)){
      ct++;
    }
  }
  fout<<ct<<endl;
}

void subsolve(){
  fin>>n;
  ll a,b,c,d,x,y;
  fin>>a>>b>>c>>d>>x>>y>>m;
  pt init; init.x=x; init.y=y;
  pts.pb(init);
  for(int i=1;i<n;i++){
    ll p,q;
    x=(a*x+b)%m;
    y=(c*y+d)%m;
    pt s; s.x=x; s.y=y;
    pts.pb(s);
  }
  /*  REP(i,n){
    fout<<pts[i].x<<' '<<pts[i].y<<endl;
  }
  */
  n=pts.size();
  go();
  pts.clear();
}

void input(){
  int N; fin>>N;
  REP(i,N){
    fout<<"Case #"<<i+1<<": ";
    subsolve();
  }
}

main(){
  input();
}
