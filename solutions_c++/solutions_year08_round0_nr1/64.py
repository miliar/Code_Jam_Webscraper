#include <iostream>
#include <map>
using namespace std;
#define MAXS 100
#define MAXQ 1000
int S, Q, queries[MAXQ];
map<string, int> M;
int dp[MAXQ][MAXS + 1];
int go(int x, int last) {
  if (x == Q) 
    return 0;
  int &ret = dp[x][last];
  if (ret != -1)
    return ret;
  ret = 1000000000;
  if ((last!=S) && (last != queries[x])) 
    ret <?= go(x + 1, last);
  for (int i = 0; i < S; ++i) 
    if (i != queries[x])
      ret <?= 1 + go(x + 1, i);
  return ret;
}
int main() {
  int no_tests;
  string s;
  getline(cin, s);
  no_tests = atoi(s.c_str());
  for (int rr = 1; rr <= no_tests; ++rr) {
    M.clear();
    int at = 0;
    getline(cin, s);
    S = atoi(s.c_str());
    for (int i = 0; i < S; ++i) {
      string s;
      getline(cin, s);
      M[s] = at++;
    }
    getline(cin, s);
    Q = atoi(s.c_str());
    for (int i = 0; i < Q; ++i) {
      string s;
      getline(cin, s);
      queries[i] = M[s];
    }
    memset(dp, -1, sizeof(dp));
    printf("Case #%d: %d\n", rr, ((Q==0)?0:go(0, S) - 1));
  }
  return 0;
}
