#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int T,pd,pg;
long long n;
int en(int key,int p)
{
    int temp=key;
    key=1;
    for(int i=0;i<p;i++)
        key=temp*key;
    return key;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int case_cnt=0;
    while(T--)
    {
        scanf("%lld%d%d",&n,&pd,&pg);
        printf("Case #%d: ",++case_cnt);
        if(pg==100)
        {
            if(pd!=100)
            {
                puts("Broken");
                continue;
            }
        }
        else if(pg==0)
        {
            if(pd!=0)
            {
                puts("Broken");
                continue;
            }
        }

        int t1=0,f1=0,t2=0,f2=0,temp=1;
        for(t1=0;t1<=2;t1++)
        {
            temp=temp<<1;
            if(pd%temp!=0) break;
        }
       temp=1;;
        for(f1=0;f1<=2;f1++)
        {
            temp=temp*5;
            if(pd%temp!=0) break;
        }
       temp=1;

        for(t2=0;t2<=2;t2++)
        {
            temp=temp<<1;
            if(pg%temp!=0) break;
        }
        temp=1;;
        for(f2=0;f2<=2;f2++)
        {
            temp=temp*5;
            if(pg%temp!=0) break;
        }
        temp=1;

        if((long long)en(2,2-t1)*en(5,2-f1)<=n)
        {
            puts("Possible");
        }

        else puts("Broken");
    }
}
