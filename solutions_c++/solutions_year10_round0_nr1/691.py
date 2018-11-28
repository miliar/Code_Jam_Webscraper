#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
    int t,n,k;
    scanf("%d",&t);
    for (int i = 0;i < t;i++)
    {
        scanf("%d %d",&n,&k);
        if ((k+1)%(int)pow(2,n) == 0)
            printf("Case #%d: ON\n",i+1);
        else
            printf("Case #%d: OFF\n",i+1);
    }
    return 0;
}
