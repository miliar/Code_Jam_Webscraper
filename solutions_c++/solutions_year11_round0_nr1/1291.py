#include<iostream>
using namespace std;
int i,j,n,d,t1,t2,x1,x2,t;
char c;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        t1=t2=0;
        x1=x2=1;
        for(j=1;j<=n;j++)
        {
            scanf(" %c %d",&c,&d);
            if(c=='O')
            {
                t1+=abs(x1-d);
                x1=d;
                t1=t1>t2?t1:t2;
                t1++;
            }
            if(c=='B')
            {
                t2+=abs(x2-d);
                x2=d;
                t2=t2>t1?t2:t1;
                t2++;
            }
        }
        printf("Case #%d: %d\n",i,t1>t2?t1:t2);
    }
}
