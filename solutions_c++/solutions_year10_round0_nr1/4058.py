#include<iostream>
#include<cstdio>
using namespace std;

int n,k,t,p;

int main()
{
    scanf("%d",&t);
    for(;t;t--)
    {
        p++;
        scanf("%d%d",&n,&k);
        n=(1<<n);
        printf("Case #%d: ",p);
        if((k%n)==(n-1))printf("ON\n");
        else printf("OFF\n");
    }
}
