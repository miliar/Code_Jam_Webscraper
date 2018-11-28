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

int p[10000];
int nxt[10000];
int prev[10000];

int main(){
 int t;cin>>t;int ic=1;
 while(t--){
  int k;cin>>k;
  CLEAR(p,-1);
  REP(i,k){
   prev[i]=(i+k-1)%k;
   nxt[i]=(i+1)%k;
  }
  int x=0;
  for(int i=0;i<k;i++){
   for(int j=0;j<i;j++){
    x=nxt[x];
   }
   nxt[prev[x]]=nxt[x];
   prev[nxt[x]]=prev[x];
   p[x]=i+1;
   x=nxt[x];
  }
  int n;cin>>n;
  cout<<"Case #"<<ic++<<":";
  for(int i=0;i<n;i++){int xx;cin>>xx;cout<<" "<<p[xx-1];}
  cout<<endl;
 }
 return 0; 
}
