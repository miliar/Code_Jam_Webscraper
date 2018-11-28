#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <cassert>
#include <fstream>
using namespace std; 
#define REP(i,b,n) for(int i=b;i<n;i++) 
#define rep(i,n)      REP(i,0,n) 
#define pb push_back  
#define mp make_pair 
#define ALL(C)   (C).begin(),(C).end() 
#define fe(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr != (c).end();itr++)
#define BITSHIFT(X)     ( (1<<(X)) )
#define CONTAIN(S,X) ( ((S)&BITSHIFT(X)) != 0)
template<class T> void vp(T &a,int p){rep(i,p)cout << a[i]<<" ";cout << endl;}  
template<class T> T ceilUp(const T& a,const T& b){return (a+b-1)/b;}
typedef complex<double>P; 
typedef long long ll; 
typedef unsigned long long ull; 
typedef pair<int,int> pii; 
const ll mod = 1000000009;
const double eps = 1e-10;
int is_intersected_circle(P a,P b,double r1,double r2){
  double d = abs(a-b);
  if (d<eps && abs(r1-r2)<eps)return 3;
  if (d+r2 < r1)return 0;
  if (d+r1 < r2)return 1;
  if (d > r1+r2)return 4;
  return 2;
}

bool rec(int n,int now,double w,double h,vector<double> &r,vector<P> &pos){
  rep(i,now){
    REP(j,i+1,now)if (is_intersected_circle(pos[i],pos[j],r[i],r[j]) != 4)return false;
  }
  if (now == n){
    rep(i,n){
      printf(" %.10lf %.10lf",pos[i].real(),pos[i].imag());
    }
    printf("\n");
    return true;
  }
  rep(i,100){//try 100 times
    double x = rand()/(double)RAND_MAX * w,y = rand()/(double)RAND_MAX*h;
    pos[now].real() = x;
    pos[now].imag() = y;
    if (rec(n,now+1,w,h,r,pos))return true;
  }
  return false;
}


void solve(int n,double w,double h,vector<double> &r){
  vector<P> pos(n);
  rep(i,n){
    swap(r[0],r[i]);
    pos[0] = P(0,0);
    if (rec(n,1,w,h,r,pos))return;
    swap(r[0],r[i]);
  }
  assert(false);
  return;
}

main(){
  srand(20121212);
  int te,tc=1;
  cin>>te;
  while(te--){
    int n;
    double w,h;
    cin>>n>>w>>h;
    vector<double> r(n);
    rep(i,n)cin>>r[i];
    printf("Case #%d:",tc++);
    solve(n,w,h,r);
  }
  return 0;
}

