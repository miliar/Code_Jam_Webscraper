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
#include <list>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PI;
#define rep(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SZ(a) (int(a.size()))
#define F first
#define S second
const double pi=acos(-1);
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};

PI in[1000];

main(){
  int T;
  cin>>T;
  rep(ca,T){
    cout<<"Case #"<<ca+1<<": ";
    int x,s,r,n;
    double t;
    cin>>x>>s>>r>>t>>n;
    ll sum=0;
    rep(i,n){
      int b,e,w;
      cin>>b>>e>>w;
      in[i].F=w+s;
      in[i].S=e-b;
      sum+=e-b;
    }
    in[n].F=s;
    in[n].S=x-sum;
    ++n;
    sort(in,in+n);
    double ans=0;
    rep(i,n){
      if(1.*in[i].S/(in[i].F-s+r)<=t){
        t-=1.*in[i].S/(in[i].F-s+r);
        ans+=1.*in[i].S/(in[i].F-s+r);
      }else if(abs(t)<EPS){
        ans+=1.*in[i].S/in[i].F;
      }else{
        ans+=t;
        ans+=(in[i].S-t*(r+in[i].F-s))/in[i].F;
        t=0;
      }
    }
    printf("%.9f\n",ans);
  }
}
