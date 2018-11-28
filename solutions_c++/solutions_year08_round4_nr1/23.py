#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

int m,v,g[11000],c[11000],t[11000][2];
main(){
  int C;cin>>C;
  for(int cc=1;cc<=C;cc++){
    cin>>m>>v;
    for(int i=1;i<=m;i++)t[i][0]=t[i][1]=11000;
    for(int i=1;i<=(m-1)/2;i++)cin>>g[i]>>c[i];
    for(int i=1;i<=(m+1)/2;i++){int z;cin>>z;t[(m-1)/2+i][z]=0;}
    for(int i=(m-1)/2;i>=1;i--){
      FOR(left,2)FOR(right,2)t[i][g[i]?left&right:left|right]<?=t[2*i][left]+t[2*i+1][right];
      if(c[i])FOR(left,2)FOR(right,2)t[i][!g[i]?left&right:left|right]<?=t[2*i][left]+t[2*i+1][right]+1;
    }
    cout<<"Case #"<<cc<<": ";
    if(t[1][v]<11000)cout<<t[1][v]<<endl;
    else cout<<"IMPOSSIBLE"<<endl;
  }
}
