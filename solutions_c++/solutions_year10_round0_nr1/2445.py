#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,n,k,t,m;
    scanf("%d",&cas);
    for(t=1;t<=cas;t++)
    {
        scanf("%d %d",&n,&k);
        m=(int)pow((double)2,(double)n);
        printf("Case #%d: ",t);
        if((k+1)%m==0) printf("ON");
        else printf("OFF");

        printf("\n");
    }
    return 0;
}
