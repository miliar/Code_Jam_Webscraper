#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("C-small.in", "r"), * fout = fopen ("C-small.out", "w");

void work(int r)
{
     fprintf (fout, "Case #%d: ", r);
     int N, L, H;
     fscanf (fin, "%d%d%d", &N, &L, &H);
     int other[100];
     for (int i = 0; i < N; i ++)
     {
         fscanf (fin, "%d", &other[i]);
     }
     for (int s = L; s <= H; s ++)
     {
         bool ham = true;
         for (int t = 0; t < N; t ++)
         {
             if (s % other[t] != 0 && other[t] % s != 0)
             {
                   ham = false;
                   break;
             }
         }
         if (ham)
         {
                 fprintf (fout, "%d\n", s);
                 return;
         }
     }
     fprintf (fout, "NO\n");
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