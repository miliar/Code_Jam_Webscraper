#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxN = 10000 + 10;
const int infinite = 1 << 30;

int F[maxN][3];
bool ope[maxN], can[maxN]; 
int ans, N, V, last;

void getinf()
{
  int x, y;
  char s[5];

  scanf("%d%d\n", &N, &V);
  memset(F, 0xff, sizeof(F));
  memset(ope, 0, sizeof(ope));
  memset(can, 0, sizeof(can));
  for (int i = 1; i <= N; i++) 
    {
      gets(s);
      if (strlen(s) == 1)
	{
	  sscanf(s, "%d", &x);
	  F[i][x] = 0;
	  F[i][1 - x] = -1;
	}
      else
	{
	  sscanf(s, "%d%d", &x, &y);
	  ope[i] = x, can[i] = y;
	  last = i;
	}
    }
}

void calc(int i, bool ope, int step)
{
  int L = i * 2, R = i * 2 + 1;
  if (ope)
    {
      for (int t1 = 0; t1 < 2; t1++)
	for (int t2 = 0; t2 < 2; t2++)
	  if (F[L][t1] > -1 && F[R][t2] > -1)
	    F[i][t1 & t2] <?= F[L][t1] + F[R][t2] + step;
    }
  else 
    {
      for (int t1 = 0; t1 < 2; t1++)
	for (int t2 = 0; t2 < 2; t2++)
	  if (F[L][t1] > -1 && F[R][t2] > -1)
	    F[i][t1 | t2] <?= F[L][t1] + F[R][t2] + step;
    }
}

void solve()
{
  for (int i = last; i > 0; i--)
    {
      F[i][1] = F[i][0] = infinite;
      calc(i, ope[i], 0);
      if (can[i]) calc(i, !ope[i], 1);
      if (F[i][0] == infinite) F[i][0] = -1;
      if (F[i][1] == infinite) F[i][1] = -1;
    }
}

int main()
{
  int data = 0;
  scanf("%d", &data);
  for (int i = 1; i <= data; i++)
    {
      getinf();
      solve();
      if (F[1][V] == -1) printf("Case #%d: IMPOSSIBLE\n", i);
      else printf("Case #%d: %d\n", i, F[1][V]);
    }
}
