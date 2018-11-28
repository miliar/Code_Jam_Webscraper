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

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)


typedef long long ll;

using namespace std;

class Data{
public:
  int score[3];
  int apt;
  int getApt(){
    sort(score, score+3);
    int cnt = 0;
    rep(i, 3){
      REP(j, i+1, 3){
	cnt = max(abs(score[i] - score[j]), cnt);
      }
    }
    apt = cnt;
    return apt;
  }
};


vector<Data> V[3];

int ans = 0;

void solve(int id, int nowS, int limit, int now, int border, int n){
  if(n == id){
    if(limit == nowS)ans = max(ans, now);
    return;
  }
  FOR(it, V[id]){
    if(it->score[2] >= border)now++;
    if(it->apt == 2){
      nowS++;
    }
    if(nowS <= limit)solve(id+1, nowS, limit, now, border, n);
    
    if(it->apt == 2){
      nowS--;
    }
    if(it->score[2] >= border)now--;
  }
}

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout << "Case #" << tc+1 <<": ";
    int n, s, p;
    cin >> n >> s >> p;
    int t[n];
    rep(i, n)cin >> t[i];
    rep(id, n){
      V[id].clear();
      rep(i, 11){
	rep(j, 11){
	  if(i+j > t[id])continue;
	  if(t[id] - i - j > 10){
	    continue;
	  }
	  int k = t[id] - i - j;
	  Data d;
	  d.score[0] = i;
	  d.score[1] = j;
	  d.score[2] = k;
	  int cnt = d.getApt();
	  if(cnt > 2)continue;
	  V[id].push_back(d);
	}
      }
    }
    ans = 0;
    
    solve(0, 0, s, 0, p, n);
    cout << ans <<endl;
  }
  return 0;
}
