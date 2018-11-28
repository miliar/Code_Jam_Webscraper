#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-large.in", "r"), * fout = fopen ("A-large.out", "w");

void work(int T)
{
     fprintf (fout, "Case #%d:\n", T);
     printf ("%d", T);
     int N;
     fscanf (fin, "%d", &N);
     char a[100][100];
     for (int i = 0; i < N; i ++)
     {
         for (int j = 0; j < N; j ++)
         {
             fscanf (fin, "%c", &a[i][j]);
             if (a[i][j] == '\n') fscanf (fin, "%c", &a[i][j]);
             //fprintf (fout, "%c", a[i][j]);
         }
     }
     int win[100], play[100];
     for (int i = 0; i < N; i ++)
     {
         win[i] = 0;
         play[i] = 0;
         for (int j = 0; j < N; j ++)
         {
             if (a[i][j] == '1')
             {
                win[i] ++;
                play[i] ++;
             }
             if (a[i][j] == '0')
             {
                play[i] ++;
             }
         }
         //fprintf (fout, "i %d: win : %d play: %d\n", i, win[i], play[i]);
     }
     double WP[100], OWP[100];
     for (int i = 0; i < N; i ++)
     {
         WP[i] = win[i] / (play[i] + 0.0);
         OWP[i] = 0.0;
         for (int j = 0; j < N; j ++)
         {
             if (j == i) continue;
             //if (a[j][i] == '.') OWP[i] += win[j] / (play[j] + 0.0);
             if (a[j][i] == '1') OWP[i] += (win[j] - 1.0)/(play[j] - 1.0);
             if (a[j][i] == '0') OWP[i] += win[j] / (play[j] - 1.0);
         }
         OWP[i] = OWP[i] / (play[i] - 0.0);
         //fprintf (fout, "i %d WP %lf OWP %lf\n", i, WP[i], OWP[i]);
     }
     for (int i = 0; i < N; i ++)
     {
         double OOWP = 0.0;
         for (int j = 0; j < N; j ++)
         {
             if (j == i) continue;
             if (a[i][j] != '.') OOWP += OWP[j];
         }
         OOWP = OOWP / play[i];
         double RPI = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP;
         fprintf (fout, "%lf\n", RPI);
     }
     return;
}

int main ()
{
    int T;
    fscanf (fin, "%d", &T);
    for (int i = 0; i < T; i ++)
    {
        work (i + 1);
    }
    return 0;
}