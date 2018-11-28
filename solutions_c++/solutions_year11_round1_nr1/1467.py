#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-small.in", "r"), * fout = fopen ("A-small.out", "w");

int GCD(int a, int b)
{
    if (a == 1 || b == 1) return 1;
    if (a > b)
    {
          int tmp = a;
          a = b;
          b = tmp;
    }
    while (a > 0)
    {
          b = b % a;
          int tmp = a;
          a = b;
          b = tmp;
    }
    return b;
}

void work(int T)
{
     fprintf (fout, "Case #%d: ", T);
     int PG, PD, N;
     fscanf (fin, "%d%d%d", &N, &PD, &PG);
     if (100 / GCD(100, PD) <= N && (PD == 100 || (PD != 100 && PG != 100)) && (PG != 0 || (PG == 0 && PD == 0))){
             fprintf (fout, "Possible\n");
             return;
             }
     fprintf (fout, "Broken\n");
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