#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <cassert>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PI;
#define rep(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SZ(a) (int(a.size()))
#define F first
#define S second
const double pi=acos(-1);
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};

int in[1000];
bool vis[1000];

int dfs(int v){
  if(vis[v])return 0;
  vis[v]=true;
  return 1+dfs(in[v]-1);
}

main(){
  int T;
  cin>>T;
  rep(ca,T){
    memset(vis,0,sizeof(vis));
    cout<<"Case #"<<ca+1<<": ";
    int ans=0;
    int n;
    cin>>n;
    rep(i,n)cin>>in[i];
    rep(i,n){
      if(vis[i])continue;
      if(in[i]==i+1)continue;
      ans+=dfs(in[i]-1);
    }
    cout<<ans<<endl;
  }
}
