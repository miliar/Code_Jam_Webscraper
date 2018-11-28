
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int m[2000];
int smaller[2000][2000];
long long price[2000][2000];

long long mini[16][1600][1600];
int p;
int x, y;

#define INF 1000000000

long long apply(int s, int e, int seen)
{
  int v = smaller[s][e];

  if (mini[seen][s][e] >= 0)
    return mini[seen][s][e];

  //printf("%d -> %d (max %d) (seen %d) (price %lld) %d >= %d - %d: %s. %d - %d <= 1: %s\n", s, e, v, seen, price[s][e], seen, p, v, (seen >= p-v) ? "true":"false", e, s, (e-s<=1)?"true":"false");
  if (seen >= p-v) return mini[seen][s][e] = 0;
  if (e - s <= 1) return mini[seen][s][e] = INF;

  int middle = (s+e)/2;
  return mini[seen][s][e] = std::min(
    price[s][e] + apply(s, middle, seen + 1) + apply(middle, e, seen + 1),
    apply(s, middle, seen) + apply(middle, e, seen));
}

void solve(int CASE)
{
  cin >> p;
  int n = 1 << p;
  memset(mini, -1, sizeof mini);
  x = 0;
  y = 0;

  for (int i = 0; i < n; i++)
    cin >> m[i];

  for (int i = 0; i < n; i++)
  {
    smaller[i][i] = 2*n;
    for (int j = i+1; j <= n; j++)
      smaller[i][j] = std::min(smaller[i][j-1], m[j-1]);
  }


  int dummy;
  for (int i = 0; i < p; i++)
  {
    int jump = 1 << (i+1);
    for (int j = 0; j < (1 << (p-1-i)); j++)
    {
      cin >> dummy;
      price[j*jump][(j+1)*jump] = dummy;
    }
  }

  long long int k = apply(0, 1 << p, 0);
  printf("Case #%d: %lld\n", CASE, k);
}

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) solve(i+1);
  return 0;
}
