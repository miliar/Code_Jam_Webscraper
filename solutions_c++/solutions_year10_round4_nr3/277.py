#include <iostream>
using namespace std;
const int maxn=600;
int t,cc,a[maxn][maxn],ans,i,j,k,n,x0,y0,x1,y1,s;
char x;
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
int swap(int &i,int &j)
{
    int tmp;
    tmp=i;
    i=j;
    j=tmp;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for (cc=1;cc<=t;cc++)
    {
        cin>>n;
        for (i=0;i<maxn;i++)
        memset(a[i],0,sizeof(a[i]));
        for (i=1;i<=n;i++)
        {
            cin>>x0>>y0>>x1>>y1;
            if (x0>x1) swap(x0,x1);
            if (y0>y1) swap(y0,y1);
            for (j=x0;j<=x1;j++)
                for (k=y0;k<=y1;k++) a[j][k]=1;
        }
            s=1;
            for (ans=0;s;ans++)
            {
                s=0;
                for (i=maxn-1;i;i--)
                    for (j=1;j<i;j++)
                    {
                        k=i-j;
                        if ((a[j-1][k])&&(a[j][k-1])) a[j][k]=1;
                        if ((!a[j-1][k])&&(!a[j][k-1])) a[j][k]=0;
                        if (a[j][k]) s=1;
                    }
            }
        printf("Case #%d: %d\n",cc,ans);
    }
}
