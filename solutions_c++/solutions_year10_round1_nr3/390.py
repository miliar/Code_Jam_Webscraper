#include<stdio.h>
#include<string.h>
int t,a1,a2,b1,b2;
int check(int a,int b)
{
    if(a==b) return 0;
    if(a<b)
    {
           int c=b;
           b=a;
           a=c;
    }
    if(a>=2*b) return 1;
    else return (1-check(b,a-b));
} 

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&t); 
    for(int ca=1;ca<=t;ca++)
    {
            scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
            int ans=0;
            for(int i=a1;i<=a2;i++)
             for(int j=b1;j<=b2;j++)
             ans+=check(i,j);
             printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
              
