#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,n,k,m;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d",&n,&k);
        m=(1<<n)-1;
        printf("Case #%d: ",c+1);
        if((k&m)==m)
        {
            printf("ON\n");
        }
        else
        {
            printf("OFF\n");
        }
    }
    return 0;
}
