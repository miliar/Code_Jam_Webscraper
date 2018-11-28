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

vector<int> primos;

int pat[1000011];

int find(int x){
 if(pat[x]==x)return x;
 else return pat[x]=find(pat[x]);
}

void merge(int a, int b){
 a=find(a);
 b=find(b);
 if(rand()%2)pat[b]=pat[a];
 else pat[a]=pat[b];
}

int main(){
 int t;cin>>t;int ic=1;
 primos.push_back(2);
 for(int i=3;i<=10000;i+=2){
  int v=1;
  for(int j=0;j<primos.size() && v;j++)if(i%primos[j]==0)v=0;
  if(v)primos.PB(i);
 }
 while(t--){
  ent a,b,p;
  cin>>a>>b>>p;
  int sz=b-a+1;
  REP(i,sz)pat[i]=i;
  FORS(i,primos)if(primos[i]>=p && primos[i]<=b){
   ent st=a-(a%primos[i])+primos[i];
   if(a%primos[i]==0)st-=primos[i];
   ent x=st+primos[i];
   while(x<=b){
    merge(st-a,x-a);
    x+=primos[i];
   }
  }
  int ret=0;
  REP(i,sz)if(pat[i]==i)ret++;
  cout<<"Case #"<<ic++<<": "<<ret<<endl;
 }
 return 0;
}




