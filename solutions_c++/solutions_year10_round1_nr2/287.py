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
int D,I,M,N,a[110],t[110][300];
main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    cin>>D>>I>>M>>N;
    FOR(i,N)cin>>a[i+1];
    FOR(i,110)FOR(j,300)t[i][j]=INF;
    FOR(j,300)t[0][j]=I;
    for(int i=1;i<=N;i++){
      FOR(j,300){
        t[i][j]=t[i-1][j]+D;
        t[i][j]<?=D*(i-1)+abs(a[i]-j);
      }
      FOR(j,300)FOR(k,300)if(abs(j-k)<=M)t[i][k]<?=t[i-1][j]+abs(a[i]-k);
      if(M)FOR(j,300)FOR(k,300)if(j!=k)t[i][k]<?=t[i][j]+(abs(j-k)+M-1)/M*I;
    }
    int r=INF;
    FOR(j,300)r<?=t[N][j];
    cout<<"Case #"<<c<<": "<<r<<endl;
  }
}
