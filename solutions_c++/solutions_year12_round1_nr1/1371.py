/*
TASK: Password Problem
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
using namespace std;
#define X first
#define Y second
int N,M,T;
double a[100005];
double b[100005];
double c[100005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int A,B,ii=0;
    while(T--)
    {
        scanf("%d%d",&A,&B);
        for(i=1;i<=A;i++)
            scanf("%lf",&a[i]);
        double ans=2.0+B;
        ans=min(ans,A+B+1.0);
        double p=1.0,q,x;
        for(i=1;i<=A;i++)
        {
            p=p*a[i];       // all true
            x=p*((A-i)+B-A+(A-i)+1);
            q=1-p;
            x=x+q*((A-i)+B-A+(A-i)+1+B+1);
            ans=min(ans,x);
        }
        ii++;
        printf("Case #%d: %lf\n",ii,ans);
    }
}
