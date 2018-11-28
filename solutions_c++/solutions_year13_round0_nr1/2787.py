#include <stdlib.h>
#include <stdio.h>

#define MSG_X_WON "X won"
#define MSG_O_WON "O won"
#define MSG_DRAW "Draw"
#define MSG_GAME_NOT_COMPLETED "Game has not completed"

int max_letter(unsigned char game[4][4], char x)
{
  int i, j;
  int cnt[4];
  i = 0;
  cnt[0] = 0;
  cnt[1] = 0;
  cnt[2] = 0;
  cnt[3] = 0;
  while (i < 4)
    {
      j = 0;
      while (j < 4)
	{
	  if (game[i][j] == 'T' ||  game[i][j] == x)
	    ++cnt[0];
	  if (game[j][i] == 'T' ||  game[j][i] == x)
	    ++cnt[1];
	  ++j;
	}
      if (cnt[0] == 4 || cnt[1] == 4)
	return (1);
      cnt[0] = 0;
      cnt[1] = 0;
      if (game[i][i] == 'T' ||  game[i][i] == x)
      	++cnt[2];
      if (game[i][3 - i] == 'T' ||  game[i][3 - i] == x)
	++cnt[3];
      ++i;
    }
  if (cnt[2] == 4 || cnt[3] == 4)
    return (1);
  return (0);
}

const char *check_game(unsigned char game[4][4], int free_space)
{
  if (max_letter(game, 'X'))
    return (MSG_X_WON);
  if (max_letter(game, 'O'))
    return (MSG_O_WON);
  if (free_space > 0)
    return (MSG_GAME_NOT_COMPLETED);
  return (MSG_DRAW);
}

int	main(void)
{
  int T, iT, i, j, k, free_space, c;
  unsigned char game_l[21];
  unsigned char game_m[4][4];

  scanf("%d", &T);
  getc(stdin);
  iT = 0;
  while (iT < T)
    {
      fread(game_l, sizeof(unsigned char), 21, stdin);
      free_space = 0;
      i = 0;
      k = 0;
      while (i < 4)
	{
	  j = 0;
	  while (j < 4)
	    {
	      game_m[i][j] = game_l[k];
	      if (game_l[k] == '.')
		++free_space;
	      ++k;
	      ++j;
	    }
	  ++k;
	  ++i;
	}
      printf("Case #%d: %s\n", iT + 1, check_game(game_m, free_space));
      ++iT;
    }
  return (EXIT_SUCCESS);
}
