#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int n, m, len;
int memo[512][512];
char line[512], sub[] = "welcome to code jam";

int count(int i, int j) {
  int res = 0;
  if (j == len)
    return 1;
  if (i == m)
    return 0;
  if (memo[i][j] != -1)
    return memo[i][j];
  res = count(i+1, j);
  if (line[i] == sub[j])
    res += count(i+1, j+1);
  return memo[i][j] = res % 10000;
}

int main() {
  int cases = 1;
 
  len = strlen(sub);

  scanf(" %d ", &n);
  while (n--) {
    fgets(line, 505, stdin);
    m = strlen(line) - 1;
    memset(memo, -1, sizeof(memo));
    printf("Case #%d: %04d\n", cases++, count(0, 0));
  }

  return 0;
}
