#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int T;

char c[200][200];
int d[200][200];
bool in[200];
char s[10000];
char t[1000];
int n;

int main()
{
  scanf("%d", &T);
  for (int tt = 0; tt < T; tt++) {
    int C;
    scanf("%d", &C);
    memset(c, 0, sizeof(c));
    memset(d, 0, sizeof(d));
    for (int i = 0; i < C; i++) {
      scanf("%s", s);
      c[s[0]][s[1]] = c[s[1]][s[0]] = s[2];
      //printf("%c %c = %c\n", s[0], s[1], s[2]);
    }
    int D;
    scanf("%d", &D);
    for (int i = 0; i < D; i++) {
      scanf("%s", s);
      d[s[0]][s[1]] = d[s[1]][s[0]] = 1;
    //  printf(" opp %c %c\n", s[0], s[1]);
    }
    int N;
    scanf("%d", &N);
    scanf("%s", s);
    n = 0;
    for (int i = 0; i < N; i++) {
      t[n++] = s[i];
      bool merge = false;
      if (n >= 2) {
	if (c[t[n - 1]][t[n - 2]]) {
	  t[n - 2] = c[t[n - 1]][t[n - 2]];
	  n--;
	  merge = true;
	}
      }
      if (!merge) {
	for (int j = 0; j < n; j++) {
	  if (d[t[j]][s[i]]) {
	    n = 0;
	  }
	}
      }
      t[n] = 0;
     // printf("at %c: %s\n", s[i], t);
    }
    printf("Case #%d: [", tt + 1);
    for (int i = 0; i < n; i++) {
      printf("%c", t[i]);
      if (i + 1 < n) {
	printf(", ");
      }
    }
    printf("]\n");
  }
  return 0;
}