#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

FILE *fout = fopen ("A-large.out", "w");

char pattern[500][15][26];
char word[5000][15];
int l,d,n;

void readPattern(int a, int b)
{
     if (b == l)
     {
           return;
     }
     char c;
     cin >> c;
     if (c == '(')
     {
          int t = 0;
          cin >> c;
          while (c != ')')
          {      
                 pattern[a][b][t] = c;
                 t ++;
                 cin >> c;
          }
          readPattern (a,b + 1);
          return;
     }
     pattern[a][b][0] = c;
     readPattern (a, b + 1);
     return;
}

bool in (char a, char b[])
{
     for (int i = 0; b[i] != 0; i ++)
     {
         if (a == b[i])
            return true;
     }
     return false;
}

void work (int a)
{
     int re = 0;
     for (int i = 0; i < d; i ++)
     {
         bool match = true;
         for (int j = 0; j < l; j ++)
         {
             if (!in (word[i][j], pattern[a][j]))
             {
                     match = false;
                     break;
             }
         }
         if (match)
         {
                   re ++;
         }
     }
     fprintf (fout, "Case #%d: %d\n", a + 1, re);
     return;
}

int main ()
{
    scanf ("%d%d%d",&l,&d,&n);
    for (int i = 0; i < d; i ++){
        for (int j = 0; j < l; j ++){
            cin >> word[i][j];
        }
    }
    for (int i = 0; i < n; i ++){
        readPattern (i, 0);
    }
    for (int i = 0; i < n; i ++){
        work (i);
    }
    return 0;
}
