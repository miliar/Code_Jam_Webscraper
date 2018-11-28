
#include <iostream>
#include <cstdio>
#include <cstring>
#define MOD 100003

using namespace std;

int rank[1000];
int npicked = 0;

int n;

bool is_pure(int v)
{
  while (rank[v] != 1)
    if (rank[v] == 0)
      return false;
    else
      v = rank[v];

  return true;
}

int pick(int v)
{
  rank[v] = ++npicked;

  int x = 0;
  if (v == n) { if (is_pure(n)) x++; }
  else
    for (int i = v+1; i <= n; i++)
      x = ( (x % MOD) + (pick(i) % MOD) ) %MOD;

  rank[v] = 0;
  npicked--;
  return x % MOD;
}

void solve(int c)
{
  cin >> n;
  npicked = 0;
  memset(rank, 0, sizeof rank);

  int x = 0;
  for (int i = 2; i <= n; i++)
    x = ( (x%MOD) + (pick(i) % MOD) ) % MOD;

  printf("Case #%d: %d\n", c, x % MOD);
}

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; i++)
    solve(i+1);
}
