#include<stdio.h>
int func(int n,int A,int B)
{
    int k=n,i=0;
    int n10=1;
    int ret=0;
    while(k)
    {
        n10*=10;
        k=k/10;
        i++;
    }
    n10/=10;
    k=n;
    for(int j=0;j<i-1;j++)
    {
        int r=k%10;
        k=k/10+n10*r;

        if(k>n && k<=B)
        {
            ret++;
          //  printf("%d\n",k);
        }

    }
    return ret;
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int itr=1;itr<=T;itr++)
    {
        int A,B;
        scanf("%d %d",&A,&B);
        int ans=0;
        for(int i=A;i<=B;i++)
        {
            ans=ans+func(i,A,B);
        }
        printf("Case #%d: %d\n",itr,ans);
    }

    return 0;
}
