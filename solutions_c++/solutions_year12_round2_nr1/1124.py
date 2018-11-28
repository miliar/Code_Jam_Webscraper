#include <algorithm>
#include <stdio.h>
int main ()
{
  int T, N, i, X, s[200], j, srt[200], k, sum, cnt;
  double best, v;
  scanf ("%d", &T);
  for (i = 1; i <= T; i++) {
    scanf ("%d", &N);
    X = 0;
    for (j = 0; j < N; j++) {
      scanf ("%d", &s[j]);
      X += s[j];
      srt[j] = s[j];
    }
    std::sort (srt, srt + N);
    printf ("Case #%d:", i);
    for (j = 0; j < N; j++) {
      sum = X;
      best = 1;
      cnt = 1;
      for (k = 0; k < N; k++) {
        if ((k == 0 || srt[k-1] != s[j]) && s[j] == srt[k]) continue;
        sum += srt[k] - s[j];
        cnt++;
        v = sum / (double)cnt / X;
        //printf ("\n%d / %d / %d = %lf\n", sum, cnt, X, v);
        if (best > v) best = v;
      }
      printf (" %.9lf", best < 0 ? 0 : best * 100);
    }
    printf ("\n");
  }
  return 0;
}
