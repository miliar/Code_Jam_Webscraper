#include <stdio.h>

int n,t,c,d,q,k,g;
char s;
char ans[1000];
char a[1000][40], b[1000][40];

int pos(char ans[1000], char x)
{
    for (int i=1; i<=q; i++)
    {
        if (ans[i]==x)
        {
            return 1;
        }
    }
    return 0;
}


int main()
{
   scanf("%d", &t);
   for (int i=1; i<=t; i++)
   {
       q = 0;
       ans[0] = '1';
       scanf("%d", &c);
       for (int j=1; j<=c; j++)
       {
            scanf("%c%c%c%c", &s, &a[j][1], &a[j][2], &a[j][3]);
       }
       scanf(" %d", &d);
       for (int j=1; j<=d; j++)
       {
           scanf("%c%c%c", &s, &b[j][1], &b[j][2]);
       }
       scanf(" %d", &n);
       scanf("%c", &s);
       for (int j=1; j<=n; j++)
       {
          scanf("%c", &s);
          q++;
          ans[q] = s;
          for (k=1; k<=c; k++)
          {
             if (((ans[q] == a[k][1]) and (ans[q-1] == a[k][2])) or ((ans[q] == a[k][2]) and (ans[q-1] == a[k][1])))
             {
                 q--;
                 ans[q] = a[k][3];
             }
          }
          for (k=1; k<=d; k++)
          {
             if ((pos(ans, b[k][1]) > 0) and (pos(ans, b[k][2]) > 0))
                {
                    q = 0;
                }
          }
       }

        printf("Case #%d: [", i);
        for (k=1; k<q; k++)
        {
            printf("%c, ", ans[k]);
        }
        if (q>0)
        {
            printf("%c", ans[q]);
        }
        printf("]\n");
    }
return 0;
}
