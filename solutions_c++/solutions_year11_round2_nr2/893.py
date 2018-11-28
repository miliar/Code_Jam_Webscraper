#include <stdio.h>


int t,t1,c,d,q;
int p[100];
int v[100];
int r[10000];

int main()
{

    scanf("%d", &t1);
    for (int i=1; i<=t1; i++)
    {
        t=0;
        scanf("%d%d", &c,&d);
        for (int j=1; j<=c; j++)
        {
            scanf("%d%d", &p[j], &v[j]);
            for (int k=1; k<=v[j]; k++)
            {
                t++;
                r[t] = p[j];
            }
        }

        for (int j=1; j<=t; j++)
        {
           for (int k=j+1; k<=t; k++)
           {
               if (r[j] > r[k])
               {
                   int tmp;
                   tmp = r[j];
                   r[j] = r[k];
                   r[k] = tmp;
               }
           }
        }
        double j;
        j=0;
        while (j<=100000)
        {
        int check =1;
        double cur=-100000000;
            for (int i1=1; i1<=t; i1++)
            {
                if (r[i1] - j >= cur + d)
                {
                    cur = r[i1] - j;
                }
                else
                {
                    cur = cur+d;
                }
                if (cur > r[i1] + j)
                {
                    check = 0;
                }
            }
        if (check==1)
        {
            break;
        }
        j = j+0.5;
        }
        printf("Case #%d: %.1lf\n", i,j);
    }
}
