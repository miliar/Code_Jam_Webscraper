#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t,num=0,flag,n,i,j,l,h,data[102];
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        num++;
        scanf("%d%d%d",&n,&l,&h);
        for(i=0;i<n;i++)
            scanf("%d",&data[i]);
        for(i=l,flag=0;i<=h;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i%data[j]==0 || data[j]%i==0)
                    continue;
                else break;
            }
            if(j>=n)
            {
                flag=1;
                break;
            }
        }
        printf("Case #%d: ",num);
        if(flag)
            printf("%d\n",i);
        else
            printf("NO\n");
    }
    return 0;
}