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
int N,K;
char a[110][110];
main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    cin>>N>>K;
    FOR(i,N)cin>>a[i];
    FOR(i,N){
      int pos=N-1;
      for(int j=N-1;j>=0;j--)if(a[i][j]!='.'){char tmp=a[i][j];a[i][j]='.';a[i][pos--]=tmp;}
    }
    bool r=false,b=false;
    FOR(i,N)FOR(j,N)if(a[i][j]!='.')for(int dx=-1;dx<=1;dx++)for(int dy=-1;dy<=1;dy++)if(dx||dy){
      int z=0;
      while(i+z*dx>=0&&i+z*dx<N&&j+z*dy>=0&&j+z*dy<N&&a[i][j]==a[i+z*dx][j+z*dy])z++;
      if(z>=K){
        r|=a[i][j]=='R';
        b|=a[i][j]=='B';
      }
    }
    cout<<"Case #"<<c<<": "<<(r&&b?"Both":r?"Red":b?"Blue":"Neither")<<endl;
  }
}
