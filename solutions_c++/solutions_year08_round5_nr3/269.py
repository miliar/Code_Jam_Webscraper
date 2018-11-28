#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
#define MAXN 10
#define MAXM 10
using namespace std;
vector<int> vali;
int ok[10];
int M, N;
int dp[MAXN][1<<MAXM];
int allowed[1<<MAXM];
int PC[1<<MAXM];
int pc(int x) { return !x?0:(x&1)+pc(x>>1); }
using namespace std;
int go(int row, int val) {
  int &ret = dp[row][val];
  if (ret != -1)
    return ret;
  ret = 0;
  for (int i = 0; i < vali.size(); ++i) {
    int mask = vali[i] & val;
    if (row == 0)
      ret >?= PC[mask];
    else
      ret >?= PC[mask] + go(row-1, allowed[mask]&ok[row-1]);
  }
  return ret;
}
bool good(int m) {
  for (int i = 0; i+1 < M; ++i)
    if ((m&(1<<i)) && (m&(1<<(i+1))))
      return false;
  return true;
}
int main() {
  string s;
  int no_cases;
  getline(cin, s);
  no_cases = atoi(s.c_str());
  for (int i = 0; i < (1<<MAXM); ++i)
    PC[i] = pc(i);
  for (int rr = 1; rr <= no_cases; ++rr) {
    getline(cin, s);
    sscanf(s.c_str(), "%d %d", &N, &M);
    memset(ok, 0, sizeof(ok));
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < N; ++i) {
      getline(cin, s);
      assert(s.size() == M);
      for (int j = 0; j < M; ++j)
	if (s[j] != 'x')
	  ok[i] |= 1<<j;
    }
    vali = vector<int>();
    for (int m = 0; m < (1<<M); ++m)
      if (good(m))
	vali.push_back(m);
    for (int m = 0; m < (1<<M); ++m) {
      int x = (1<<M)-1;
      for (int j = 0; j < M; ++j)
	if (m & (1<<j)) {
	  if (j > 0)
	    x &= ~(1<<(j-1));
	  if (j+1 < M)
	    x &= ~(1<<(j+1));
	}
      allowed[m] = x;
    }
    printf("Case #%d: %d\n", rr, go(N-1, ok[N-1]));
  }
  return 0;
}
