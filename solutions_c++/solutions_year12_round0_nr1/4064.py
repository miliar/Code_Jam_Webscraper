#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

FILE * fin = fopen ("A-small-attempt1.in", "r"), * fout = fopen ("A-small.out", "w");

char f[30] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

void work (int r)
{
     fprintf (fout, "Case #%d: ", r + 1);
     char code;
     //cin >> code;
     fscanf (fin, "%c", &code);
/*     for (int i = 0; code[i]; i ++)
     {
         if (code[i] != ' ')
            code[i] = f[code[i] - 'a'];
         fprintf (fout, "%c", code[i]);
     }*/
     while (code != '\n')
     {
           if (code != ' ')
              code = f [code - 'a'];
           fprintf (fout, "%c", code);
           fscanf (fin, "%c", &code);
     }
     fprintf (fout, "\n");
     return;
}

int main ()
{
    int t;
    //cin >> t;
    fscanf (fin, "%d", &t);
    char p;
    fscanf (fin, "%c", &p);
    for (int i = 0; i < t; i ++)
    {
        work (i);
    }
    return 0;
}
