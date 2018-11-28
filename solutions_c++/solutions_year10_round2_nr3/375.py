#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

int T;

int n;

vi v;

int res = 0;

int q[50];

void gen(int st, int x)
{
  if (x > n)
  {
    int i = n;
    while (i != -1 && i != 1)
    {
      i = q[i];
    }
    if (i == 1)
      ++res;
    if (res >= 100003)
      res -= 100003;
    return;
  }
  gen(st, x + 1);
  q[x] = st;
  gen(st + 1, x + 1);
  q[x] = -1;
  

}

int ans[50];

int main()
{
  for (n = 2; n <= 25; ++n)
  {
    memset(q, -1, sizeof(q));
    res = 0;
    gen(1, 2);
    ans[n] = res;
    
  }

  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    int a;
    scanf("%d", &a);
    printf("Case #%d: %d\n", t+1, ans[a]);
  }

  return 0;
}