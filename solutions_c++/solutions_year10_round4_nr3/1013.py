#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

int testID;
bool data[200][200];
bool newdata[200][200];

void deal()
{
  memset(data, false, sizeof(data));
  int R;
  scanf("%d", &R);
  while (R--)
  {
    int x1, x2, y1, y2;
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    for (int i = x1; i <= x2; ++i)
      for (int j = y1; j <= y2; ++j)
        data[i][j] = true;
  }

  int ans = 0;
  while (true)
  {
    for (int i = 0; i < 200; ++i)
      for (int j = 0; j < 200; ++j)
        newdata[i][j] = data[i][j];
    ans++;

    int count = 0;
    for (int i = 1; i <= 100; ++i)
      for (int j = 1; j <= 100; ++j)
      {
        if (data[i][j])
        {
          if (!data[i - 1][j] && !data[i][j - 1])
            newdata[i][j] = false;
        }
        else
        {
          if (data[i - 1][j] && data[i][j - 1])
            newdata[i][j] = true;
        }
        if (newdata[i][j])
          count++;
      }
    if (count == 0) break;

    for (int i = 0; i < 200; ++i)
      for (int j = 0; j < 200; ++j)
        data[i][j] = newdata[i][j];
  }
  cout << "Case #" << testID << ": " << ans << endl;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (testID = 1; testID <= T; ++testID)
    deal();
  return 0;
}
