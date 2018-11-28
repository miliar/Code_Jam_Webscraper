#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
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
#include<bitset>
#include<ctime>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)
#define dbg(x) cerr << #x << " = " << (x) << endl


typedef long long ll;

using namespace std;


int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout <<"Case #" << tc+1<<": "<<flush;
    ll N, W, H;
    cin >> N >> W >> H;
    vector<pair<ll, ll > > R(N);
    rep(i, N){
      cin >> R[i].first;
      R[i].second = i;
    }
    pair<ll, ll> ans[N];
    sort(ALL(R));
    reverse(ALL(R));
    vector<pair<ll, ll> >   v;
    srand((unsigned)time(NULL));
    while(1){
      if(v.size() == R.size())break;
      bool next = false;
      rep(i, 100){
	ll w = (ll)rand()%(W+1);
	ll h = (ll)rand()%(H+1);
	bool found = false;
	rep(j, v.size()){
	  if(abs(w - v[j].first) * abs(w - v[j].first) + abs(h - v[j].second) * abs(h - v[j].second) <=
	     (R[j].first + R[v.size()].first) * (R[j].first + R[v.size()].first)){
	    found = true;
	    break;
	  }
	}
	if(found)continue;
	next = true;
	ans[R[v.size()].second] = make_pair(w, h);
	v.push_back(make_pair(w, h));
	break;
      }
      if(!next){
	v.pop_back();
      }
    }
    rep(i, v.size()){
      if(i!=0)cout <<' ';
      cout << ans[i].first <<' ' << ans[i].second;
    }
    cout << endl;
  }
  
  
  return 0;
}
