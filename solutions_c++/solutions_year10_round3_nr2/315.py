#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int t,l,p,c;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("BBBlarg.out","w",stdout);
    int k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d %d %d",&l,&p,&c);
        int num=0;
        while(l<p)
        {
            if(p%c==0)
                p/=c;
            else
                p=p/c+1;
            num++;
        }
        int ans=0;
        while(num!=1)
        {
            if(num%2==0)
                num/=2;
            else
                num=num/2+1;
            ans++;
        }
        printf("Case #%d: %d\n",k,ans);
    }
    //system("pause");
    return 0;
}
