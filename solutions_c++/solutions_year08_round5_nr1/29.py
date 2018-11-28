#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define LET(i,c) typeof(c) i = (c)
#define MP make_pair
#define PB push_back
#define SORT(x) sort((x).begin(),(x).end())
#define ALL(x) (x).begin(),(x).end()
#define UNIQUE(x) remove(unique((x).begin(),(x).end()),(x).end())
#define CLEAR(x,v) memset((x),(v),sizeof((x)))
#define FORS(i,x) for(int i=0;i<(int)(x).size();i++)
#define X first
#define Y second
typedef long long ent;

set<int> h[6010],v[6010];

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

char mp[6010][6010];

void go(){
 REP(i,6010){h[i].clear();v[i].clear();}
 int n;
 cin>>n;
 int x=3005,y=3005;
 int d=0;
 REP(i,n){
  int t;string s;
  cin>>s>>t;
  REP(j,t){
   FORS(k,s){
    if(s[k]=='F'){
     int nx=x+dx[d];
     int ny=y+dy[d];
     if(d==0){
      v[y].insert(x);
     }
     if(d==2){
      v[y-1].insert(x);
     }
     if(d==1){
      h[x].insert(y);
     }
     if(d==3){
      h[x-1].insert(y);
     }
     x=nx;
     y=ny;
    }
    if(s[k]=='R'){
     d=(d+1)%4;
    }
    if(s[k]=='L'){
     d=(d+3)%4;
    }
   }
  }
 }
 CLEAR(mp,0);
 int ret=0;
 REP(i,6010){
  if(h[i].size()){
   int s=0;
   int lst=-1;
   FOREACH(j,h[i]){
    if(lst!=-1){
     if(s==0){
      for(int k=lst;k<*j;k++){
       if(mp[i][k]==0){
        mp[i][k]=1;
        ret++;
       }
      }
     }
    }
    lst=*j;
    s=1-s;
   } 
  }
 }
 REP(i,6010){
  if(v[i].size()){
   int s=0;
   int lst=-1;
   FOREACH(j,v[i]){
    if(lst!=-1){
     if(s==0){
      for(int k=lst;k<*j;k++){
       if(mp[k][i]==0){
        mp[k][i]=1;
        ret++;
       }
      }
     }
    }
    lst=*j;
    s=1-s;
   } 
  }
 }
 cout<<ret<<endl;
}

int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 cout<<"Case #"<<ic++<<": ";
 go();
}
return 0;
}
