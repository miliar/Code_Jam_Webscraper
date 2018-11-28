#include<cstdio>
#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

#define O 'O'
#define X 'X'
#define T 'T'
#define DOT '.'
#define NOT_COMP "Game has not completed"

char cell[5][5];
int n;
int cnt;
void won(char c)
{
  printf("Case #%d: %c won\n", cnt, c); 
}
void draw()
{
  printf("Case #%d: Draw\n", cnt);
}
void NotComp()
{
  printf("Case #%d: %s\n", cnt, NOT_COMP);
}

int main()
{
  cin >> n;
  for(cnt = 1; cnt <= n; cnt++)
  {
    for(int i = 0; i < 4; i++)
    {
      cin >> cell[i];
    }


    bool isNotFill = false;
    bool resO = true;
    bool resX = true;

    //横
    for(int i = 0; i < 4; i++)
    {
      for(int j = 0; j < 4; j++)
      {
        if(cell[i][j] == DOT)
          isNotFill = true;
        resO = resO && (cell[i][j] == O || cell[i][j] == T);
        resX = resX && (cell[i][j] == X || cell[i][j] == T);
      }
      if(resO)
      {
        won(O);
        goto loopend;
      }
      else if(resX)
      {
        won(X);
        goto loopend;
      }
      resO = resX = true;
    }
    //縦
    for(int j = 0; j < 4; j++)
    {
      for(int i = 0; i < 4; i++)
      {
        if(cell[i][j] == DOT)
          isNotFill = true;
        resO = resO && (cell[i][j] == O || cell[i][j] == T);
        resX = resX && (cell[i][j] == X || cell[i][j] == T);
      }
      if(resO)
      {
        won(O);
        goto loopend;
      }
      else if(resX)
      {
        won(X);
        goto loopend;
      }
      resO = resX = true;
    }
    //斜め
    for(int i = 0; i < 2; i++)
    {
      if(i == 0)
      {
        for(int j = 0; j < 4; j++)
        {
          if(cell[j][j] == DOT)
            isNotFill = true;
          resO = resO && (cell[j][j] == O || cell[j][j] == T);
          resX = resX && (cell[j][j] == X || cell[j][j] == T);
        }
      }
      else
      {
        for(int j = 0; j < 4; j++)
        {
          if(cell[j][3 - j] == DOT)
            isNotFill = true;
          resO = resO && (cell[j][3 - j] == O || cell[j][3 - j] == T);
          resX = resX && (cell[j][3 - j] == X || cell[j][3 - j] == T);
        }
      }
      if(resO)
      {
        won(O);
        goto loopend;
      }
      else if(resX)
      {
        won(X);
        goto loopend;
      }
      resO = resX = true;
    }

    if(isNotFill)
      NotComp();
    else
      draw();
loopend:;
  }

  return 0;
}
