#include <stdio.h>

int main(void) {
  int L, D, N;
  scanf("%d %d %d", &L, &D, &N);

  unsigned int words[8192][16];

  char word[256];
  for (int i = 0; i < D; i++) {
    scanf("%s", word);
    for (int j = 0; j < L; j++) {
      words[i][j] = 1 << (word[j] - 'a');
    }
  }

  unsigned int patterns[8192][16];

  char pattern[256];
  for (int i = 0; i < N; i++) {
    int k = 0;
    scanf("%s", pattern);

    int bitmask = 0;
    bool in_parenthesis = false;
    for (int j = 0; pattern[j]; j++) {
      char c = pattern[j];
      if (c == '(') {
	in_parenthesis = true;
      } else if (c == ')') {
	in_parenthesis = false;
	patterns[i][k++] = bitmask;
	bitmask = 0;
      } else if (in_parenthesis) {
	bitmask |= 1 << (c - 'a');
      } else {
	patterns[i][k++] = 1 << (c - 'a');
      }
    }

    // printf("%s: ", pattern);
    // for (int j = 0; j < L; j++) {
    //   printf("%d,", patterns[i][j]);
    // }
    // printf("\n");
  }

  for (int p = 0; p < N; p++) {
    int count = 0;
    for (int w = 0; w < D; w++) {
      bool ok = true;
      for (int j = 0; j < L; j++) {
	if (!(patterns[p][j] & words[w][j])) {
	  ok = false;
	  break;
	}
      }
      if (ok) count++;
    }
    printf("Case #%d: %d\n", p + 1, count);
  }
  return 0;
}
