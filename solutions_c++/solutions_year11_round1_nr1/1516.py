#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tt, n, pd, pg;
    scanf("%d", &tt);
    for(int t=1; t<=tt; t++)
    {
        bool ff=0;
        scanf("%d%d%d", &n, &pd, &pg);
        printf("Case #%d: ", t);
        if(pd!=0 && pg==0) {printf("Broken\n");continue;}
        else if(pd==0 && pg==0) {printf("Possible\n"); continue;}
        else if(pd==100){printf("Possible\n"); continue;}
        else if(pd!=100 && pg==100) {printf("Broken\n");continue;}
        else
        for(int i=1; i<=n; i++)
        {
            int flag=0;
            flag=(pd*i)%100;
            if(flag==0) {printf("Possible\n");ff=1; break;}
         }
         if(ff==0)
            printf("Broken\n");
    }
    return 0;
}
