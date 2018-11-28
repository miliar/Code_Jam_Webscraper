#include <cstdio>
#include <algorithm>
using std::max;

char board[4][4];

bool check(char p)
{
  int sum = 0;
  for (int i=0; i<4; i++)
    {
      sum = 0;
      for (int j=0; j<4; j++)
	sum += (board[i][j] == p || board[i][j] == 'T');
      if (sum == 4)
	return true;
    }
  for (int i=0; i<4; i++)
    {
      sum = 0;
      for (int j=0; j<4; j++)
	sum += (board[j][i] == p || board[j][i] == 'T');
      if (sum == 4)
	return true;
    }
  sum = 0;
  for (int i=0; i<4; i++)
    sum += (board[i][i] == p || board[i][i] == 'T');
  if (sum == 4)
    return true;
  sum = 0;
  for (int i=0; i<4; i++)
    sum += (board[i][3-i] == p || board[i][3-i] == 'T');
  if (sum == 4)
    return true;
  return false;
}

char calc()
{
  if (check('X'))
    return 'X';
  if (check('O'))
    return 'O';
  for (int i=0; i<4; i++)
    for (int j=0; j<4; j++)
      if (board[i][j] == '.')
	return 'G';
  return 'D';
}

int main()
{
  int t;
  scanf("%d",&t);
  for (int i=1; i<=t; i++)
    {
      for (int j=0; j<4; j++)
	scanf("%s\n",board[j]);
      scanf("\n");
      char result = calc();
      printf("Case #%d: ",i);
      switch(result) 
	{
	case 'X': printf("X won\n"); break;
	case 'O': printf("O won\n"); break;
	case 'D': printf("Draw\n"); break;
	case 'G': printf("Game has not completed\n"); break;
	}
    }
}
