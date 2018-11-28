#include<iostream>
#include<stdio.h>
using namespace std;
int f[32];
int main()
{
    int t;
    scanf("%d",&t);
    f[0]=1;
    int i;
    for(i=1;i<=30;i++)
        f[i]=f[i-1]*2;
    for(int cas=1;cas<=t;cas++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",cas);
        if((k&(f[n]-1))==f[n]-1)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
