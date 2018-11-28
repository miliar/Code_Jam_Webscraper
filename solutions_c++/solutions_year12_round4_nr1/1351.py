#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <memory.h>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <cctype>
#include <set>
#include <fstream>
#include <cmath>
using namespace std;

#define rep(i, n) for(int i = 0; i< n; i++)
#define rep2(i, m, n) for(int i = m; i < n; i++)
typedef long long ll;
typedef pair<int, int> P;
const int INF = 1000000007;
const double EPS = 1e-10;

const int SZ = 10010;
int N;
ll d[SZ];
ll l[SZ];
ll best[SZ];

bool bfs(){
  queue<int> que;

  que.push(0);
  memset(best, -1, sizeof(best));
  best[0] = d[0];
  while(!que.empty()){

    int v = que.front(); que.pop();
    
    if(v == N) return true;
    for(int v2 = v; v2 <= N; v2++){
      if(d[v2] - d[v] <= best[v]){
	if(best[v2] < min(l[v2], d[v2]- d[v])){
	  best[v2] = min(l[v2], d[v2] - d[v]);
	  que.push(v2);
	}
      }else{
	break;
      }
    }
    for(int v2 = v; v2 >= 0; v2--){
      if(d[v] - d[v2] <= best[v]){
	if(best[v2] < min(l[v2], d[v]- d[v2])){
	  best[v2] = min(l[v2], d[v] - d[v2]);
	  que.push(v2);
	}
      }else{
	break;
      }
    }
  }
  return false;
}

int main(){
  int T;
  cin >> T;
  rep(t, T){
    cin >> N;
    rep(i,N) cin >> d[i] >> l[i];
    cin >> d[N];
    l[N] = 0;
    string res = bfs() ? "YES" : "NO";
    cout  << "Case #" << t + 1 << ": " << res << endl;
  }
  return 0;
}
