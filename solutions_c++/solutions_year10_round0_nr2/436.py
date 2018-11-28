#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;

int n,xx[10];

int GCD(int x,int y)
{
    if(!x || !y)
    return x > y? x : y;
    for(int t;t = x % y ; x = y, y = t);
    return y;
}

int f(int a,int b)
{
    if(a%b==0)
    return a/b;
    else
    return a/b+1;
}

int main()
{
	//freopen("C.in","r",stdin);
	//freopen("C.out","w",stdout);
    int i,j,cases,t,res,x,a;
    scanf("%d",&cases);
    for(i=1;i<=cases;i++)
    {
        scanf("%d",&n);
        if(n==2)
        {
            scanf("%d%d",&xx[0],&xx[1]);
            sort(xx,xx+2);
            t=xx[1]-xx[0];
            a=f(xx[0],t);
            res = a*t - xx[0];
        }
        else
        {
            scanf("%d%d%d",&xx[0],&xx[1],&xx[2]);
            sort(xx,xx+3);
            x=GCD(xx[2]-xx[1],xx[1]-xx[0]);
            a=f(xx[0],x);
            res = a*x - xx[0];
        }
        printf("Case #%d: %d\n",i,res);
    }
	return 0;
}
