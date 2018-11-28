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

int T, n, s, p;

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    scanf("%d %d %d", &n, &s, &p);
    int res = 0;
    for (int i = 0; i < n; ++i)
    {
      int x;
      scanf("%d", &x);
      bool b1 = false, b2 = false;
      for (int i1 = 0; i1 <= 10; ++i1)
        for (int i2 = i1; i2 >= 0 && i2 >= i1 - 2; --i2)
          for (int i3 = i1; i3 >= 0 && i3 >= i1 - 2; --i3)
          {
            if (i1 + i2 + i3 == x && i1 >= p)
            {
              b1 = true;
              if (i1 - 2 < i2 && i1 - 2 < i3)
                b2 = true;
            } 
          }
      if (b2) ++res;
      else if (b1 && s > 0)
      {
        --s;
        ++res;
      }
    }
    printf("Case #%d: %d\n", t+1, res);
  }
  return 0;
}