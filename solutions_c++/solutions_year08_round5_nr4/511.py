#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxN = 100 + 10;
const int size = 10007;

int F[maxN][maxN];
int N, M, R;

void getinf()
{
  int x, y;
  memset(F, 0, sizeof(F));
  F[1][1] = 1;
  scanf("%d%d%d", &N, &M, &R);
  for (int i = 0; i < R; i++)
    {
      scanf("%d%d", &x, &y);
      F[x][y] = -1;
    }
}

void update(int i, int j, int t)
{
  if (i <= N && j <= M && F[i][j] > -1)
    F[i][j] = (F[i][j] + t) % size;
}

void solve()
{
  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= M; j++)
      {
	if (F[i][j] == -1) continue;
	update(i + 1, j + 2, F[i][j]);
	update(i + 2, j + 1, F[i][j]);
      }
}

int main()
{
  int data;
  scanf("%d", &data);
  for (int tot = 1; tot <= data; tot++)
    {
      getinf();
      solve();
      printf("Case #%d: %d\n", tot, F[N][M]);
    }
}
