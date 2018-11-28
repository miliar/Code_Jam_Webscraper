#include <cstdio>

using namespace std;

int grid[5][5];

//0 -> empty
//1 -> O
//1 -> X
//2 -> T

bool check(int a)
{
  bool e;
  //scorri righe
  for (int i=0; i<4; i++)
  {
    e = true;
    for (int j=0; j<4; j++)
    {
      if (grid[i][j] != a)
        e = false;
    }
    if (e)
      return true;
  }
  //scorri colonne
  for (int j=0; j<4; j++)
  {
    e = true;
    for (int i=0; i<4; i++)
    {
      if (grid[i][j] != a)
        e = false;
    }
    if (e)
      return true;
  }
  //diagonale
  e = true;
  for (int i=0; i<4; i++)
  {
    if (grid[i][i] != a)
      e = false;
  }
  if (e)
    return true;
  e = true;
  for (int i=0; i<4; i++)
  {
    if (grid[i][3-i] != a)
      e = false;
  }
  if (e)
    return true;
  return false;
}

int main()
{
  int t, tr, tc;
  char temp;
  bool finished;
  scanf("%d\n",&t);
  for (int k=0; k<t; k++)
  {
    tr = 4; tc = 4;
    finished = true;
    for (int i=0; i<4; i++)
    {
      for (int j=0; j<4; j++)
      {
        scanf("%c\n",&temp);
        if (temp=='T')
        {
          tr = i;
          tc = j;
          grid[i][j] = 3;
        }
        else if (temp=='X')
          grid[i][j] = 2;
        else if (temp=='O')
          grid[i][j] = 1;
        else
        {
          finished = false;
          grid[i][j] = 0;
        }
      }
      scanf("\n");
    }
    scanf("\n");
    /*
    for (int i=0; i<4; i++)
    {
      for (int j=0; j<4; j++)
      {
        printf("%d ",grid[i][j]);
      }
      printf("\n");
    }
    printf("\n");*/
    printf("Case #%d: ",k+1);
    grid[tr][tc] = 1;
    if (check(1))
    {
      printf("O won\n");
      continue;
    }
    grid[tr][tc] = 2;
    if (check(2))
    {
      printf("X won\n");
      continue;
    }
    if (finished)
    {
      printf("Draw\n");
    }
    else
    {
      printf("Game has not completed\n");
    }
  }
  return 0;
}
