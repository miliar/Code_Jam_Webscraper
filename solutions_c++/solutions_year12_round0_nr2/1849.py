#include<stdio.h>
int main()
{
    int a,b,t,n,s,p,out,score;
    int c1,c2,ch;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(a=1;a<=t;a++)
    {
        scanf("%d%d%d",&n,&s,&p);
        c1 = 3*p-2;
        c2 = c1-2;
        if(p==0)
        {
            c1=0;
            c2=0;
        }
        else if(p==1)
        {
            c1=1;
            c2=1;
        }
        for(b=0,out=0,ch=0;b<n;b++)
        {
            scanf("%d",&score);
            if(score>=c1)
                out++;
            else if(score>=c2)
                ch++;
        }
        if(ch>s)
            ch=s;
        printf("Case #%d: %d\n",a,out+ch);
    }
    scanf(" ");
}
