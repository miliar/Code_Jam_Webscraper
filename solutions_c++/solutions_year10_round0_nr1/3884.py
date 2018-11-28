#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,n,k,a[100],s;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        memset(a,0,sizeof(a));
        scanf("%d%d",&n,&k);
        s=0;
        while(k>0)
        {
            a[++s]=k%2;
            k/=2;
        }
        s=0;
        for(j=1;j<=n;j++)
            if(a[j]==0) 
            {
                s=1;
                break;
            }
        if(!s) printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    }
    return 0;
}
