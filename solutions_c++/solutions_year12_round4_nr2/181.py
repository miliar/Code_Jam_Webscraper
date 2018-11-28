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
static const double EPS = 1e-7;
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
int dx[]={0,1,0,-1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};

PI in[1000];
int n,w,l;
PI ans[1000];

void solve(int ca){
  cin>>n>>w>>l;
  rep(i,n){
    cin>>in[i].F;
    in[i].S=i;
  }

  sort(in,in+n);
  reverse(in,in+n);

  int bw=-10000000;
  bool di=false;
  rep(i,n){
    int nx=max(0,bw+in[i].F);
    if(nx>w){
      nx=0;
      di=!di;
    }
    if(di)nx=w-nx;
    int ny=0;
    rep(j,i)
      if(abs(nx-ans[in[j].S].F)<in[j].F+in[i].F)
        ny=max(ny,ans[in[j].S].S+in[j].F+in[i].F);
    if(ny>l){
      --i;
      bw=-1000000;
      continue;
    }
    ans[in[i].S]=mp(nx,ny);
    if(di)nx=w-nx;
    bw=nx+in[i].F;
  }

  printf("Case #%d:",ca);
  rep(i,n)printf(" %d %d",ans[i].F,ans[i].S);
  cout<<endl;
}

main(){
  int t;
  cin>>t;
  rep(i,t)
    solve(i+1);
}
