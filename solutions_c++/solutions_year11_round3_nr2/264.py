#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define popcount  __builtin_popcount
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define all(c)  (c).begin(),(c).end()
#define rall(c)  (c).rbegin(),(c).rend()
#define tr(c,i)  for(__typeof__((c).begin()) i=(c).begin(),till=(c).end(); i!=till; i++)
#define found(s,e)  ((s).find(e)!=(s).end())
#define mset(arr,val)  memset(arr,val,sizeof(arr))

typedef long long ll;

int main(){
  int T;cin>>T; // 1-100
  rep(t,T){
    int L; // 0-2-N
    ll Y; // 0-1e11
    int N, C; // 1000:100000, 1000
    cin>>L>>Y>>N>>C;
    vector<int> a(C); //1-10000
    rep(c,C) cin>>a[c];

    vector<ll> d(N+1); d[0]=0;
    rep(i,N) d[i+1]=d[i] + 2LL*a[i%C];

    vector<int> j(N);
    priority_queue<int> pq;
    rep(i,N) {
      if (d[i+1]<=Y) j[i]=0;
      else if (d[i]<=Y) {
        j[i]=(int)(d[i+1]-Y)/2;
      } else j[i] = a[i%C];
      pq.push(j[i]);
    }

    ll TT = d[N]; int z=0;
    while(!pq.empty()){
      int hd = pq.top(); pq.pop();
      if (z++<L) TT -= hd;
    }
  

    printf("Case #%d: %lld\n", 1+t, TT);
  }
  return 0;
}
