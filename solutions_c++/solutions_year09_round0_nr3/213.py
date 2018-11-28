#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <set>
using namespace std;

const int N = 600;
const int MOD = 10000;
//const int MOD = 1000000000;

int calc_1(char* s, int offset, const char* msg, int p, int memo[][30], int used[][30]) {
  if (msg[p] == '\0') return 1;
  if (s[offset] == '\0') return 0;

  int sum = 0;
  for (int i = offset; s[i] != '\0'; i++) {
    if (s[i] == msg[p]) {
      if (used[i][p]) {
        // printf("[%s] [%s] %d\n", s+i, msg+p, memo[i][p]);
        sum = (sum + memo[i][p]) % MOD;
      }
      else {
        memo[i][p] = calc_1(s, i+1, msg, p+1, memo, used);
        used[i][p] = true;
        sum = (sum + memo[i][p]) % MOD;
      }
    }
  }
  return sum;
}

int calc(char* s) {
  const char* msg = "welcome to code jam";
  set<char> st(msg, msg+strlen(msg));

  char t[1000];
  int len = 0;
  for (int i = 0; s[i] != '\0'; i++) {
    if (st.find(s[i]) != st.end()) {
      // printf("contain:%c\n", s[i]);
      t[len++] = s[i];
    }
  }
  t[len] = '\0';

  int memo[N][30];
  int used[N][30] = {};
  return calc_1(t, 0, msg, 0, memo, used);
}

int main() {
  char s[1000];
  gets(s);
  int ncases = atoi(s);
  for (int cc = 0; cc < ncases; cc++) {
    gets(s);
    printf("Case #%d: %04d\n", cc+1, calc(s));
  }
}

