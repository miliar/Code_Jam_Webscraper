/*
 * Author: ahxgw
 * Created Time:  2010-5-8 21:50:47
 * File Name: C.cpp
 * Description: 
 */
#include<iostream>
#include<cstdio>
using namespace std;

#define MaxN 11

int r,k,n;
int a[MaxN];

int main()
{
    int t,i,j;
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d %d",&r,&k,&n);
        int sum=0;
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[j]);
            sum+=a[j];
        }
        int pos=0,ans=0;
        for(j=0;j<r;j++)
        {
            int num=0;
            while(num+a[pos]<=k&&num<sum)
            {
                num+=a[pos];
                pos=(pos+1)%n;
            }
            ans+=num;
        }
        printf("Case #%d: %d\n",i,ans);
    }

    return 0;
}
