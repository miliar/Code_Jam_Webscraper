#include <cstdio>
#include <iostream>
#include <algorithm>
#define MAXD 100
using namespace std;

const int md[MAXD+1]={0,100,50,100,25,20,50,100,25,100,10,100,25,100,50,20,25,
100,50,100,5,100,50,100,25,4,50,100,25,100,10,100,25,100,50,20,25,100,50,100,5,
100,50,100,25,20,50,100,25,100,2,100,25,100,50,20,25,100,50,100,5,100,50,100,25,
20,50,100,25,100,10,100,25,100,50,4,25,100,50,100,5,100,50,100,25,20,50,100,25,
100,10,100,25,100,50,20,25,100,50,100,1};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,pd,pg;
    long long n;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%I64d %d %d",&n,&pd,&pg);
        printf("Case #%d: ",c+1);
        if(pg==100)
        {
            if(pd==100)
            {
                printf("Possible\n");
            }
            else
            {
                printf("Broken\n");
            }
        }
        else if(pg==0)
        {
            if(pd==0)
            {
                printf("Possible\n");
            }
            else
            {
                printf("Broken\n");
            }
        }
        else
        {
            if(md[pd]<=n)
            {
                printf("Possible\n");
            }
            else
            {
                printf("Broken\n");
            }
        }
    }
    return 0;
}
