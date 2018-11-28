#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#include<numeric>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<complex>
#include<cassert>
using namespace std;
#define rep(i,s,e) for(int i=(s),___e=(e);i<___e;++i)
#define REP(i,n) rep(i,0,n)
#define ITER(c) __typeof((c).begin())
#define FOR(i,c) for(ITER(c) i=(c).begin(),___e=(c).end();i!=___e;++i)
#define ALL(c) (c).begin(), (c).end()

char m[50][51];
char r[50][51];
int N, K;

int dr[] = {0,0,1,-1,1,1,-1,-1};
int dc[] = {1,-1,0,0,1,-1,1,-1};

int Count(int i, int j) {
  if(r[i][j] == '.') return 0;
  int ret = 1;
  REP(k, 8) {
    int s = i, t = j;
    int cnt = 0;
    char ch = r[s][t];
    while((0 <= s && s < N && 0 <= t && t < N) && r[s][t] == ch) {
      s += dr[k];
      t += dc[k];
      ++cnt;
    }
    ret = max(ret, cnt);
  }
    return ret;
}

int main()
{
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  REP(turn, T) {
    cin >> N >> K;
    REP(i, N) cin >> m[i];
    memset(r, 0, sizeof(r));
    // rot
    REP(i, N) REP(j, N) r[i][j] = m[j][i];
    // fall
    for(int i = N - 1; i > 0; --i) {
      REP(j, N) if(r[i][j] == '.') {
        for(int k = i - 1; k >= 0; --k) {
          if(r[k][j] != '.') {
            swap(r[i][j], r[k][j]);
            break;
          }
        }
      }
    }
    // check
    int max_bs = 0, max_rs = 0;
    REP(i, N) REP(j, N) if(r[i][j] != '.') {
      if(r[i][j] == 'B') {
        max_bs = max(max_bs, Count(i, j));
      } else {
        max_rs = max(max_rs, Count(i, j));
      }
    }
//     REP(i, N) puts(r[i]);
//     cout << max_bs << ' ' << max_rs << endl;
    const char* ret = "";
    if(max_bs < K && max_rs < K) {
      ret = "Neither";
    } else if(max_rs >= K && max_bs >= K) {
      ret = "Both";
    } else if(max_bs >= K) {
      ret = "Blue";
    } else {
      ret = "Red";
    }
    printf("Case #%d: %s\n", turn + 1, ret);
  }
  return 0;
}

