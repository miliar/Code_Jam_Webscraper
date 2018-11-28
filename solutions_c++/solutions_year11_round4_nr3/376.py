#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXP 1000000
#define SQRT 1000
using namespace std;

char mark[MAXP+1];
long long n;

void initialize()
{
    int i,j;
    for(i=2;i<=SQRT;i++)
    {
        if(mark[i]==0)
        {
            for(j=i*i;j<=MAXP;j=j+i)
            {
                mark[j]=1;
            }
        }
    }
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int p,q;
    long long i,j,x,s;
    initialize();
    scanf("%d",&q);
    for(p=0;p<q;p++)
    {
        scanf("%I64d",&n);
        printf("Case #%d: ",p+1);
        if(n==1)
        {
            printf("0\n");
            continue;
        }
        s=1;
        for(i=2;i*i<=n;i++)
        {
            if(mark[i]==0)
            {
                x=i*i;
                for(j=0;x<=n;j++)
                {
                    x=x*i;
                }
                s=s+j;
            }
        }
        printf("%I64d\n",s);
    }
    return 0;
}
