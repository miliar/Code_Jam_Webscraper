#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

struct Order
{
  char color;
  int pos;
};

const int MAX = 110;
Order orders[MAX];
int t, n;

int next(char color, int pos, int start)
{
  for (int i = start; i < n; i++)
  {
    if (color == orders[i].color)
      return orders[i].pos;
  }
  return pos;
}

int main()
{
  scanf("%d", &t);
  for (int testcase = 1; testcase <= t; testcase++)
  {
    int seconds = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
      char c[2];
      scanf("%s %d", c, &orders[i].pos);
      orders[i].color = c[0];
    }

    int posO = 1, posB = 1;
    for (int i = 0; i < n; i++)
    {
      int nextO = next('O', posO, i);
      int nextB = next('B', posB, i);
      bool done = false;
      while (!done)
      {
        if (orders[i].color == 'O' && orders[i].pos == posO)
          done = true;//, printf("O pushed the button %d\n", posO);
        if (orders[i].color == 'B' && orders[i].pos == posB)
          done = true;//, printf("B pushed the button %d\n", posB);
        if (posO < nextO) posO++;//, printf("O went forward to %d\n", posO);
        else if (posO > nextO) posO--;//, printf("O went back to %d\n", posO);
        if (posB < nextB) posB++;//, printf("B went forward to %d\n", posB);
        else if (posB > nextB) posB--;//, printf("B went back to %d\n", posB);
        seconds++;
      }
    }

    printf("Case #%d: %d\n", testcase, seconds);
  }
  return 0;
}
