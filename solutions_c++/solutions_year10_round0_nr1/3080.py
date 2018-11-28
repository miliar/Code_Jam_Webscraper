#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int t;
int n,k;

int main()
{
freopen("A-large.in","r",stdin);
freopen("out.txt","w",stdout);
    int i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d",&n,&k);
        if((k+1)%((int)pow(2,n))==0)
            printf("Case #%d: ON\n",i);
        else
            printf("Case #%d: OFF\n",i);
    }
    return 0;
}
