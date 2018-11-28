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

int nodo[10010];
int change[10010];

int t[10010][2];

int calc(int x, int val){
 if(change[x]==2){
  if(val==nodo[x])return 0;
  else return 1<<20;
 }
 int &ret = t[x][val];
 if(ret!=-1)return ret;
 ret = 1<<20;
 
 if(nodo[x]==0 || change[x]){
  int add = nodo[x]==1;
  if(val==0){
   ret<?=calc(2*x,0)+calc(2*x+1,0)+add;
  }
  else{
   ret<?=calc(2*x,1)+calc(2*x+1,0)+add;   
   ret<?=calc(2*x,1)+calc(2*x+1,1)+add;
   ret<?=calc(2*x,0)+calc(2*x+1,1)+add;
  }
 }
 if(nodo[x]==1 || change[x]){
  int add=nodo[x]==0;
  if(val==1){
   ret<?=calc(2*x,1)+calc(2*x+1,1)+add;
  }
  else{
   ret<?=calc(2*x,1)+calc(2*x+1,0)+add;   
   ret<?=calc(2*x,0)+calc(2*x+1,0)+add;
   ret<?=calc(2*x,0)+calc(2*x+1,1)+add;
  }
 }
// cout<<x<<" "<<val<<" "<<ret<<endl;
 return ret;
}

int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 int m,v;
 cin>>m>>v;
 REP(i,(m-1)/2){
  cin>>nodo[i+1]>>change[i+1];
 } 
 REP(i,(m+1)/2){
  cin>>nodo[i+(m-1)/2+1];
  change[i+(m-1)/2+1]=2;
 } 
 CLEAR(t,-1);
 int ret=calc(1,v);
 if(ret==1<<20){
  cout<<"Case #"<<ic++<<": IMPOSSIBLE"<<endl;
 }
 else cout<<"Case #"<<ic++<<": "<<ret<<endl;
}
return 0;
}
