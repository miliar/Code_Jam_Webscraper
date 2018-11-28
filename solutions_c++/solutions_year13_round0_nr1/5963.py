
#include <iostream>
#include <cstdio>

using namespace std;

char plansza[4][4];

bool check(char p)
{
  int ile = 0;  
  for (int i = 0; i < 4; i++)
  {
    ile = 0;
    for (int j = 0; j < 4; j++)
    {
      if (plansza[i][j] == p || plansza[i][j] == 'T')
      {
        ile++; 
      }
    }
    if (ile == 4) return true;

    ile = 0;
    for (int j = 0; j < 4; j++)
    {
      if (plansza[j][i] == p || plansza[j][i] == 'T')
      {
        ile++; 
      }
    }
    if (ile == 4) return true;
  }
  
  ile = 0;
  for (int j = 0; j < 4; j++)
  {
    if (plansza[j][j] == p || plansza[j][j] == 'T')
    ile++;
  }
  if (ile == 4) return true;

  ile = 0;
  for (int j = 0; j < 4; j++)
  {
    if (plansza[j][3 - j] == p || plansza[j][3 - j] == 'T')
    ile++;
  }
  if (ile == 4) return true;
  
  return false;

}

int main()

{
  int T;
  scanf("%d", &T);
  
  for (int i = 0; i < T; i++)
  {
    bool notfinish = false;
    
    for (int j = 0; j < 4; j++)
      scanf("%s", plansza[j]);
      
    int ileX = 0;
    int ileO = 0;
      
      
    for (int j = 0; j < 4; j++)
    for (int k = 0; k < 4; k++)
    {
     if (plansza[j][k] == '.')
       notfinish = true;
    }

  
  
    if (check('X'))
    {
      printf("Case #%d: X won\n", i + 1);
    }else
    if (check('O'))
    {
      printf("Case #%d: O won\n", i + 1);
    }
    else if (notfinish)
    {
      printf("Case #%d: Game has not completed\n", i + 1);
    }
    else
    {
      printf("Case #%d: Draw\n", i + 1);
    }
  }
  return 0;
}
