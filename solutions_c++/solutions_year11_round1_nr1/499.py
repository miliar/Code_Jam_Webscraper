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

main(){
  int test;
  cin>>test;
  rep(ca,test){
    cout<<"Case #"<<ca+1<<": ";
    ll n,pd,pg;
    cin>>n>>pd>>pg;
    bool ok=false;
    if(n<100){
      for(int i=1;i<=n;i++){
        ll pw=i*pd/100;
        if(pw*100==i*pd)ok=true;
      }
    }else ok=true;
    if((pg==100 && pd<100) || (pg==0 && pd>0))ok=false;
    cout<<(ok?"Possible":"Broken")<<endl;
  }
}
