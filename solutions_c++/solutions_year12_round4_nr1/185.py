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

int n;
PI in[20000];
int vis[20000];

void solve(int ca){
  string ans="NO";

  cin>>n;
  rep(i,n)cin>>in[i].F>>in[i].S;
  cin>>in[n].F;
  in[n].S=0;
  memset(vis,0,sizeof(vis));
  set<PI> app;
  
  priority_queue<PI> q;
  q.push(mp(0,in[0].F));
  while(!q.empty()){
    int cv=q.top().F;
    int cd=q.top().S;
    q.pop();
    //cout<<cv<<' '<<cd<<endl;
    if(vis[cv]>=cd)continue;
    vis[cv]=cd;
    if(cv==n){
      ans="YES";
      break;
    }
    for(int ne=cv+1;ne<=n;++ne){
      if(in[ne].F>in[cv].F+cd)break;
      if(ne==n){
        ans="YES";
        break;
      }      
      if(vis[ne]<min(in[ne].F-in[cv].F,in[ne].S))
         q.push(mp(ne,min(in[ne].F-in[cv].F,in[ne].S)));
    }
  }

  cout<<"Case #"<<ca<<": "<<ans<<endl;
}

main(){
  int t;
  cin>>t;
  rep(i,t)
    solve(i+1);
}
