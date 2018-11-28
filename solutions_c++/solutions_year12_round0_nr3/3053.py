#include<cstdio>
using namespace std;
int main()
{
    int a,t,i,j,b,p,o=0;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        o=0;
        scanf("%d%d",&a,&b);
        p=1;
        int a2=a;
        while(a2)
        {
            p*=10;
            a2/=10;
        }
        for(j=a;j<=b;j++)
        {
            a2=j;
            int b2=0,p2=1;
            while(a2)
            {
                b2+=p2*(a2%10);
                p2*=10;
                a2/=10;
                if(a<=b2*(p/p2)+a2 && b2*(p/p2)+a2<=b && a2!=0 && b2*(p/p2)+a2>j)
                {
                    o++;
                }
            }
        }
        printf("Case #%d: %d\n",i,o);
    }
}
