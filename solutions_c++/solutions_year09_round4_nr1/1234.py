#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <cmath>

#include "cout.h"
using namespace std;
typedef long long ll;

#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define rep1(var,n)  for(int var=1;var<=(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

int N;
vector<int> rang;
int cnt;

void sw(vector<int> &r,  int a, int b){
  int tmp = r[a]; r[a] = r[b]; r[b] = tmp;
}

int score(const vector<int>& r){
  int sc = 0;
  rep(i,N){
    if (r[i] > i) sc -= (r[i] - i);
  }
  return sc;
}

main(){
  int T; cin >> T; // 60
  rep(t,T){
    cin >> N; // 8|40

    rang.resize(N);
    rep(n,N){
      string s; cin >> s;
      //ll sl=0, lw=-1;
      ll lw=-1;
      for(ll i=0,m=1LL,c=sz(s);i<c;i++,m<<=1) {
        //if (s[i]>'0') { sl+=m; lw=i; }
        if (s[i]>'0') lw=i;
      }
      rang[n] = lw;
    }
    // cout << rang << endl;

    set<vector<int> > visited;
    visited.clear();
    priority_queue<pair<int,pair<int,vector<int> > > > pq;
    // step, score, vec
    pq.push(make_pair(0,make_pair(score(rang),rang)));
    visited.insert(rang);
    
    while(!pq.empty()) {
      int step = -pq.top().first;
      int sc = -pq.top().second.first;
      if (sc == 0) {
        printf("Case #%d: %d\n", 1+t, step);
        break;
      }
      vector<int> r = pq.top().second.second;
      // cout << step << " " << sc << " " << r << endl;
      pq.pop();

      rep(i,N-1){
        sw(r,i,i+1);
        if (!found(visited,r)) {
          visited.insert(r);
          pq.push(make_pair(-(step+1),make_pair(-score(r),r)));
        }
        sw(r,i+1,i);
      }
    }
    //dp(0);
    //rp();
    ///
  }
}
