#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    freopen ("1.in","r",stdin);
    freopen ("1.out","w",stdout);
    int t,n,k;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int fail=0;
        scanf("%d%d",&n,&k);
        for(int j=0;j<n;j++)
            if(!((1<<j)&k))
                fail=1;
        if(fail)
            printf("Case #%d: OFF\n",i+1);
        else
            printf("Case #%d: ON\n",i+1);
    }
    return (0);
}

