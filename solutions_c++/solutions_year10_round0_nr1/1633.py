#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int T,N,K;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
int i,j,flag;
    scanf("%d",&T);
    for (i=0;i<T;i++)
    {
        scanf("%d%d",&N,&K);
        flag = 1;
        for (j=0;j<N;j++)
        {
            if (1<<j & K)  //应该是按位与 ， 老大！！ 
            {}
            else
            {
                flag = 0;
                break;
            }
        }
        if (flag)
        printf("Case #%d: ON\n",i+1);
        else
        printf("Case #%d: OFF\n",i+1);
              
    }

return 0;
}

