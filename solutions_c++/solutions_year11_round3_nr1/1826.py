#include <cstdio>

int main()
{
  int T, t;
  int X, Y;
  int x, y;
  char field[50][50];
  int todo;
  scanf("%d",&T);
  for(t=1;t<=T;t++)
  {
    scanf("%d %d\n", &Y, &X);
    todo = 0;
    for(y=0;y<Y;y++)
    {
      for(x=0;x<X;x++)
      {
        scanf("%c", &field[x][y]);
        if(field[x][y]=='#') todo++;
      }
      if(y!=Y-1) scanf("%*c");
    }

    for(y=0;y<Y-1;y++)
    {
      for(x=0;x<X-1;x++)
      {
        if(field[x][y]=='#' && field[x][y+1]=='#' && field[x+1][y]=='#' && field[x+1][y+1]=='#')
        {
          field[x][y] = '/';
          field[x][y+1] = '\\';
          field[x+1][y] = '\\';
          field[x+1][y+1] = '/';
          todo -= 4;
        }
      }
    }

    if(todo>0) printf("Case #%d:\nImpossible\n",t);
    else
    {
      printf("Case #%d:\n",t);
      for(y=0;y<Y;y++)
      {
        for(x=0;x<X;x++)
        {
          printf("%c", field[x][y]);
        }
        printf("\n");
      }
    }
  }

  return 0;
}

