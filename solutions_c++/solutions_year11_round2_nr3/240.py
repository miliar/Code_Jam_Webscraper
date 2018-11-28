#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#define rep(i,n) for(int i=0;i<n;i++)
#define fr(i,c) for(__typeof (c.begin()) i=c.begin(); i!=c.end(); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long ll;

void pv(int room,int n){
  cerr<<"pv: ";
  rep(i,n)if(room&1<<i)cerr<<i+1<<" ";
  cerr<<endl;
}
bool ok(int num,int n,vi &rooms,vi &res){
  int pw[10]; pw[0]=1; rep(i,n)pw[i+1]=pw[i]*num;
  rep(i,pw[n]){
    int color[10];
    rep(j,n)color[j]=i/pw[j]%num;

    bool allok=1;

    rep(j,rooms.size()){
      bool ok[10]={};
      rep(k,n)if(rooms[j]&1<<k)ok[color[k]]=1;
      rep(k,num)if(!ok[k])allok=0;
    }

    if(allok){
      vi ans;
      rep(j,n)ans.pb(color[j]);
      res=ans;
      return 1;
    }
  }
  return 0;
}

int main(){
  int T; cin>>T;
  rep(cs,T){
    int n,m; cin>>n>>m;
    int u[8], v[8];
    rep(i,m)cin>>u[i];
    rep(i,m)cin>>v[i];

    vi rooms;
    rooms.pb((1<<n)-1);
    rep(i,m){
      int s=u[i]-1,t=v[i]-1;
      rep(j,rooms.size())if( (rooms[j]&1<<s)&&(rooms[j]&1<<t) ){
        int newroom=0;
        for(int k=s;;k=(k+1)%n){
          if(rooms[j]&1<<k)newroom|=1<<k;
          if(k==t)break;
        }
        rooms[j]=rooms[j]^newroom | 1<<s|1<<t;
        rooms.pb(newroom);
        break;
      }
    }

    int mnv=10;
    rep(i,rooms.size()){
      int v=0;
      rep(j,n)if(rooms[i]&1<<j)v++;
      mnv=min(v,mnv);
    }

    if(mnv==n){
      cout<<"Case #"<<cs+1<<": "<<n<<endl;
      rep(i,n)cout<<i+1<<(i==n-1?"\n":" ");
      continue;
    }
    for(int i=mnv;i>0;i--){
      vi cl;
      if(ok(i,n,rooms,cl)){
        cout<<"Case #"<<cs+1<<": "<<i<<endl;
        rep(j,n)cout<<cl[j]+1<<(j==n-1?"\n":" ");
        break;
      }
    }
  }
  return 0;
}
