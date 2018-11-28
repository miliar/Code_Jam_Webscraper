#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <time.h>
#include <stack>

using namespace std;

long long n;
long long R[1009],l,w;
long long X[1009],Y[1009];

bool check(int d)
{
    for(int i=0;i<d;i++)
        if((X[i]-X[d])*(X[i]-X[d])+(Y[i]-Y[d])*(Y[i]-Y[d])<(R[i]+R[d])*(R[i]+R[d])) return 0;
    return 1;
}

bool solve(long long d)
{
    if(d==n) return 1;
    for(int k=0;k<10;k++)
    {
        X[d]=rand()%(w+1);
        Y[d]=rand()%(l+1);
        if(!check(d)) continue;
        if(solve(d+1)) return 1;
    }
    return 0;
}

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int ca,T=0;
    scanf("%d",&ca);
    srand(time(NULL));
    while(ca--)
    {
        scanf("%lld%lld%lld",&n,&w,&l);
        for(int i=0;i<n;i++) scanf("%lld",&R[i]);
        while(!solve(0));
        printf("Case #%d:",++T);
        for(int i=0;i<n;i++)
            printf(" %lld.0 %lld.0",X[i],Y[i]);
        puts("");
    }
    return 0;
}
