#include<stdio.h>
#include<stdlib.h>

int main()
{
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++)
  {
    int n;
    scanf("%d", &n);
    getchar();
    int overo = 0;
    int overb = 0;
    int sum = 0;
    int lasto = 1;
    int lastb = 1;
    for(int j = 0; j < n; j++)
    {
      char r;
      int p;
      scanf("%c%d", &r, &p);
      getchar();
      if(r == 'O')
      {
        int d = abs(p - lasto) + 1;
        if(overo >= d)
        {
          overo = 0;
          sum++;
          overb++;
          lasto = p; 
          continue;
        }
        else if(overo > 0)
        {
          d -= overo;
          overo = 0;
        }
        overb += d;
        sum += d;
        lasto = p;  
      }
      else
      {
        int d = abs(p - lastb) + 1;
        if(overb >= d)
        {
          overb = 0;
          sum++;
          overo++;
          lastb = p; 
          continue;
        }
        else if(overb > 0)
        {
          d -= overb;
          overb = 0;
        }
        overo += d;
        sum += d;
        lastb = p; 
      }
    }
    printf("Case #%d: %d\n", i, sum);
  }
  return 0;
}
