#include <stdio.h>
#include <memory.h>

const int MAXD = 5001;
const int MAXN = 501;
const int MAXNL = 26;

int l, d, n;
char *words[MAXD];
bool **pattern[MAXN]; 

void init() {
  scanf("%d %d %d", &l, &d, &n);
  char tmp;
  scanf("%c", &tmp);
//  scanf("%c", &tmp);
  for (int i = 0; i < d; ++i) {
    words[i] = new char[l];
    for (int j = 0; j < l; ++j) {
      scanf("%c", &words[i][j]);
    }
    scanf("%c", &tmp);
//    scanf("%c", &tmp);
  }
  for (int i = 0; i < n; ++i) {
    pattern[i] = new bool*[l];
    for (int j = 0; j < l; ++j) {
      pattern[i][j] = new bool[MAXNL];
      memset(pattern[i][j], 0, sizeof(bool) * MAXNL);
      char tc;
      scanf("%c", &tc);
      if (tc == '(') {
	do {
	  scanf("%c", &tc);
	  if (tc == ')') break;
	  pattern[i][j][(int) (tc - 'a')] = 1;
	} while (true);
      } else {
	pattern[i][j][(int) (tc-'a')] = 1;
      }
    }
    scanf("%c", &tmp);
//    scanf("%c", &tmp);
  }
}

void solve() {
  for (int i = 0; i < n; ++i) {
    int count = 0;
    for (int j = 0; j < d; ++j) {
      bool flag = true;
      for (int k = 0; k < l; ++k)
	if (pattern[i][k][(int) (words[j][k] - 'a')] == 0) {
	  flag = false;
	  break;
	}
      if (flag) ++count;
    }
    printf("Case #%d: %d\n", i+1, count);
  }
}

int main() {
  init();
  solve();
}

