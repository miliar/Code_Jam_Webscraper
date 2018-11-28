#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,n,T,count,j,k;
    int a[10002][10];
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
       count=0;
       scanf("%d",&n);
       for(j=0;j<n;j++)
       scanf("%d%d",&a[j][0],&a[j][1]);
       for(j=0;j<n;j++)
           for(k=j+1;k<n;k++)
           {
               if((a[j][0]>a[k][0]&&a[j][1]<a[k][1])||(a[j][0]<a[k][0]&&a[j][1]>a[k][1]))
               count+=1;
            }
       printf("Case #%d: %d\n",i,count);
    }
    return 0;
}
