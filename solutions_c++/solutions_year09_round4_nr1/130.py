#include<iostream>
using namespace std;
int cn,ci;
int n,i,j,ans,k;
int a[100];
char s[1000];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cn);
    for (ci=1;ci<=cn;ci++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%s",&s);
            a[i]=0;
            for (j=0;j<n;j++)
            if (s[j]=='1') a[i]=j;
        }
        ans=0;
        for (i=0;i<n;i++)
        {
            for (j=i;j<n;j++)
            if (a[j]<=i) break;
            ans+=j-i;
            for (k=j;k>i;k--) a[k]=a[k-1];
        }
        printf("Case #%d: %d\n",ci,ans);
    }
    return 0;
}
