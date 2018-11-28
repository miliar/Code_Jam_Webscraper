#include<stdio.h>
int pow2[40];

int main()
{
    int t,n,k,flag,i,temp,res,tt;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    i=0;
    while(t--)
    {
        i++;
        scanf("%d%d",&n,&k);
        if((k+1)%(1<<n)==0) flag=1;
        else flag=0;

        if(flag==0) printf("Case #%d: OFF\n",i);
        else printf("Case #%d: ON\n",i);
    }
    return 0;
}
