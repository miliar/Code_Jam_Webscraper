#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-small.in", "r"), * fout = fopen ("A-small.out", "w");

void work(int r)
{
     fprintf (fout, "Case #%d: ", r);
     printf ("%d", r);
     int X, S, R, t, N;
     fscanf (fin, "%d%d%d%d%d", &X, &S, &R, &t, &N);
     //fprintf (fout, "\nS: %d, R: %d\n", S, R);
     int B[1000], E[1000], w[2000];
     double l[2000];
     double ari[1000];
     int s = 0;
     int end = 0;
     for (int i = 0; i < N; i ++)
     {
         int sp;
         fscanf (fin, "%d%d%d", &B[i], &E[i], &sp);
         if (B[i] != end)
         {
            l[s] = B[i] - end;
            w[s] = 0;
            s ++;
         }
         l[s] = E[i] - B[i];
         end = E[i];
         w[s] = sp;
         s ++;
     }
     if (E[N - 1] != X)
     {
             l[s] = X - E[N - 1];
             w[s] = 0;
             s ++;
     }
     for (int i = 0; i < s; i ++)
     {
         for (int j = i + 1; j < s; j ++)
         {
             if (w[j] < w[i])
             {
                double tmp = l[i];
                l[i] = l[j];
                l[j] = tmp;
                int tmpi = w[i];
                w[i] = w[j];
                w[j] = tmpi;
             }
         }
     }
     double cost = 0.0;
     int head = 0;
     double precost = 0.0;
     double tt = t;
     while (head < s)
     {
           if (tt * (R + w[head]) > l[head])
           {
                 tt -= (l[head] + 0.0) / (0.0 + R + w[head]);
                 cost = cost + (l[head] + 0.0) / (0.0 + R + w[head]);
                 head ++;
           }
           else
           {
                 cost = cost + tt + (l[head] - (R + w[head]) * tt) / (S + w[head]);
                 tt = 0;
                 head ++;
           }
       //    fprintf (fout, "\n l: %lf, w: %d, cost: %lf", l[head - 1], w[head - 1], cost - precost);
           precost = cost;
     }
     fprintf (fout, "%lf\n", cost);
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