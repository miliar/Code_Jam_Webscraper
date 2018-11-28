#include<iostream>
using namespace std;
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
        int n;
        scanf("%d",&n);
        int sum=0,xr=0,p,mn=10000000;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&p);
            xr^=p;
            sum+=p;
            if(p<mn)
            mn=p;
        }
        printf("Case #%d: ",ca);
        if(xr) puts("NO");
        else
        {
            printf("%d\n",sum-mn);
        }
    }
}
