#include <cstdio>
#include <assert.h>

char words[5000][20];
bool patterns[500][20][30];
int l;
int d;
int n;

void readPattern(int i) {
    for (int j = 0; j < 15; ++j) {
      for (int k =0; k < 15; ++k) {
        patterns[i][j][k] = false;
      }
    }

    char t[500];
    int r = scanf("%s\n", &t[0]);
    bool inset = false;
    int j = 0;
    int pos = 0;
    for(pos = 0; t[pos] != '\0'; ++pos) {
      char c = t[pos];
      if (c == '(') {
        inset = true;
        continue;
      }
      if (c == ')') {
        inset = false;
        ++j;
        continue;
      }
      assert(c >= 'a' && c <= 'z');
      patterns[i][j][c - 'a'] = true;
//      printf("set %d %d %d\n", i, j, (int)(c - 'a'));
      if (!inset) {
        ++j;
      }
    }
    assert (j==l);
}

bool matchesx(int word, int pattern) {
  for (int i = 0 ; i < l; ++i) {
    if (!patterns[pattern][i][words[word][i] - 'a']) {
      return false;
    }
  }
  return true;
}


int main() {
  scanf("%d %d %d\n", &l, &d, &n);
  for (int i = 0; i < d; ++i) {
    scanf("%s\n", &words[i][0]);
  }

  for (int i = 0; i < n; ++i) {
    readPattern(i);
  }
  
  for (int pattern = 0; pattern < n; ++pattern) {
    int count = 0;
    for (int word = 0; word < d; ++word) {
      if (matchesx(word, pattern)) {
        ++count;
//        printf("matching %s\n", &words[word][0]);
      }
    }
    printf("Case #%d: %d\n", pattern+1, count);
  }
}
