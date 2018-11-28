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

int m,n;
string mp[20];

int t[20][1<<10];

int nbits[2000];
int fbits(int x){
 int k=0;
 while(x){k+=x%2;x/=2;}
 return k;
}

int calc(int r, int st){
// cout<<r<<" "<<st<<endl;
 if(r==n)return 0;
 int &ret=t[r][st];
 if(ret!=-1)return ret;
 ret=0;
 REP(i,(1<<m)){
  int v=1;
  REP(j,m)if(mp[j][r]=='x' && (i>>j)%2)v=0;
  if(!v)continue;
  int lst=0;
  REP(j,m){
   if(lst && (i>>j)%2)v=0;
   lst=(i>>j)%2;
  }
  if(!v)continue;
  REP(j,m)if((st>>j)%2){
   if(j<m-1 && (i>>(j+1))%2)v=0;
   if(j>0 && (i>>(j-1))%2)v=0;
  }
  if(!v)continue;
 // cout<<"V "<<r<<" "<<st<<" "<<i<<" "<<nbits[i]<<endl;
  REP(j,m)cout<<((i>>j)%2);cout<<endl;
  REP(j,m)cout<<((st>>j)%2);cout<<endl;
  cout<<endl;
  ret>?=calc(r+1,i) + nbits[i];
 }
// cout<<"ret "<<r<<" "<<st<<" "<<ret<<endl;
 return ret;
}

int calc2(int r, int st){
// cout<<r<<" "<<st<<endl;
 if(r==m)return 0;
 int &ret=t[r][st];
 if(ret!=-1)return ret;
 ret=0;
 REP(i,(1<<n)){
  int v=1;
  REP(j,n)if(mp[r][j]=='x' && (i>>j)%2)v=0;
  if(!v)continue;
  int lst=0;
  REP(j,n){
   if(lst && (i>>j)%2)v=0;
   lst=(i>>j)%2;
  }
  if(!v)continue;
  REP(j,n)if((st>>j)%2){
   if(j<n-1 && (i>>(j+1))%2)v=0;
   if(j>0 && (i>>(j-1))%2)v=0;
  }
  if(!v)continue;
  //cout<<"V "<<r<<" "<<st<<" "<<i<<" "<<nbits[i]<<endl;
  ret>?=calc2(r+1,i) + nbits[i];
 }
 //cout<<"ret "<<r<<" "<<st<<" "<<ret<<endl;
 return ret;
}

void go(){
 CLEAR(nbits,0);
 REP(i,1<<10){
  nbits[i]=fbits(i);
 }
 
 cin>>m>>n;
 REP(i,m)cin>>mp[i];
 CLEAR(t,-1);
 cout<<calc2(0,0)<<endl;
}

int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 cout<<"Case #"<<ic++<<": ";
 go();
}
return 0;
}
