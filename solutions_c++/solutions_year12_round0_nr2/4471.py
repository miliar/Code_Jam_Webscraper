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
const int INF = 10000;
const double EPS = 1e-10;

int total[110];
int memo[110][110];
int T, N, S, p;

int calc(int pos, int rest){
  if(pos == N){
    return rest == 0 ? 0 : -INF;
  }
  if(memo[pos][rest] != -1) return memo[pos][rest];
  int &res = memo[pos][rest] = -INF;
  for(int i = 0; i <= 10; i++){
    for(int j = 0; j <= i; j++){
      for(int k = 0; k <= j; k++){
	if(i + j + k == total[pos]){
	  if(i - k <= 1){
	    res = max(res, (i >= p) + calc(pos + 1, rest));
	  }
	  if(i - k == 2 && rest > 0){
	    res = max(res, (i >= p) + calc(pos + 1, rest - 1));
	  }
	}
      }
    }
  }
  return res;
}

int main(){
  cin >> T;
  rep(t, T){
    cin >> N >> S >> p;
    rep(i, N) cin >> total[i];
    memset(memo, -1, sizeof(memo));
    cout << "Case #" << t + 1 << ": " << calc(0, S) << endl;
  }
  return 0;
}
