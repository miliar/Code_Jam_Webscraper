#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int CAS;
int n,pd,pg;
int p,q;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        scanf("%d%d%d",&n,&pd,&pg);
        if(pg == 0 && pd != 0)
        {
            printf("Case #%d: Broken\n",cas);
            continue;
        }
        else if(pg == 100 && pd != 100)
        {
            printf("Case #%d: Broken\n",cas);
            continue;
        }
        else
        {
            p = pd;q = 100;
            for(int i = 2;i <= 100;)
            {
                if((q % i == 0) && (p % i == 0))
                {
                    q = q/i;
                    p = p/i;
                }
                else i++;
            }
            if(q <= n)
                printf("Case #%d: Possible\n",cas);
            else printf("Case #%d: Broken\n",cas);
            //printf("p:%d q:%d\n",p,q);
        }
    }
    fclose(stdin);
    fclose(stdout);
}
