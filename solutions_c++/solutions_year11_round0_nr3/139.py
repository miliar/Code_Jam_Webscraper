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

int add(int a,int b){
  int ret=0;
  for(int i=0;(1<<i)<=max(a,b);i++){
    if((a>>i&1)+(b>>i&1)==1){
      ret|=1<<i;
    }
  }
  return ret;
}

main(){
  int T;
  cin>>T;
  rep(ca,T){
    cout<<"Case #"<<ca+1<<": ";
    int n;
    cin>>n;
    int sum=0;
    rep(i,n){
      cin>>in[i];
      sum=add(sum,in[i]);
    }
    if(sum!=0)cout<<"NO"<<endl;
    else{
      sort(in,in+n);
      sum=0;
      rep(i,n-1){
        sum+=in[i+1];
      }
      cout<<sum<<endl;
    }
  }
}
