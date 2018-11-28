#include "cstdio"
#include "string"
using namespace std;
typedef long long i64;

const string t = "welcome to code jam";
const int MOD = 10000;
int memo[1000][19];
bool mark[1000][19];

int TruncLine(char* s) {
  int len = (int)strlen(s);
  if (len > 0 && s[len - 1] == '\n')
    s[--len] = '\0';
  return len;
}
int f(const char* s, int n, int i, int j) {
  if (j >= (int)t.size()) return 1;
  if (i >= n) return 0;
  int& count = memo[i][j];
  if (mark[i][j]) return count;
  count = f(s, n, i + 1, j), mark[i][j] = true;
  if (s[i] == t[j])
    (count += f(s, n, i + 1, j + 1)) %= MOD;
  return count;
}
int main() {
  static char s[1000];
  const int T = atoi(fgets(s, sizeof(s), stdin));
  for (int Ti = 1; Ti <= T; ++Ti) {
    const int n = TruncLine(fgets(s, sizeof(s), stdin));
    memset(mark, false, sizeof(mark));
    printf("Case #%d: %04d\n", Ti, f(s, n, 0, 0));
  }
  return 0;
}
