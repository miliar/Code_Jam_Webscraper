#include <cstdio>
#include <cstdlib>

FILE *fin = fopen ("D-large.in", "r"), *fout = fopen ("D-large.out", "w");

void work (int r)
{
     fprintf (fout, "Case #%d: ", r);
     int n;
     fscanf (fin, "%d", &n);
     int x[1000];
     for (int i = 0; i < n; i ++)
     {
         fscanf (fin, "%d", &x[i]);
     }
     int loop;
     bool inlist[1000];
     for (int i = 0; i < n; i ++)
     {
         inlist[i] = false;
     }
     double re = 0.0;
     for (int i = 0; i < n; i ++)
     {
         if (!inlist[i])
         {
            inlist[i] = true;
            loop = 0;
            int head = x[i];
            //fprintf (fout, "head %d %d:", i, head);
            int value = x[i];
            while (x[value - 1] != head)
            {
               inlist[value - 1] = true;
               value = x[value - 1];
               //fprintf (fout, "%d ", value);
               loop ++;
            }
            loop ++;
            re += (loop > 1? loop : 0);
         }
     }
     fprintf (fout, "%lf\n", re);
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
