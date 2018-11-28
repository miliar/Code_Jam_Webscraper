#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>                                                                               

using namespace std;

typedef vector <int> vi;
typedef pair <int, int> pii;
typedef long long ll;

int T;
int n, d[50000], l[50000], p;

int f[50000];

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    memset(f, 0, sizeof(f));
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
      scanf("%d %d", &d[i], &l[i]);
    l[n] = 10000000;
    scanf("%d", &d[n++]);
    
    f[0] = min(d[0], l[0]);

    for (int i = 0; i < n-1; ++i)
    {
      int j = i + 1;
      while (j < n && d[j] - d[i] <= f[i])
      {
        int c = min(d[j] - d[i], l[j]);
        f[j] = max(f[j], c);
        ++j;
      }
    } 
    if (f[n-1])
      printf("Case #%d: YES\n", t + 1);
    else
      printf("Case #%d: NO\n", t + 1);
  }
  return 0;
}
