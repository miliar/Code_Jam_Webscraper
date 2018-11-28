#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;

int f(int u,int v)
{
    if(u%v==0)
    return u/v;
    else
    return u/v+1;
}

int GCD(int x,int y)
{
    if(!x || !y)
    return x > y? x : y;
    for(int t;t = x % y ; x = y, y = t);
    return y;
}

int main()
{
	int n,v[10];
    int i,c,t,r,x,a;
    scanf("%d",&c);
    for(i=1;i<=c;i++)
    {
        scanf("%d",&n);
        if(n==2)
        {
            scanf("%d%d",&v[0],&v[1]);
            sort(v,v+2);
            t=v[1]-v[0];
            a=f(v[0],t);
            r = a*t - v[0];
        }
        else
        {
            scanf("%d%d%d",&v[0],&v[1],&v[2]);
            sort(v,v+3);
            x=GCD(v[2]-v[1],v[1]-v[0]);
            a=f(v[0],x);
            r = a*x - v[0];
        }
        printf("Case #%d: %d\n",i,r);
    }
	return 0;
}
