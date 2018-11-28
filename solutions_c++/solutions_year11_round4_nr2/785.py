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
#include <list>
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

string in[500];

main(){
  int T;
  cin>>T;
  rep(ca,T){
    cout<<"Case #"<<ca+1<<": ";
    int r,c,d;
    cin>>r>>c>>d;
    rep(i,r){
      cin>>in[i];
      rep(j,c)in[i][j]-='0';
    }
    int ans=-1;
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
        for(int k=i+3;k<=r;k++){
          int l=j+k-i;
          if(l>c)break;
          int cx=0,cy=0;
          for(int x=i;x<k;++x){
            for(int y=j;y<l;++y){
              if(x==i && (y==j || y==l-1) ||
                 x==k-1 && (y==j || y==l-1))continue;
              cx+=(d+in[x][y])*(2*x-(k+i-1));
              cy+=(d+in[x][y])*(2*y-(l+j-1));
            }
          }
          if(cx==0 && cy==0)ans=max(ans,k-i);
        }
      }
    }
    if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
    else cout<<ans<<endl;
  }
}
