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
#include <cstring>
#include <sstream>
#include <cassert>
#include <ctime>
#include <list>
#include <numeric>
using namespace std;
static const double EPS = 1e-8;
typedef long long ll;
typedef pair<int,int> PI;
#ifndef M_PI
const double M_PI=acos(-1);
#endif
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SZ(a) (int((a).size()))
#define F first
#define S second
int dx[]={0,-1,0,1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};

void solve(int ca){
  printf("Case #%d:",ca);
  int n;
  cin>>n;

  vector<pair<PI,int> > in(n);
  rep(i,n)in[i].S=i;
  rep(i,n){
    cin >> in[i].F.S;
    in[i].F.S *= -1;
  }
  
  rep(i,n){
    cin >> in[i].F.F;
    in[i].F.F *= -1;
  }
  sort(ALL(in));
  rep(i,n)cout<<' '<<in[i].S;
  cout<<endl;
}

main(){
  int t;
  cin>>t;
  rep(i,t)
    solve(i+1);
}
