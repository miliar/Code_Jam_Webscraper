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
//int dx[]={0,-1,0,1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};
int dx[]={1,0,-1,-1,0,1};
int dy[]={1,1,0,-1,-1,0};

int un[10000];
int find(int x){
  if(x==un[x])return x;
  return un[x]=find(un[x]);
}

void unit(int a,int b){
  un[find(a)]=find(b);
}


int s,m;
set<PI> corner;
PI in[10000];
int edge(PI a){
  if(corner.count(a))return 0;
  if(a.F==1)return 1;
  if(a.S==1)return 2;
  if(a.F==2*s-1)return 3;
  if(a.S==2*s-1)return 4;
  if(a.F-a.S==s-1)return 5;
  if(a.S-a.F==s-1)return 6;
  return 0;
  /*
  if(min(a.F,a.S)==1)return true;
  if(max(a.F,a.S)==2*s-1)return true;
  if(abs(a.F-a.S)==s-1)return true;
  return false;
  */
}

int getring(){
  rep(i,m)un[i]=i;
  map<PI,int> ptoi;
  rep(i,m){
    set<int> app;
    int ins=0;
    rep(j,6){
      int nx=in[i].F+dx[j],ny=in[i].S+dy[j];
      int nnx=in[i].F+dx[(j+1)%6],nny=in[i].S+dy[(j+1)%6];
      if(!ptoi.count(mp(nx,ny)))
        continue;
      
      if(!ptoi.count(mp(nnx,nny))){
        app.insert(find(ptoi[mp(nx,ny)]));
        ++ins;
        continue;
      }
      if(find(ptoi[mp(nx,ny)]) != find(ptoi[mp(nnx,nny)])){
        app.insert(find(ptoi[mp(nx,ny)]));
        ++ins;
      }
    }
    if(ins != SZ(app))return i+1;
    
    rep(j,6){
      int nx=in[i].F+dx[j],ny=in[i].S+dy[j];
      if(!ptoi.count(mp(nx,ny)))
        continue;
      unit(i,ptoi[mp(nx,ny)]);
    }
    ptoi[in[i]] = i;
  }
  return m+1;
}

int getfork(){
  int low=0,up=m+1;
  while(low+1<up){
    int mid=(low+up)/2;
    map<PI,int> ptoi;
    rep(i,mid)
      ptoi[in[i]]=i;

    bool vis[m];
    memset(vis,0,sizeof(vis));
    bool ok=false;
    rep(i,mid){
      if(vis[i])continue;
      queue<PI> q;
      q.push(in[i]);
      set<int> app;
      while(!q.empty()){
        int cx=q.front().F,cy=q.front().S;
        int pn=ptoi[mp(cx,cy)];
        q.pop();
        if(vis[pn])continue;
        vis[pn]=true;
        int p=edge(PI(cx,cy));
        if(p)app.insert(p);
        if(SZ(app)>2)break;

        rep(j,6){
          int nx=cx+dx[j],ny=cy+dy[j];
          if(!ptoi.count(mp(nx,ny)))continue;
          q.push(mp(nx,ny));
        }
      }
      if(SZ(app)>2){
        ok=true;
        break;
      }
    }
    if(ok) up = mid;
    else low = mid;
  }
  return up;
}


int getbridge(){
  int low=0,up=m+1;
  while(low+1<up){
    int mid=(low+up)/2;
    map<PI,int> ptoi;
    rep(i,mid)
      ptoi[in[i]]=i;

    bool vis[m];
    memset(vis,0,sizeof(vis));
    bool ok=false;
    rep(i,mid){
      if(vis[i])continue;
      queue<PI> q;
      q.push(in[i]);
      int co=0;
      while(!q.empty()){
        int cx=q.front().F,cy=q.front().S;
        int pn=ptoi[mp(cx,cy)];
        q.pop();
        if(vis[pn])continue;
        vis[pn]=true;
        
        if(corner.count(PI(cx,cy)))++co;
        if(co>1)break;

        rep(j,6){
          int nx=cx+dx[j],ny=cy+dy[j];
          if(!ptoi.count(mp(nx,ny)))continue;
          q.push(mp(nx,ny));
        }
      }
      if(co>1){
        ok=true;
        break;
      }
    }
    if(ok) up = mid;
    else low = mid;
  }
  return up;
}

void solve(int ca){
  printf("Case #%d: ",ca);
  cin>>s>>m;
  corner.clear();
  corner.insert(mp(1,1));
  corner.insert(mp(s,1));
  corner.insert(mp(1,s));
  corner.insert(mp(s,s*2-1));
  corner.insert(mp(s*2-1,s));
  corner.insert(mp(s*2-1,s*2-1));

  rep(i,m)
    cin>>in[i].F>>in[i].S;
  int ring = getring();
  int bridge = getbridge();
  int fork = getfork();
  //printf("%d %d %d\n",ring,bridge,fork);

  int mi=min(ring,min(bridge,fork));
  if(mi==m+1){
    cout<<"none"<<endl;
    return;
  }

  string ans;

  if(bridge==mi)ans+="-bridge";
  if(fork==mi)ans+="-fork";
  if(ring==mi)ans+="-ring";
  /*
  if(ans=="-fork" && mi<12){
    cout<<s<<' '<<mi<<endl;
    rep(i,mi)cout<<in[i].F<<' '<<in[i].S<<endl;
    cout<<endl;
  }
  */
  ans=ans.substr(1);
  cout<<ans<<" in move "<<mi<<endl;
}

main(){
  int t;
  cin>>t;
  rep(ca,t)
    solve(ca+1);
}
