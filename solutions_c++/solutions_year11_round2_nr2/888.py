#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
using namespace std;

long long nod(long long a,long long b)
{
    while(a&&b)
        if(a>b) a=a%b; else b=b%a;
    return a+b;
}
int x[1000005];
int n,d;

bool solve(double m)
{
    double cc=x[0]-m;
    for(int i=1;i<n;i++)
    {
        double t=cc+d;
        if(x[i]+m<t)
            return false;
        if(x[i]>t)
          cc=max(t,x[i]-m);
        else
         cc=min(x[i]+m,t);
    }
    return true;
}

int main()
{
	int T;
	cin>>T;
	int a[205],b[205];
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int c,p,v,k=0;
        cin>>c>>d;
        n=0;
        for(int i=0;i<c;i++)
        {
            cin>>a[i]>>b[i];
            n+=b[i];
        }
        int rr=0;
        for(int i=0;i<c;i++)
        {
            for(int j=0;j<b[i];j++)
            {
                x[rr++]=a[i];
            }
        }

    double l=0,r=1000*1000+2;
    for(int i=0;i<55;i++)
    {
        double m=(l+r)/2;
        if(solve(m)) r=m;else l=m;
    }
    printf("%.2lf\n",r);

    }

	return 0;
}
