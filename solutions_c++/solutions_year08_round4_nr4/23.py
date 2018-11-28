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

int t[1<<17][17];
main(){
  int C,k;cin>>C;
  for(int c=1;c<=C;c++){
    string S;
    cin>>k>>S;
    int ans=1000000,cost[20][20]={};
    vector<string> blocks(S.size()/k);
    FOR(i,S.size()/k)FOR(j,k)blocks[i]+=S[i*k+j];
    FOR(a,k)FOR(b,k)FOR(i,blocks.size())cost[a][b]+=blocks[i][a]!=blocks[i][b];
    FOR(first,k){
      memset(t,60,sizeof(t));
      t[1<<first][first]=0;
#define INF 100000000      
      for(int used=1<<first;used<(1<<k);used++)FOR(last,k)if(t[used][last]<INF)FOR(next,k)if(!(used&1<<next))
        t[used+(1<<next)][next]<?=t[used][last]+cost[last][next];
      FOR(last,k){
        int cur=t[(1<<k)-1][last]+1;
        FOR(i,blocks.size()-1)cur+=blocks[i][last]!=blocks[i+1][first];
        ans<?=cur;
      }
    }
    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
}
