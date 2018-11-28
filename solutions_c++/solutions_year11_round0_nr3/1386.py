#include <cstdio>
#include <cstdlib>

FILE * fin = fopen("C-large.in","r"), *fout = fopen("C-large.out", "w");

void work (int r)
{
     fprintf (fout, "Case #%d: ", r);
     int n;
     fscanf (fin, "%d", &n);
     int a[1000];
     int p = 0;
     int mini = 10000000;
     int sum = 0;
     for (int i = 0; i < n; i ++)
     {
         fscanf (fin, "%d", &a[i]);
         sum += a[i];
         p = p xor a[i];
         if (a[i] < mini)
            mini = a[i];
     }
     if (p == 0)
     {
           fprintf (fout, "%d\n", sum - mini);
           return;
     }
     else
     {
         fprintf (fout, "NO\n");
         return;
     }
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