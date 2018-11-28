#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>

int main()
{
  int qnum = 0;
  scanf("%d", &qnum);

  int x = 0;
  while (qnum--)
    {
      x++;
  int y = 0;

  int N;
  long K;

  scanf("%d", &N);
  scanf("%d", &K);

  long n2 = 1 << N;
  int i;

  long d = (K + 1) % n2;
  if (K != 0 && d == 0)
    {
      y = 1;
    }
  else
  {
    y = 0;
  }

  printf("Case #%d: %s\n", x, y ? "ON" : "OFF");
    }
}
