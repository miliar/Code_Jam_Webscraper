#include<iostream>
using namespace std;
__int64 sum[1010][1010];
int num[1010];
int bs(int l,int r,int k,int v)
{
    if(l==r)
    return l;
    if(l==r-1)
    {
        if(sum[k][r]<=v)
        return r;
        return l;
    }
    int m=(l+r)>>1;
    if(sum[k][m]>v)
    return bs(l,m-1,k,v);
    return bs(m,r,k,v);
}
int main()
{
    int r,k,n,cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
         scanf("%d%d%d",&r,&k,&n);
         for(int i=0;i<n;i++)
         scanf("%d",&num[i]);
         for(int i=0;i<n;i++)
         {
             sum[i][1]=num[i];
             for(int j=2;j<=n;j++)
                 sum[i][j]=sum[i][j-1]+num[(i+j-1)%n];
         }
         __int64 res=0;
         int s=0;
         while(r--)
         {
             int p=bs(1,n,s,k);
             res+=sum[s][p];
             s=(s+p)%n;
         }
         printf("Case #%d: %I64d\n",ca,res);
    }
}
