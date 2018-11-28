
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int x[100];
int v[100];

bool reaches[100];
int swaps_to_reach[100];

int n, k, b, t;

void solve(int CASE)
{
  cin >> n >> k >> b >> t;
  for (int i = 0; i < n; i++)
    cin >> x[i];
  for (int i = 0; i < n; i++)
    cin >> v[i];

  memset(reaches, 0, sizeof reaches);
  memset(swaps_to_reach, 0, sizeof swaps_to_reach);

  int nreaches = 0;
  for (int i = n-1; i >= 0; i--)
  {
    if (v[i]*t >= b-x[i])
    {
      nreaches++;
      reaches[i] = true;
      swaps_to_reach[i] = 0;
      for (int j = i + 1; j < n; j++)
        if (reaches[j])
        {
          swaps_to_reach[i] += swaps_to_reach[j];
          break;
        }
        else
          swaps_to_reach[i]++;
    }
  }

  if (nreaches < k)
  {
    printf("Case #%d: IMPOSSIBLE\n", CASE);
    return;
  }

  vector<int> swaps;
  for (int i = 0; i < n; i++)
    if (reaches[i])
      swaps.push_back(swaps_to_reach[i]);

  sort(swaps.begin(), swaps.end());

  int v = 0;
  for (int i = 0; i < k; i++)
    v += swaps[i];

  printf("Case #%d: %d\n", CASE, v);
}

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; i++)
    solve(i+1);
  return 0;
}
