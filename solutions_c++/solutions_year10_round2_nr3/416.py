#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
using namespace std;


long long f[600][600];
long long c[600][600];
long long moder = 100003;
int testID;

void init()
{
  c[1][0] = 1;
  c[1][1] = 1;
  for (int i = 2; i <= 500; ++i)
  {
    c[i][0] = 1;
    c[i][i] = 1;
    for (int j = 1; j < i; ++j)
      c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % moder;
  }
  memset(f, -1, sizeof(f));
}

long long getF(int a, int r)
{
  if (r > a - 1)
    return 0;

  if (r == a - 1)
    return 1;

  if (r == 1)
    return 1;

  if (f[a][r] >= 0)
    return f[a][r];


  f[a][r] = 0;
  for (int i = r; i <= r; ++i)
  {
    for (int j = 1; j <= i - 1; ++j)
    {
      int mid = r - j - 1;
      int num = a - i - 1;
      f[a][r] += getF(i, j) * c[num][mid];
      f[a][r] %= moder;
    }
  }

  return f[a][r];
}

void deal()
{
  int N;
  scanf("%d", &N);

  long long ans = 0;
  for (int i = 1; i <= N - 1; ++i)
  {
    ans += getF(N, i);
  }
  ans %= moder;

  cout << "Case #" << testID << ": " << ans << endl;
}

int main()
{
  init();
  int T;
  scanf("%d", &T);
  for (testID = 1; testID <= T; ++testID)
    deal();
  return 0;
}
