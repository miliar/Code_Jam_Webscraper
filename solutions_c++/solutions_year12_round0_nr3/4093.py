#include<stdio.h>
#include<string.h>
int trans(int x,int flag)
{
    if(x>=100)
    {
        int s1=x%10;
        int s2=x/10;
        s2%=10;
        int s3=x/100;
        if(flag)
            return s2+s3*10+s1*100;
        else
            return s2*100+s1*10+s3;
    }
    else if(x>=10)
    {
        int s1=x%10;
        int s2=x/10;
        return s2+s1*10;
    }
    else
        return x;
}
int calc(int a,int b)
{
    int add=0;
    for(int i=a;i<=b;i++)
    {
        int t1=trans(i,0);
        if(t1<i&&t1>=a)
            add++;
        if(i>=100)
        {
            int t2=trans(i,1);
            if(t2<i&&t2>=a)
                add++;
        }
    }
    return add;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.txt","w",stdout);
    int T,a,b,cnt=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&a,&b);
        printf("Case #%d: %d\n",cnt++,calc(a,b));
    }
}
