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
#include <cassert>
#include <fstream>
using namespace std; 
#define REP(i,b,n) for(int i=b;i<n;i++) 
#define rep(i,n)      REP(i,0,n) 
#define pb push_back  
#define mp make_pair 
#define ALL(C)   (C).begin(),(C).end() 
#define fe(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr != (c).end();itr++)
#define BITSHIFT(X)     ( (1<<(X)) )
#define CONTAIN(S,X) ( ((S)&BITSHIFT(X)) != 0)
template<class T> void vp(T &a,int p){rep(i,p)cout << a[i]<<" ";cout << endl;}  
template<class T> T ceilUp(const T& a,const T& b){return (a+b-1)/b;}
typedef complex<double>P; 
typedef long long ll; 
typedef unsigned long long ull; 
typedef pair<int,int> pii; 
const ll mod = 1000000009;
const int N = 100000;

class st{
public:
  int len,now;
  bool operator<(const st &a)const{
    if (a.len != len)return len < a.len;
    return now > a.now;
  }
};

bool vis[N];
int cost[N];
bool solve(int n,vector<int> &d,vector<int> &l,int D){
  priority_queue<st> Q;
  rep(i,n)vis[i] = false,cost[i] = 0;
  int len = d[0];
  if (len >= D)return true;
  Q.push((st){len,0});
  cost[0] = len;

  while(!Q.empty()){
    st tmp = Q.top();Q.pop();
    int now = tmp.now,len=tmp.len;
    if (cost[now] != len)continue;
    if (d[now]+len >= D){
      return true;
    }
    //rep(next,n){
    REP(next,now+1,n){
      //if (next == now )continue; 
      if (abs(d[now]-d[next]) > len)continue;
      int nextlen = min(d[next]-d[now],l[next]);
      if (cost[next] > nextlen)continue;
      cost[next] = nextlen;
      Q.push((st){nextlen,next});
    }
  }
  return false;
}

main(){
  int te,tc=1;
  cin>>te;
  while(te--){
    int n;
    cin>>n;
    vector<int> d(n),l(n);
    rep(i,n)cin>>d[i]>>l[i];
    int D;
    cin>>D;
    bool res = solve(n,d,l,D);
    cout <<"Case #" << tc ++  << ": ";
    if (res)cout <<"YES" << endl;
    else cout <<"NO" << endl;
  }
  return 0;
}

