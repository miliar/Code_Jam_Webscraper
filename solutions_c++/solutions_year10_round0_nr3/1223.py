#include <stdio.h>
#include <string.h>

const int maxn = 1010;

long long a[maxn];
bool used[maxn];
long long earns[maxn];
long long pos[maxn];
long long begin;
long long r, k ,n;
int tc;

int main ()
{
  scanf ("%d", &tc);
  for (long long tt = 1; tt <= tc; tt++)
  {
    scanf ("%lld%lld%lld", &r, &k, &n);
    for (long long i = 0; i < n; i++)
    {
      scanf ("%lld", &a[i]);
    }
    memset (used, 0, sizeof (used));
    long long i;
    long long now = 0;
    long long len = -1;
    earns[0] = 0;
    for (i = 1; i <= r; i++)
    {
      long long cnt = 0;
      long long left = k;
      long long earn = 0;
      pos[now] = i;
      used[now] = true;
      fprintf (stderr, "begin: %lld\n", now);
      while (left >= a[now] && cnt < n)
      {
        fprintf (stderr, "left: %lld, now: %lld\n", left, a[now]);
        left -= a[now];
        earn += a[now];
        now = (now + 1) % n;
        cnt++;
      }
      earns[i] = earn + earns[i - 1];
      fprintf (stderr, "earns: %lld\n", earn);
      if (used[now])
      {
        len = i - pos[now] + 1;
        begin = pos[now];
        break;
      }
    }
    fprintf (stderr, "len: %lld, from: %lld\n", len, begin);
    long long tot = i;
    long long ans = 0;
    if (len < 0)
    {
      ans = earns[r];
    }
    else
    {
      long long times = (r - begin + 1) / len;
      ans = (earns[tot] - earns[begin - 1]) * times +
        earns[begin + (r - begin + 1) % len - 1];
    }
    printf ("Case #%lld: %lld\n", tt, ans);
  }
  return 0;
}
