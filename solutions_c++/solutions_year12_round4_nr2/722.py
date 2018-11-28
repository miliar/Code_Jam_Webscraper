#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <time.h>
#include <stack>

using namespace std;

long long n;
long long r[1009],l,w;
long long xst[1009],yst[1009];



long long work(long long l)
{
    long long a=rand()%(l+1);
    return a;
}

bool check(int i,int d)
{
    if((xst[i]-xst[d])*(xst[i]-xst[d])+(yst[i]-yst[d])*(yst[i]-yst[d])>=(r[i]+r[d])*(r[i]+r[d])) return 1;
    return 0;
}

bool dfs(long long d)
{
    if(d==n) return 1;
    for(int k=0;k<10;k++)
    {
        xst[d]=work(w);
        yst[d]=work(l);
        bool f=1;
        for(long long i=0;i<d;i++)
        {
            if(!check(i,d)) f=0;
            if(!f) break;
        }
        if(!f) continue;
        if(dfs(d+1)) return 1;
    }
    return 0;
}

int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    int ca,T=0;
    srand(time(0));
    for(scanf("%d",&ca);ca--;)
    {
        scanf("%lld%lld%lld",&n,&w,&l);
        for(long long i=0;i<n;i++) scanf("%lld",&r[i]);
//        sort(r,r+n);
        while(!dfs(0));
        printf("Case #%d:",++T);
        for(long long i=0;i<n;i++)
        {
            printf(" %lld.0 %lld.0",xst[i],yst[i]);
        }
        puts("");
    }
    return 0;
}
