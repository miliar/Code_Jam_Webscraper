#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-large.in", "r"), * fout = fopen ("A-large.out", "w");

void work(int r)
{
     fprintf (fout, "Case #%d:\n", r);
     printf ("%d", r);
     int R, C;
     fscanf (fin, "%d%d", &R, &C);
     //printf ("%d%d", R, C);
     char grid[100][100];
     for (int i = 0; i < R; i ++)
     {
         //fscanf (fin, "%s", &grid[i]);
         for (int j = 0; j < C; j ++)
         {
             fscanf (fin, "%c", &grid[i][j]);
             if (grid[i][j] == '\n' || grid[i][j] == ' ') 
                fscanf (fin, "%c", &grid[i][j]);
         }
     }
     for (int i = 0; i < R; i ++)
     {
         for (int j = 0; j < C; j ++)
         {
       //      printf ("%c", grid[i][j]);
             if (grid[i][j] == '#')
             {
                if (i == R - 1 || j == C - 1)
                {
                      fprintf (fout, "Impossible\n");
                      return;
                }
                if (grid[i + 1][j] == '#' && grid[i+1][j+1] == '#' && grid[i][j+1] == '#')
                {
                   grid[i][j] = '/';
                   grid[i + 1][j + 1] = '/';
                   grid[i +1][j] = grid[i][j + 1] = '\\';
                }
                else
                {
                    fprintf (fout, "Impossible\n");
                    return;
                }
             }
         }
     } 
     for (int i = 0; i < R; i ++)
     {
         for (int j = 0; j < C; j ++)
         {
             fprintf (fout, "%c", grid[i][j]);
         }
         fprintf (fout, "\n");
     }
     return;
}

int main ()
{
    int T;
    fscanf (fin, "%d", &T);
   // printf ("%d", T);
    for (int i = 0; i < T; i ++)
    {
        work (i + 1);
    }
    return 0;
}