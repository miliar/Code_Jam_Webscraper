#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-large.in", "r"), *fout = fopen ("A-large.out", "w");

void work (int r)
{
     fprintf (fout, "Case #%d: ", r);
     int n;
     fscanf (fin, "%d", &n);
     char color[100];
     int buttonB[100], buttonO[100];
     int j = 0, k = 0;
     for (int i = 0; i < n; i ++)
     {
         fscanf (fin, "%c", &color[i]);
         if (color[i] == ' ') fscanf (fin, "%c", &color[i]);
         if (color[i] == 'B')
         {
            fscanf (fin, "%d", &buttonB[j]);
            //fprintf (fout, "B %d %d\n", j, buttonB[j]);
            j ++;
         }
         else
         {
             fscanf (fin, "%d", &buttonO[k]);
             //fprintf (fout, "O %d %d\n", k, buttonO[k]);
             k ++;
         }
     }
     j = k = 0;
     int posB = 1, posO = 1;
     int time = 0;
     for (int i = 0; i < n; i ++)
     {
         //fprintf (fout, "%d %d %d\n", i, posB, posO);
         char tmp = color[i];
         if (tmp == 'B')
         {
            while (posB != buttonB[j])
            {
                  if (posB < buttonB[j]) posB ++;
                  else posB --;
                  if (posO < buttonO[k]) posO ++;
                  else if (posO > buttonO[k]) posO --;
                  time ++;
            }
            if (posO < buttonO[k]) posO ++;
            else if (posO > buttonO[k]) posO --;
            time ++;
            j ++;
         }
         else
         {
             while (posO != buttonO[k])
             {
                   if (posO < buttonO[k]) posO ++;
                   else posO --;
                   if (posB < buttonB[j]) posB ++;
                   else if (posB > buttonB[j]) posB --;
                   time ++;
             }
             if (posB < buttonB[j]) posB ++;
             else if (posB > buttonB[j]) posB --;
             time ++;
             k ++;
         }
     }
     fprintf (fout, "%d\n", time);
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