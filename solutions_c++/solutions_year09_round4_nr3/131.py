#include<iostream>
using namespace std;
int cn,ci,n,K,i,j,flag1,flag2,k;
int h[200][200];
int ans;
int v[200];
int lnk[200];
int a[200][200];

int find(int k)
{
    int i;
    for (i=0;i<n;i++)
    if (h[k][i] && !v[i])
    {
        v[i]=1;
        if (lnk[i]==-1 || find(lnk[i]))
        {
            lnk[i]=k;
            return 1;
        }        
    }
    return 0;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&cn);
    for (ci=1;ci<=cn;ci++)
    {
        scanf("%d %d",&n,&K);
        for (i=0;i<n;i++)
        {
            for (j=0;j<K;j++) scanf("%d",&a[i][j]);
        }
        memset(h,0,sizeof(h));
        for (i=0;i<n;i++)
        for (j=i+1;j<n;j++)
        {
            flag1=0;
            flag2=0;
            for (k=0;k<K;k++)
            {
                if (a[i][k]>=a[j][k]) flag1=1;
                if (a[i][k]<=a[j][k]) flag2=1;                
            }
            if (flag1 && flag2) continue;
            if (flag1) h[i][j]=1;
            else h[j][i]=1;
        }
        ans=n;
        for (i=0;i<n;i++) lnk[i]=-1;
        for (i=0;i<n;i++)
        {
            memset(v,0,sizeof(v));
            if (find(i)) ans--;
        }
        printf("Case #%d: %d\n",ci,ans);
    }
    return 0;
}
