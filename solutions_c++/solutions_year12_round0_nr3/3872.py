#include<queue>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<map>
#include<fstream>
using namespace std;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define rep(i,n) for(int i=0;i<n;i++)
#define pb push_back
#define sz size()
#define psi pair<string,int>
#define all(x) x.begin(),x.end()
#define GI ({int t;scanf("%d",&t); t;})
#define flush(x) memset(x,0,sizeof(x))
#define ll long long
#define mod 1000000007
#define maxn 1000010
#define GLI ({ll t;scanf("%lld",&t); t;})
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
ll poww[20];
int count(ll num) {
  int res = 0;
  while(num>0) {
    num /= 10;
    res++;
  }
  return res;
}
int f(int n, int m) {
  ll res = 0;
  for(int i = n; i <= m; i++) {
    stringstream ss;
    ss<<i;
    string s = ss.str();
    ll k = s.sz, pww = poww[k];
    set<ll> dup;
    //cout<<"i: "<<i<<endl;
    int totpart = count(i);
    for(int j=1; j<=k-1; j++) {
      ll fpart = i/poww[j], spart = i%poww[j];
      ll chg = spart*pww/poww[j]+fpart;
      if(count(fpart)+count(spart) != totpart) continue;
      //cout<<fpart<<" "<<spart<<" "<<chg<<endl;      
      if(chg <= m && chg>i) {  dup.insert(chg); }
    }
    res += dup.sz;
    dup.clear();
  }
  return res;
}
int main() {
  int t = GI, kase = 1, T;
  T = t;
  poww[0] = 1ll;
  rep(i,12) poww[i+1] = 10ll*poww[i];
  while(t--) {
    int lo, hi;
    lo = GI; hi = GI;
    cout<<"Case #"<<kase<<": "<<f(lo,hi);
    if(kase != T) cout<<endl;
    kase++;
  }
}