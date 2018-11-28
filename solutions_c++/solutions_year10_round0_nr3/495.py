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

int R,k,n,g[1060],next[1060][30];
int64 add[1060][30];
main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    cin>>R>>k>>n;
    assert(n<1060);
    FOR(i,n)cin>>g[i];
    FOR(i,n){
      add[i][0]=0;
      int j=0;
      while(j<n&&add[i][0]+g[(i+j)%n]<=k){
        add[i][0]+=g[(i+j)%n];
        j++;
      }
      next[i][0]=(i+j)%n;
//      cout<<i<<" -> "<<next[i][0]<<" with "<<add[i][0]<<endl;
    }
    for(int i=1;i<30;i++)FOR(j,n){
      next[j][i]=next[next[j][i-1]][i-1];
      add[j][i]=add[j][i-1]+add[next[j][i-1]][i-1];
    }
    int cur=0;
    int64 s=0;
    FOR(i,30)if(R&1<<i){
      s+=add[cur][i];
      cur=next[cur][i];
    }
    cout<<"Case #"<<c<<": "<<s<<endl;
  }
}
