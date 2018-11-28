#include<cstdio>
#include<algorithm>

using namespace std;

typedef long long ll;

const int MAX_D = 1000*1000;

int d[MAX_D+4];

int main()
{
  d[0] = 0;
  int N = 1;
  while (N < MAX_D)
    {
      int j = 0;
      for (int i = 0 ; i < N ; i++)
	{
	  d[j++] = 0;
	  d[j++] = 1;
	  if (d[i])
	    d[j++] = 1;
	  if (j >= MAX_D)
	    break;
	}
      N = j;
    }
  for (int i = 1 ; i <= MAX_D ; i++)
    d[i] += d[i-1];
  int T;
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; t++)
    {
      ll A1, A2, B1, B2;
      scanf("%lld%lld%lld%lld", &A1, &A2, &B1, &B2);
      ll res = (A2-A1+1)*(B2-B1+1);
      for (ll a = A1 ; a <= A2 ; a++)
	{
	  ll l = d[a-1]+1;
	  ll r = l + a - 1;
	  if (B1 > r || B2 < l)
	    continue;
	  l = max(l, B1);
	  r = min(r, B2);
	  res -= r - l + 1;
	}
      printf("Case #%d: %lld\n", t, res);
    }
}
