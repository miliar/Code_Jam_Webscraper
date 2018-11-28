#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

int n;

vector< int > p, l;
vector< int > s;

inline bool qwe(const int &a, const int &b)
{
  if (p[a] * l[a] != p[b] * l[b])
    return p[a] * l[a] > p[b] * l[b];
  if (p[a] == p[b])
  {
    if (l[a] != l[b] && p[a])
      return l[a] < l[b];
    return a < b;
  }
  else if (p[a] != p[b])
    return p[a] > p[b];
  else
    return a < b;
}

inline void solve(int testnum)
{
  s.clear();
  scanf("%d", &n);
  p.resize(n);
  l.resize(n);
  s.resize(n);
  for (int i = 0; i < n; i++)
    scanf("%d", &l[i]);
  for (int i = 0; i < n; i++)
    scanf("%d", &p[i]);
  for (int i = 0; i < n; i++)
    s[i] = i;
  
  stable_sort(s.begin(), s.end(), qwe);
  
  printf("Case #%d: ", testnum+1);
  for (int i = 0; i < n; i++)
    printf("%d ", s[i]);
  printf("\n");
}

int main()
{
  int testkol;
  scanf("%d\n", &testkol);
  for (int i = 0; i < testkol; i++)
    solve(i);
}