#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("A-large.in", "r"),
	*fpo = fopen("A-large.out", "w");

int
	T,
   R,
   C;

char
   c,
   g[50][51];

bool replace()
{
   for (int y = 0; y < R; y++)
      for (int x = 0; x < C; x++)
         if (g[y][x] == '#')
            {
            g[y][x] = '/';

            if (x == C - 1 || g[y][x + 1] != '#')
               return false;

            g[y][x + 1] = '\\';

            if (y == R - 1 || g[y + 1][x] != '#')
               return false;

            g[y + 1][x] = '\\';

            if (g[y + 1][x + 1] != '#')
               return false;

            g[y + 1][x + 1] = '/';
            }

   return true;
}

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		bool
			bPoss = false;

		fscanf(fpi, "%d %d", &R, &C);

      for (int y = 0; y < R; y++)
         {
         for (int x = 0; x < C; x++)
            {
            while (true)
               {
               fscanf(fpi, "%c", &c);
               if (c == '.' || c == '#')
                  break;
               }

            g[y][x] = c;
            }

         g[y][C] = 0;
         }

      bPoss = replace();

		fprintf(fpo, "Case #%d:\n", i + 1);
      
      if (bPoss)
         for (int y = 0; y < R; y++)
            fprintf(fpo, "%s\n", g[y]);
      else
         fprintf(fpo, "Impossible\n");

		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
