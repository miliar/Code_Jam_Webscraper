
#include <cstdio>
#include <cstring>

char T[26][26];
int O[26][26];

int solve () {

  memset (T, 0, sizeof(T));
  memset (O, 0, sizeof(O));

  int c, d, n;
  char c_str[4], d_str[3], n_str[101];

  scanf ("%d", &c);
  for (; c--; ) {
    scanf("%s", c_str);

    T[c_str[0]-'A'][c_str[1]-'A'] = c_str[2];
    T[c_str[1]-'A'][c_str[0]-'A'] = c_str[2];
  }

  scanf ("%d", &d);
  for (; d--; ) {
    scanf("%s", d_str);

    O[d_str[0]-'A'][d_str[1]-'A'] = 1;
    O[d_str[1]-'A'][d_str[0]-'A'] = 1;
  }

  char res[101];
  int r = 0;
  res[r] = '\0';

  scanf ("%d%s", &n, n_str);
  for (int i = 0; i < n; i++) {
    if (r > 0 && T[res[r-1]-'A'][n_str[i]-'A'] > 0) {
      res[r-1] = T[res[r-1]-'A'][n_str[i]-'A'];
      continue;
    }

    int j;
    for (j = 0; j < r; j++) {
      if (O[res[j]-'A'][n_str[i]-'A'] > 0)
        break;
    }
    if (j < r) {
      r = 0;
      res[r] = '\0';

      continue;
    }

    res[r++] = n_str[i];
    res[r] = '\0';
  }

  printf ("[");
  for (int j = 0; j < r; j++) {
    printf("%c", res[j]);
    if (j < r-1)
      printf(", ");
  }
  printf ("]\n");

  return 0;
}

int main() {

  int TC;
  scanf ("%d", &TC);

  for (int tc = 1; tc <= TC; tc++) {
    printf ("Case #%d: ", tc);
    solve ();
  }

  return 0;
}
