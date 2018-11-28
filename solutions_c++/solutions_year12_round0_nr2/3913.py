#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("B-large.in", "r"), * fout = fopen ("B-large.out", "w");

void work ()
{
     int N, S, p;
     fscanf (fin, "%d%d%d", &N, &S, &p);
     int good = 0, surp = 0;
     if (p == 0)
     {
           int score;
           for (int i = 0; i < N; i ++)
               fscanf (fin, "%d", &score);
           fprintf (fout, "%d\n", N);
           return;
     }
     for (int i = 0; i < N; i ++)
     {
         int score;
         fscanf (fin, "%d", &score);
         if (score >= 3 * p - 2 && score > 0) 
         {
            good ++;
         }
         else if (score >= 3 * p - 4 && score > 0) 
         {
              surp ++;
         }
     }
     if (surp > S) surp = S;
     fprintf (fout, "%d\n", good + surp);
     return;
}

int main ()
{
    int t;
    fscanf (fin , "%d", &t);
    for (int i = 0; i < t; i ++)
    {
        fprintf (fout, "Case #%d: ", i + 1);
        work ();
    }
    return 0;
}
