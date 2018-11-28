#include<cstdio>
#include<algorithm>

using namespace std;

int a[100];
int dyn[100][256];
int D, I, M, N;
const int inf = 9999999;

int go(int i, int k)
{
  if (i < 0)
    return 0;
  if (dyn[i][k] < inf)
    return dyn[i][k];
  int res = inf;
  res = min(res, go(i-1, k) + D);
  if (M)
    for (int k2 = 0 ; k2 < 256 ; k2++)
      res = min(res, go(i-1, k2)+abs(a[i]-k2)+(max(0,abs(k2-k)-1))/M*I);
  else
    res = min(res, go(i-1, k)+abs(a[i]-k));
  return dyn[i][k] = res;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; t++)
    {
      fill_n(*dyn, 256*100, inf);
      scanf("%d%d%d%d", &D, &I, &M, &N);
      for (int i = 0 ; i < N ; i++)
	scanf("%d", &a[i]);
      int res = inf;
      for (int k = 0 ; k < 256 ; k++)
	res = min(res, go(N-1, k));
      printf("Case #%d: %d\n", t, res);
    }
}
