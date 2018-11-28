#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXN 40
using namespace std;

int data[MAXN+1];
int n,k;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,p,t,x;
    scanf("%d",&t);
    for(p=0;p<t;p++)
    {
        memset(data,0,sizeof(data));
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                scanf("%1d",&x);
                if(x==1)
                {
                    data[i]=j;
                }
            }
        }
        k=0;
        for(i=1;i<=n;i++)
        {
            if(data[i]>i)
            {
                for(j=i+1;j<=n;j++)
                {
                    if(data[j]<=i)
                    {
                        rotate(data+i,data+j,data+j+1);
                        k=k+j-i;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",p+1,k);
    }
    return 0;
}
