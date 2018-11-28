#include<iostream>
#include<vector>
#include<map>
using namespace std;

vector<int> v;
map< pair<int,int>, int > memo;

int rec(int a, int b){

  if( memo.find( make_pair(a,b) ) != memo.end() ){
    return memo[ make_pair(a,b) ];
  }
  
  int can = 0;
  for(int i = 0; i < v.size(); i++){
    if( a <= v[i] && v[i] <= b ) can++;
  }
  if( can == 0 ) return memo[make_pair(a,b)] = 0;

  int m = 987654321;
  
  for(int i = 0; i < v.size(); i++){
    if( a <= v[i] && v[i] <= b ) {
      int t = (v[i] - a) + (b - v[i]);
      t += rec(a, v[i] - 1);
      t += rec(v[i] + 1, b);
      m = min(m, t);
    }
  }
  
  return memo[make_pair(a,b)] = m;
}

int main(){
  int T;
  cin >> T;
  for(int tno = 0; tno < T; tno++){
    int P, Q;
    cin >> P >> Q;

    v.clear();
    for(int i = 0; i < Q; i++){
      int t; cin >> t;
      v.push_back(t);
    }

    memo.clear();
    
    int ans = rec(1, P);
    printf("Case #%d: %d\n", tno + 1, ans);
  }
}
    
