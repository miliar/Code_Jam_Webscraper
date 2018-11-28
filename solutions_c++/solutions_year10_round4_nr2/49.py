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

#define INF 1000000000
int64 P,m[1024],c[11][1024],t[11][1024][11];
main(){
  int C;cin>>C;
  for(int z=1;z<=C;z++){
    cin>>P;
    FOR(i,1<<P){
      cin>>m[i];
      m[i]=P-m[i];
    }
    for(int i=1;i<=P;i++)FOR(j,1<<P-i)cin>>c[i][j];
    FOR(i,1<<P-1)FOR(k,11)t[1][i][k]=k>=m[2*i]&&k>=m[2*i+1]?0:k+1>=m[2*i]&&k+1>=m[2*i+1]?c[1][i]:INF;
    for(int i=2;i<=P;i++)FOR(j,1<<P-i)FOR(k,11){
      t[i][j][k]=INF;
      t[i][j][k]<?=t[i-1][2*j][k]+t[i-1][2*j+1][k];
      if(k<10)t[i][j][k]<?=t[i-1][2*j][k+1]+t[i-1][2*j+1][k+1]+c[i][j];
    }
    cout<<"Case #"<<z<<": "<<t[P][0][0]<<endl;
  }
}
