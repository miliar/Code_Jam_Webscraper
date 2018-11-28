#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

bool check(const vector<int>& pp, double t, int d)
{
  double last_left = -1234567890;
  REP(i, SZ(pp)) {
    double ge = last_left + d;
    if(pp[i]+t < ge) return false;
    last_left = max(double(pp[i] - t), ge);
  }
  return true;
}

void solve()
{
  int c, d;
  vector<int> pp;
  scanf("%d %d",&c,&d);
  
  int total = 0;
  REP(i,c) {
    int p,v;
    scanf("%d %d",&p,&v);
    REP(j,v) pp.PB(p);
    total += v;
  }
  if(check(pp, 0, d)) {
    printf("0\n");
    return;
  }
  double left = 0.;
  double right = 1.0e13;
  REP(i,10000) {
    double mid = (left + right) / 2.;
    if(check(pp, mid, d)) right = mid;
    else left = mid;
  }
  printf("%lf\n",left);
}


int main(int argc, char *argv[])
{
  int kase;
  scanf("%d", &kase);
  FORE(i,1,kase) {
    printf("Case #%d: ",i);
    solve();
  }

  return 0;
}
