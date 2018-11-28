#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

#define MAXN 110
int n;
char a[MAXN][MAXN];
int w[MAXN];
int t[MAXN];

double wp[MAXN];
double owp[MAXN], oowp[MAXN];

void pr(double a[])
{
     int i;
     for (i = 0; i < n; i++)
         printf ("%d: %lf\n", i, a[i]);
     printf ("\n");
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("1.out", "w", stdout);
    
    int i, j, csnum, cs;
    double twp, cwp, tmp;
    int tnum, cnum;
    
    scanf ("%d", &csnum);
    for (cs = 1; cs <= csnum; cs++)
    {
        scanf (" %d", &n);

        memset(wp, 0, sizeof(wp));
        memset(w, 0, sizeof(w));
        memset(t, 0, sizeof(t));

        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            {
                scanf (" %c", &a[i][j]);
                if (a[i][j] == '1')
                    w[i]++, t[i]++;
                else if (a[i][j] == '0')
                     t[i]++;
            }

            wp[i] = (double)w[i] / (double)t[i];
        }
        
        //puts("w");
       // for (i = 0; i < n; i++)
      //      printf ("%d: %d\n", i, w[i]);
      //  puts("t");
     //   for (i = 0; i < n; i++)
       //     printf ("%d: %d\n", i, t[i]);
            
        for (i = 0; i < n; i++)
        {
            twp = 0;
            tnum = 0;
            for (j = 0; j < n; j++)
            {
                if (i == j || a[i][j] == '.' || t[j] == 1) continue;
                
                tnum++;
                
                if (a[j][i] == '1')
                   twp += (double) (w[j] - 1) / (double)(t[j]-1);
                else
                   twp += (double) (w[j]) / (double)(t[j]-1);
            }
            owp[i] = twp / (double)tnum;
        }
        
        //puts("wp");
       // pr(wp);
       // puts("owp");
       //s pr(owp);
        
        for (i = 0; i < n; i++)
        {
            twp = 0;
            tnum = 0;
            for (j = 0; j < n; j++)
            {
                if (i == j || a[i][j] == '.') continue;
                
                tnum++;
                twp += owp[j];
            }
            oowp[i] = twp / (double)tnum;
        }
        
        printf ("Case #%d:\n", cs);
        for (i = 0; i < n; i++)
        {
            tmp = (wp[i] + 2.0 * owp[i] + oowp[i]) / 4.0;  
            printf ("%.7lf\n", tmp);
        }
    }
    
    //while(1);
}
/*
4
4
.11.
0.00
01.1
.10.
*/
