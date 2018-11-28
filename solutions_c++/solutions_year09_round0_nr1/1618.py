#include <stdio.h>
#include <string.h>

#define MAX_D 5000
#define MAX_L 15
#define MAX_N 500

int w[MAX_D][MAX_L];

int main() {
  int cs=0;
  int p2[26];
  char str[1024];
  int l, d, n;
  scanf("%d %d %d", &l, &d, &n);

  p2[0] = 1;
  for (int i=1; i<26; i++)
    p2[i] = 2*p2[i-1];

  memset(w, 0, sizeof(w));
  for (int i=0; i<d; i++) {
    scanf("%s", str);
    for (int j=0; j<l; j++) {
      w[i][j] = p2[str[j]-'a'];
    }
  }

  int pattern[MAX_L];
  for (int i=0; i<n; i++) {
    scanf("%s", str);

    int o=0;
    for (int j=0; j<l; j++, o++) {
      pattern[j] = 0;
      if (str[o] == '(') {
        while (str[++o] != ')')
          pattern[j] |= p2[str[o]-'a'];
      } else pattern[j] = p2[str[o]-'a'];
      //printf("%d ", pattern[j]);
    }
    //printf("\n");

    int cnt = 0;
    for (int j=0; j<d; j++) {
      int o;
      for (o=0;o<l;o++)
        if (!(w[j][o]&pattern[o])) break;
      if (o == l) cnt++;
    }
    printf("Case #%d: %d\n", ++cs, cnt);
  }

  return 0;
}
