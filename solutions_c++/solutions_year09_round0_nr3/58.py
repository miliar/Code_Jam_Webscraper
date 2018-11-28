#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string.h>
#include <assert.h>
using namespace std;
#define maxn 505
#define maxm 20
#define MOD 10000
const string magic = "welcome to code jam";
int dp[maxn][maxm];
string s;
string itoa(int x) {
  char buf[50];
  sprintf(buf, "%d", x);
  return buf;
}
string foo(int x) {
  if (x < 10)
    return "000" + itoa(x);
  if (x < 100)
    return "00" + itoa(x);
  if (x < 1000)
    return "0" + itoa(x);
  return itoa(x);  
}
int go(int x, int y) {
  if (y == magic.size())
    return 1;
  if (x == s.size())
    return 0;
  int &ret = dp[x][y];
  if (ret != -1)
    return ret;
  ret = go(x + 1, y);
  if (s[x] == magic[y])
    ret += go(x + 1, y + 1);
  return ret %= MOD;
}
int main() {
  int N;
  cin >> N;
  getc(stdin);
  for (int rr = 1; rr <= N; ++rr) {
    getline(cin, s);
    memset(dp, -1, sizeof(dp));
    printf("Case #%d: %s\n", rr, foo(go(0, 0)).c_str());
  }
  return 0;
}
