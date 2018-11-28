#include <cstdio>
#include <cstdlib>

FILE * fin = fopen("C-small.in", "r"), * fout = fopen ("C-small.out", "w");

bool prime(int a)
{
     if (a == 2) return true;
    for (int i = 2; i * i <= a; i ++)
    {
        if (a % i == 0) return false;
    }
    return true;
}

void work(int r)
{
     fprintf (fout, "Case #%d: ", r);
     int N;
     fscanf (fin, "%d", &N);
     int times1 = 0;
     int primes[1000];
     int s = 0;
     for (int i = 2; i <= N; i ++)
     {
         if (prime(i))
         {
            primes[s] = i;
            s ++;
            times1 ++;
         }
     }
     if (s == 0) times1 = 1;
     int times2 = 1;
     for (int i = 0; i < s; i ++)
     {
         int app = 1;
         int p = primes[i];
         int s = p * p;
         while (s <= N)
         {
               app ++;
               s = s * p;
         }
         times2 += app;
     }
     fprintf (fout, "%d\n", times2 - times1);
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