#include<iostream>
#include<stdio.h>
using namespace std;

int t[102],n,s,p;

int main()
{
    int T,cas=0,i,x,y;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        cas++;
        scanf("%d%d%d",&n,&s,&p);
        x=0,y=0;
        for(i=0; i<n; ++i)
        {
            scanf("%d",&t[i]);
            if(t[i]>=3*p-2)
                x++;
            else
                if(t[i]>=max(3*p-4,2))
                    y++;
        }
        printf("Case #%d: %d\n",cas,x+min(s,y));
    }
    return 0;
}
