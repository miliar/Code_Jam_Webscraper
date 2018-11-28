#include <iostream>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
#include <memory.h>
using namespace std;

int main()
{
    int t,n,k,i,j,temp;
    int r;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);

    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&k);
        temp=1<<n;
        r=k%temp;
        if(r==temp-1)
            printf("Case #%d: ON\n",i);
        else
            printf("Case #%d: OFF\n",i);
    }
    return 0;
}
