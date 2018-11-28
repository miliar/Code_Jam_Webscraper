#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int
	T;

int check_line(char a, char b, char c, char d, char player)
{
   if (a != player && a != 'T')
      return (0);

   if (b != player && b != 'T')
      return (0);

   if (c != player && c != 'T')
      return (0);

   if (d != player && d != 'T')
      return (0);

   return (1);
}

int check_win(char b[4][5], char player)
{
   for (int i = 0; i < 4; i++)
      if (check_line(b[i][0], b[i][1], b[i][2], b[i][3], player))
         return (1);

   for (int i = 0; i < 4; i++)
      if (check_line(b[0][i], b[1][i], b[2][i], b[3][i], player))
         return (1);

   if (check_line(b[0][0], b[1][1], b[2][2], b[3][3], player))
      return (1);

   if (check_line(b[0][3], b[1][2], b[2][1], b[3][0], player))
      return (1);

   return (0);
}

int check_draw(char b[4][5])
{
   for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
         if (b[i][j] == '.')
            return (0);

   return (1);
}

int main(int argc, char *argv[])
{
   FILE
	   *fpi = fopen("A-large.in", "r"),
	   *fpo = fopen("A-large.out", "w");

	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
      char
         b[4][5];

		for (int j = 0; j < 4; j++)
		   fscanf(fpi, "%s", &b[j][0]);

      fprintf(fpo, "Case #%d: ", i + 1);

      if (check_win(b, 'X'))
         fprintf(fpo, "X won\n");
      else if (check_win(b, 'O'))
         fprintf(fpo, "O won\n");
      else if (check_draw(b))
         fprintf(fpo, "Draw\n");
      else
         fprintf(fpo, "Game has not completed\n");
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
