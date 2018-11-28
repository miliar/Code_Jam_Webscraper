#include <stdio.h>

int main()
{
  int line;
  scanf("%d", &line);

  

  for(int i=0;i<line;i++)
  {
    int m;
    int x;
    int small;

    int total = 0;

//    printf("begin\n");
    scanf("%d",&m);
    for(int j=0;j<m;j++)
    {
      
      int tmp;
      scanf("%d", &tmp);
 //     printf("%d ", tmp);

      if(j == 0)
      {
        x = tmp;
        small = tmp;
        total += tmp;

      }
      else
      {
        if(tmp < small)
        {
          small = tmp;
        }
        x = x ^ tmp;
        total += tmp;
      }

    }

    if(x == 0)
    {
      printf("Case #%d: %d\n", i + 1, total - small);
    }
    else
    {
      printf("Case #%d: NO\n", i + 1);
    }


  }
}


