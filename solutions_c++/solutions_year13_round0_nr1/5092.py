#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char b[4][4];

bool check(char player)
{
  bool rtn;
  for(int i = 0; i < 4; i++)
    {
      rtn = true;
      for (int j = 0; j < 4; j++)
	rtn &= (player == b[i][j] || 'T' == b[i][j]);
      if (rtn) return true;
      rtn = true;
      for (int j = 0; j < 4; j++)
	rtn &= (player == b[j][i] || 'T' == b[j][i]);
      if (rtn) return true;
    }
  rtn = true;
  for (int i = 0; i < 4; i++)
    rtn &= (player == b[i][i] || 'T' == b[i][i]);
  if (rtn) return true;
  rtn = true;
  for (int i = 0; i < 4; i++)
    rtn &= (player == b[i][3-i] || 'T' == b[i][3-i]);
  return rtn;
}

bool full()
{
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (b[i][j] == '.')
	return false;
  return true;
}

int main()
{ 
  int T;
  scanf("%d",&T);
  for (int t = 1; t <= T; t++)
    {
      for (int i = 0; i < 4; i++)
	scanf("%s",b[i]);
      printf("Case #%d: ",t);
      if (check('X'))
	printf("X won\n");
      else if (check('O'))
	printf("O won\n");
      else if (full())
	printf("Draw\n");
      else
	printf("Game has not completed\n");
    }
  return 0;
}
