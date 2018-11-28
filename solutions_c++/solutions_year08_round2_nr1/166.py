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

int main(){
 int t;
 cin>>t;
 int ic=1;
 while(t--){
  ent n,a,b,c,d,x0,y0,m;
  cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
  vector<ent> x,y;
  REP(i,n){
   x.PB(x0);y.PB(y0);
   x0=(x0*a+b)%m;
   y0=(y0*c+d)%m;
  }

  ent mat[3][3];
  CLEAR(mat,0);
  REP(i,n)mat[x[i]%3][y[i]%3]++;
  ent tot=0;
  REP(i1,3)REP(i2,3)REP(j1,3)REP(j2,3)if(j1>i1 || (j1==i1 && j2>=i2))REP(k1,3)REP(k2,3)if(k1>j1 || (k1==j1 && k2>=j2)){

  // cout<<i1<<","<<i2<<" "<<j1<<","<<j2<<" "<<k1<<","<<k2<<endl;
if((i1+j1+k1)%3==0 && (i2+j2+k2)%3==0){
   if(i1==j1 && i2==j2 && j1==k1 && j2==k2){
    tot+=((mat[i1][i2]*(mat[i1][i2]-1))/2*(mat[i1][i2]-2))/3;
   }
   else if(i1==j1 && i2==j2){
    tot+=((mat[i1][i2]*(mat[i1][i2]-1))/2)*mat[k1][k2];
   }
   else if(i1==k1 && i2==k2){
    tot+=((mat[i1][i2]*(mat[i1][i2]-1))/2)*mat[j1][j2];
   }
   else if(j1==k1 && j2==k2){
    tot+=((mat[j1][j2]*(mat[j1][j2]-1))/2)*mat[i1][i2];
   }
   else tot+=mat[i1][i2]*mat[j1][j2]*mat[k1][k2];
  }}
 
  cout<<"Case #"<<ic++<<": "<<tot<<endl;
  
 }
 return 0;
}
