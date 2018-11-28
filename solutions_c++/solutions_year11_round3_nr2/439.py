#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("B-small.in", "r"), * fout = fopen ("B-small.out", "w");

void work(int r)
{
     fprintf (fout, "Case #%d: ", r);
     printf ("%d\n", r);
     int L, t, N, C;
     int dist[1000];
     fscanf (fin, "%d%d%d%d", &L, &t, &N, &C);
     for (int i = 0; i < C; i ++)
     {
         fscanf (fin, "%d", &dist[i]);
         printf ("%d ", dist[i]);
     }
     int time[1100][10];
     for (int i = 0; i < N; i ++)
     {
         time[0][i] = 0;
     }
     for (int i = 1; i <= N; i ++)
     {
         for (int j = 0; j <= L; j ++)
         {
             //fprintf(fout, "%d %d %d %d\n", i, j, time[i-1][j] + dist[(i - 1) % C] * 2, time[i - 1][j - 1] + dist[(i - 1) % C]);
             time[i][j] = time[i-1][j] + dist[(i - 1) % C] * 2;
             if (j > 0 && time[i-1][j-1] >= t && time[i - 1][j - 1] + dist[(i - 1) % C] < time[i][j])
                 time[i][j] = time[i - 1][j - 1] + dist[(i - 1) % C];
             if (j > 0 && time[i - 1][j - 1] < t && t + (dist[(i - 1)% C] - (t - time[i -1][j-1])/2) < time[i][j])
             {
                   time[i][j] = t + (dist[(i - 1)% C] - (t - time[i -1][j-1])/2);
             }
         }
     }
     fprintf (fout, "%d\n", time[N][L]);
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