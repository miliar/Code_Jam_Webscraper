#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,n,p,t,c,minc,sumc,state;
    scanf("%d",&t);
    for(p=0;p<t;p++)
    {
        scanf("%d",&n);
        minc=100000000;
        sumc=0;
        state=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&c);
            minc=min(minc,c);
            sumc=sumc+c;
            state=state^c;
        }
        printf("Case #%d: ",p+1);
        if(state==0)
        {
            printf("%d\n",sumc-minc);
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}
