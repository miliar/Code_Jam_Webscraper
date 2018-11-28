#include <cstdio>
#include <cstring>

typedef long long huge;

int g[2000];
huge s[2000];
int r, k, n;

inline huge sum(int st, int l)
{
  if (st + l - 1 < n)
    return s[st+l-1] - ((st == 0)?0:s[st-1]);
  else
    return s[n-1] - ((st == 0)?0:s[st-1]) + s[(st+l-1)%n];
}

int tab[2000];

int realfind(int l, int r, int st)
{
  if (r - l == 1)
    return l;
  int mid = (l+r)/2;
  huge s = sum(st, mid);
  if (s < (huge)k)
    return realfind(mid, r, st);
  else if (s == (huge)k)
    return mid;
  else
    return realfind(l, mid, st);
}

int find(int l, int r, int st)
{
  if (tab[st] != -1)
    return tab[st];
  else
    return tab[st] = realfind(l, r, st);
}

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for (int test=0; test<ntests; ++test)
    {
      scanf(" %d %d %d", &r, &k, &n);
      for (int i=0; i<n; ++i)
	scanf(" %d", &g[i]);
      s[0] = g[0];
      for (int i=1; i<n; ++i)
	s[i] = s[i-1] + g[i];
      memset(tab, -1, sizeof(tab));
      if (s[n-1] <= k)
	{
	  printf("Case #%d: %lld\n", test+1, s[n-1]*r);
	}
      else
	{
	  huge ans = 0;
	  int st = 0;
	  for (int i=0; i<r; ++i)
	    {
	      int mx = find(0, n, st);
	      ans += sum(st, mx);
	      st = (st + mx)%n;
	    }
	  printf("Case #%d: %lld\n", test+1, ans);
	}
    }
  return 0;
}
