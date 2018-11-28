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
int n;
map<string,int>  name;

vector<pair<int,int> > fences[304];

int sol(int c1, int c2, int c3){
 vector<pair<int, int> > v;
 FORS(i,fences[c1])v.PB(fences[c1][i]);
 FORS(i,fences[c2])v.PB(fences[c2][i]);
 FORS(i,fences[c3])v.PB(fences[c3][i]);
 v.PB(MP(10001,20000));
 SORT(v);
 if(v[0].X!=1)return 1<<30;
 int st=0;
 int best=0;
 int ret=0;
//  cout<<"---"<<endl;FORS(i,v)cout<<v[i].X<<" "<<v[i].Y<<endl;cout<<"###"<<endl;
 FORS(i,v){
//   cout<<st<<" "<<best<<endl;
  if(st+1<v[i].X){
   if(best<st+1)return 1<<30;
   else{
//     cout<<"anado hasta "<<best<<endl;
    ret++;
    st=best;
   }
  }
  if(st+1>=v[i].X && v[i].Y>best)best=v[i].Y;

 }
 if(best<20000)ret= 1<<30;
 if(st<20000)ret++;
//   cout<<"RET "<<ret<<endl;
 return ret-1;
}

void go(){
 cin>>n;
 name.clear();
 int in=0;
 for(int i=0;i<304;i++)fences[i].clear();
 REP(i,n){
  string s;int a,b;cin>>s>>a>>b;
  if(name.count(s)==0)name[s]=in++;
  fences[name[s]].PB(MP(a,b));
 }
 int best=1<<30;
 in+=2;
 REP(i,in)SORT(fences[i]);
 for(int i=0;i<in;i++)for(int j=i+1;j<in;j++)for(int k=j+1;k<in;k++){
  best=min(best,sol(i,j,k));
 }
 if(best==1<<30)cout<<"IMPOSSIBLE"<<endl;
 else cout<<best<<endl;
}

int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 cout<<"Case #"<<ic++<<": ";
 go();
}
return 0;
}
