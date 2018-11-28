#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxL = 1000 + 10;
const int infinite = 1 << 30;
const int maxK = 5 + 10;

char S[maxL], s[maxL];
int p[maxK];
bool used[maxK];
int K, L, ans;

void getinf()
{
  scanf("%d\n", &K);
  gets(S);
  L = strlen(S);
}

int Count()
{
  int tot = 1;
  for (int i = 1; i < L; i++)
    {
      if (s[i] != s[i - 1]) tot++;
    }
  return tot;
}

void update()
{
  for (int i = 0; i < L; i += K)
    {
      for (int j = 0; j < K; j++)
	{
	  s[i + j] = S[i + p[j]];
	}
    }
  ans <?= Count();
}

void dfs(int dep)
{
  if (dep == K) update();
  for (int i = 0; i < K; i++)
    {
      if (!used[i]) p[dep] = i, used[i] = 1, dfs(dep + 1), used[i] = 0;
    }
}

void solve()
{
  ans = infinite;
  dfs(0);
}

int main()
{
    freopen("input0.in","r",stdin);
    freopen("output.txt","w",stdout);
  int data;
  scanf("%d", &data);
  for (int i = 1; i <= data; i++)
    {
      getinf();
      solve();
      printf("Case #%d: %d\n", i, ans);
    }
}
