#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
int k, n, l, h, a[110];
int main()
{
  freopen("B.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> k;
  for(int c = 0; c < k; c++)
  {
    int ans = -1;
    cin >> n >> l >> h;
    for(int i = 0; i < n; i++)
      cin >> a[i];
    for(int i = l; i <= h; i++)
    {
      bool flag = true;
      for(int j = 0; flag && j < n; j++)
        if (a[j] % i != 0 && i % a[j] != 0)
          flag = false;
      if (flag)
      {
        ans = i;
        break;
      }
    }
    printf("Case #%d: ", c + 1);
    if (ans == -1)
      cout << "NO" << endl;
    else
      cout << ans << endl;
  }
  return 0;
}