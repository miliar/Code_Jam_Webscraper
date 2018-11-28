#include <stdio.h>

int n,t,k,pb,po,so,sb;
char s, s1, col;
int ans[1000];



int abs(int x)
{
    if (x>=0)
    {
        return x;
    }
    else
    {
       return x*(-1);
    }
}

int main()
{
   scanf("%d", &t);
   for (int i=1; i<=t; i++)
   {
       pb = 1;
       po = 1;
       so = 0;
       sb = 0;
       ans[0] = 0;
       scanf("%d", &n);
       for (int j=1; j<=n; j++)
       {
            scanf("%c%c%c%d", &s, &col, &s1, &k);
            if (col == 'O')
            {
                if ((abs(k - po) - ans[j-1] + so) > 0)
                {
                    ans[j] = abs(k - po) + so + 1;
                }
                else
                {
                    ans[j] = ans[j-1] + 1;
                }
                so = ans[j];
                po = k;
            }
            if (col == 'B')
            {
                if ((abs(k - pb) - ans[j-1] + sb) > 0)
                {
                    ans[j] = abs(k - pb) + sb + 1;
                }
                else
                {
                    ans[j] = ans[j-1] + 1;
                }
                sb = ans[j];
                pb = k;
            }
       }
       printf("Case #%d: %d\n", i, ans[n]);
    }
return 0;
}
