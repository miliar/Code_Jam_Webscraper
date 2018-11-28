#include <stdio.h>
















int a[10000];
int l,h,n,t1,t;
int check;


int main()
{

    //freopen("C-small-attempt0 (1).in","r",stdin);
    //freopen("output.txt","w",stdout);













	                                            
	scanf("%d", &t1);
    for (int i=1; i<=t1; i++)
    {
        scanf("%d%d%d", &n,&l,&h);
        for (int j=1; j<=n; j++)
        {
            scanf("%d", &a[j]);
        }
        for (int j=l; j<=h; j++)
        {
            check =1;
            for (int k=1; k<=n; k++)
            {
                 if (j % a[k] != 0 && a[k] % j != 0)
                {
                    check = 0;
                }
                if (j==h && k==n && check==0)
                {
                    printf("Case #%d: NO\n", i);
                }
            }

         if (check == 1)
         {
             printf("Case #%d: %d\n", i, j);
             break;
         }

        }

    }
}

		