#include <iostream>
using namespace std;
const int maxn=12;
const int maxm=1<<maxn;
const int maxs=1000000001;
int t,cc,f[maxm][maxn],i,j,k,n,p,cost[maxm],a[maxm],l;
int max(int i,int j)
{
    if (i<j) return j;
        else return i;
}
int min(int i,int j)
{
    if (i>j) return j;
        else return i;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for (cc=1;cc<=t;cc++)
    {
        cin>>p;
        n=1<<p;
        for (i=0;i<n;i++) 
        {
            cin>>a[i];
            a[i]=p-a[i];
        }
        for (j=p;j>=1;j--)
            for (i=1;i<=(1<<(j-1));i++)
                cin>>cost[(1<<(j-1))+i-1];
        for (i=0;i<maxm;i++)
            for (j=0;j<maxn;j++) f[i][j]=maxs;
        for (i=1;i<=(1<<(p-1));i++)
        {
            k=(1<<(p-1))+i-1;
            j=max(a[2*i-2],a[2*i-1]);
            f[k][j]=0;
            if (j) f[k][j-1]=cost[k];
        }
        for (i=(1<<(p-1))-1;i;i--)
            for (j=0;j<=p;j++)
            if (f[2*i][j]<maxs)
            for (k=0;k<=p;k++)
            if (f[2*i+1][k]<maxs)
            {
                                l=max(j,k);
                                f[i][l]=min(f[2*i][j]+f[2*i+1][k],f[i][l]);
                                if (l)
                                f[i][l-1]=min(f[2*i][j]+f[2*i+1][k]+cost[i],f[i][l-1]);
            }
        printf("Case #%d: %d\n",cc,f[1][0]);
    }
}
