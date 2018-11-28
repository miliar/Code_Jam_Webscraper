#include <cstdio>
#include <cstring>

const char* hints[][2] = 
  {
    {"aoz", "yeq"},
    {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
     "our language is impossible to understand"},
    {"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
     "there are twenty six factorial possibilities"},
    {"de kr kd eoya kw aej tysr re ujdr lkgc jv",
     "so it is okay if you want to just give up"}
  };

const int T_MAX = 30, T_DIM = T_MAX + 10;
const int L_MAX = 100, L_DIM = L_MAX + 10;
const int CHAR_MAX = 256;

int T;
char s[T_MAX][L_MAX];
char tbl[CHAR_MAX];

int main() {
  scanf("%d ", &T);

  for(int i = 0; i < 4; i++) {
    const char *p, *q;
    p = hints[i][0];
    q = hints[i][1];

    while(*p != 0) {
      tbl[*p] = *q;
      p++;
      q++;
    }
  }

  fprintf(stderr, "T:%d\n", T);

  for(int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);
    for(;;) {
      char c;
      scanf("%c", &c);
      if(c == '\n')
	break;
      printf("%c", tbl[c]);
    }
    printf("\n");
  }
}
