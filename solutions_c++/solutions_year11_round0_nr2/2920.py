#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<cassert>
#include<queue>
#include<stack>
#include<bitset>
#include<cstring>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)

using namespace std;
typedef long long lli;
typedef vector<int> vint;
typedef pair<int, int> pii;
const double EPS = 0.00000001;
const int INF = 1000000000;
template<class T> void pp(T t, int n){
  rep(i, n){
    cout << t[i] << ' ';
  }
  cout << endl;
}

map<string, char> combine;
map<char, vector<int> > op;


bool comb(vector<char> &V){
  int n = V.size();
  if(n < 2)return false;
  string tmp;
  tmp += min(V[n-1], V[n-2]);
  tmp += max(V[n-1], V[n-2]);
  if(combine.find(tmp) == combine.end())return false;
  V.pop_back();
  V.pop_back();
  V.push_back(combine[tmp]);
  return true;
}

void del(vector<char> &V){
  set<int> flag[50];
  FOR(it, V){
    FOR(it2, op[*it]){
      flag[*it2].insert(*it);
      if(flag[*it2].size() == 2){
        V.clear();
        return;
      }
    }
  }
}

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    int C, D, N;
    combine.clear();
    op.clear();
    cin >> C;
    rep(i, C){
      string s;
      cin >> s;
      string tmp = s.substr(0, 2);
      sort(ALL(tmp));
      combine[tmp] = s[2];
    }
    cin >> D;
    rep(i, D){
      string s;
      cin >> s;
      op[s[0]].push_back(i);
      op[s[1]].push_back(i);
    }
    cin >> N;
    vector<char> ans;
    rep(i, N){
      char c;
      cin >> c;
      ans.push_back(c);
      while(comb(ans));
      del(ans);
    }
    cout << "Case #"<< tc+1 << ": [";
    rep(i, ans.size()){
      if(i != 0)cout << ", ";
      cout << ans[i];
    }
    cout << "]" << endl;
  }
  return 0;
}
