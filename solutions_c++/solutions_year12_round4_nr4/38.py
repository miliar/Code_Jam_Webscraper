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
int dx[]={0,-1,0,1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};


string in[100];
int r,c;

pair<int,string> bfs(int x,int y){
  pair<int,string> ret;
  queue<PI> q;
  q.push(mp(x,y));
  set<PI> app;
  while(!q.empty()){
    PI p=q.front();q.pop();
    if(app.count(p))continue;
    app.insert(p);

    rep(i,3){
      int nx=p.F+dx[i],ny=p.S+dy[i];
      if(in[nx][ny]=='#')continue;
      q.push(mp(nx,ny));
    }
  }

  ret.F=SZ(app);
  ret.S="Unlucky";


  /*
  cout<<SZ(app)<<endl;
  FOR(it,app)cout<<it->F<<' '<<it->S<<' ';
  cout<<endl;
  */

  queue<set<PI> > bfsq;
  bfsq.push(app);
  set<set<PI> > bapp;
  while(!bfsq.empty()){
    set<PI> cv=bfsq.front();
    bfsq.pop();
    if(bapp.count(cv))continue;
    bapp.insert(cv);


    if(cv.size()==1 &&
       cv.begin()->F==x &&
       cv.begin()->S==y){
      ret.S="Lucky";
      return ret;
    }

    rep(i,3){
      set<PI> nv;
      bool ok=true;
      FOR(it,cv){
        int nx=it->F-dx[i],ny=it->S+dy[i];
        if(in[nx][ny]=='#'){
          nv.insert(*it);
          continue;
        }
        if(!app.count(mp(nx,ny))){
          ok=false;
          break;
        }
        nv.insert(mp(nx,ny));
      }
      if(!ok)continue;
      bfsq.push(nv);
    }
  }
  return ret;
}

pair<int,string> ans[100];

void solve(int ca){
  printf("Case #%d:\n",ca);
  
  cin>>r>>c;
  rep(i,r)cin>>in[i];

  int ap=0;
  rep(i,r)rep(j,c)
    if(isdigit(in[i][j])){
      ++ap;
      ans[in[i][j]-'0']=bfs(i,j);
    }

  rep(i,ap)cout<<i<<": "<<ans[i].F<<' '<<ans[i].S<<endl;
       
}


main(){
  int t;
  cin>>t;
  rep(i,t)
    solve(i+1);
}
