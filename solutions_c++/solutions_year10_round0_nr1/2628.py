#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
   freopen("d:\\A-large.in","r",stdin);
    freopen("d:\\b.out","w",stdout);
    int T;
    int n,k;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        int ans = 0;
        scanf("%d%d",&n,&k);
        ans+=k;
        bool mark = true;
        for(int j=0;j<n;j++)
        {
            if((ans|(1<<j))!=ans)
            {
                mark =false;
                break;
            }
        }
        if(mark)
        {
           printf("Case #%d: ON\n",i);
        }
        else
        {
            printf("Case #%d: OFF\n",i);
        }
    }
    return 0;
}
