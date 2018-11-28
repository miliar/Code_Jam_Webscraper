#include<cstdio>


int main ()
{
        int tt;
        scanf("%d",&tt);
        for(int pp=0;pp<tt;pp++)
        {
                int n,k;
                scanf("%d %d",&n,&k);
                int aux= (1<<n);
               // printf("%d\n",aux);
                printf("Case #%d: ",pp+1);

                if(k%aux==aux-1)
                    printf("ON\n");
                else
                    printf("OFF\n");
        }
        return 0;
}
