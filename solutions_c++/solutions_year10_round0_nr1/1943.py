#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
int main()
{
   int T;
   scanf("%d",&T);
   for(int r=0;r<T;r++)
    {
        long long a,b;
        scanf("%ld%ld",&a,&b);
        long long mod=(long long)((long long)1<<a);
        if(b%mod==mod-1)
         printf("Case #%d: ON\n",r+1);
        else
         printf("Case #%d: OFF\n",r+1);
    }
}
