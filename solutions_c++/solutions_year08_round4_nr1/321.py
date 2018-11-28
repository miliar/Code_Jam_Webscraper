#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <set>
using namespace std;
struct state {
  int value;
  int ao;
  int c;
  state(int value, int ao, int c) : value(value), ao(ao), c(c) {
  }
  state(){}
};
vector<state> states;
int n, v;
bool isleaf(int a){
  return a>=(n-1)/2;
}
int improve(int a, int b){
  if(a == -1)return b;
  else if(b == -1) return a;
  else return min(a,b);
}
pair<int,int> dfs(int cur){
  if(isleaf(cur)){
    if(states[cur].value == 0){
      //cout << cur << " " << 0 << " " << -1 << endl;
      return make_pair(0, -1);
    } else {
      //cout << cur << " " << -1 << " " << 0 << endl;
      return make_pair(-1, 0);
    }
  } else {
    pair<int,int> left = dfs(2*(cur+1)-1);
    pair<int,int> right = dfs(2*(cur+1));
    state s = states[cur];
    int l = -1, r = -1;
    if(s.ao || s.c){
      int ll=-1,rr=-1;
      if(left.second != -1 && right.second != -1){
	rr = improve(r, left.second+right.second);
      }
      ll = improve(l, improve(left.first, right.first));
      if(!s.ao && s.c){
	rr=rr==-1?-1:rr+1;
	ll=ll==-1?-1:ll+1;
      }
      l = improve(l,ll);
      r = improve(r,rr);
    } 
    if(!s.ao || s.c){
      int ll=-1,rr=-1;
      if(left.first != -1 && right.first != -1){
	ll = improve(l, left.first+right.first);
      } 
      rr = improve(r, improve(left.second, right.second));
      if(s.ao && s.c){
	rr=rr==-1?-1:rr+1;
	ll=ll==-1?-1:ll+1;
      }
      l=improve(l,ll);
      r=improve(r,rr);
    }
    //cout << cur << " " << l << " " << r << endl;
      return make_pair(l,r);
  }
}
int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ": ";
    cin >> n >> v;
    states.resize(n);
    for(int i=0;i<(n-1)/2;i++){
      int a,b;
      cin >> a >> b;
      states[i] = state(-1,a,b); 
    }
    for(int i=0;i<(n+1)/2;i++){
      int c;
      cin >> c;
      states[i+(n-1)/2] = state(c,-1,-1);
    }
    pair<int,int> ret=dfs(0);
    if(v==0){
      int ans = ret.first;
      if(ans==-1){
	cout << "IMPOSSIBLE" << endl;
      } else {
	cout << ans << endl;
      }
    } else {
      int ans = ret.second;
      if(ans==-1){
	cout << "IMPOSSIBLE" << endl;
      } else {
	cout << ans << endl;
      }
    }
  }
  return 0;
}
