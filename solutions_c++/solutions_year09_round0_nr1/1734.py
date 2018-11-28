#include <cstdio>
#include <string.h>
#include <cstring>
using namespace std;

const int MAXLEN = 15;
const int MAXD = 5000;
const int MAXN = 500;
const int SIGMA = 26;
const int MAXPAT = (2 + SIGMA) * MAXLEN + 1;

int l, d, n;
char dict[MAXD][MAXLEN];
bool pattern[MAXN][MAXLEN][SIGMA];

void readdata() {
  int i, j, k, m;
  char mark;
  char s[MAXPAT];
  
  scanf("%d %d %d\n", &l, &d, &n);
  for (i = 0; i < d; ++i) {
    gets(s);
    for (j = 0; j < l; ++j)
      dict[i][j] = s[j];
    //    for (j = 0; j < l; ++j)
    //      printf("%c", dict[i][j]);
    //    printf("\n");
  }
  
  for (i = 0; i < n; ++i) {
    gets(s);
    //    puts(s);
    m = strlen(s);
    //    printf("%d\n", m);
    k = -1; mark = 0;
    for (j = 0; j < m; ++j) {
      if (s[j] == '(') {
	++k;
	mark = 1;
      }
      else if (s[j] == ')')
	mark--;
      else {
	k += 1 - mark;
	pattern[i][k][s[j] - 'a'] = 1;
      }
    }
    /*    for (j = 0; j < l; ++j) {
      for (k = 0; k < SIGMA; ++k) 
	printf("%d", pattern[i][j][k]);
      printf("\n");
    }
    printf("\n");*/
  }
}

void output() {
  int i, j, k, cnt;

  for (i = 0; i < n; ++i) {
    cnt = 0;
    for (j = 0; j < d; ++j) {
      for (k = 0; k < l; ++k)
	if (!pattern[i][k][dict[j][k] - 'a'])
	  break;
      if (k == l)
	++cnt;
    }
    printf("Case #%d: %d\n", i+1, cnt);
  }
}

int main() {
  readdata();
  output();
}
