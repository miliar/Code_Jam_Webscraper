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
  int T;
  cin>>T;
  rep(ca,T){
    cout<<"Case #"<<ca+1<<": ";
    int n;
    cin>>n;
    int o=1,b=1;
    int ot=0,bt=0;

    while(n--){
      char r;
      int p;
      cin>>r>>p;
      if(r=='B'){
        bt+=max(abs(p-b)+1,ot-bt+1);
        b=p;
      }else{
        ot+=max(abs(p-o)+1,bt-ot+1);
        o=p;
      }
    }
    cout<<max(bt,ot)<<endl;
  }
}
