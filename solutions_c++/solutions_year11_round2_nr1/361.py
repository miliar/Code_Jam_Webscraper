#include<iostream>
using namespace std;
const int maxn=110;
char a[maxn][maxn];
int b[maxn],c[maxn];
double d[maxn],e[maxn];
int n;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases,tt,i,j,k;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        getchar();
        for (j=0;j<n;j++)
        a[i][j]=getchar();
    }
    for (i=0;i<n;i++)
    {
        b[i]=0;
        c[i]=0;
        for (j=0;j<n;j++)
        {
            if (a[i][j]!='.') b[i]++;
            if (a[i][j]=='1') c[i]++;
        }
    }
    printf("Case #%d:\n",tt+1);
    for (i=0;i<n;i++)
    {
        d[i]=0;
        for (j=0;j<n;j++)
        if (a[i][j]!='.')
           if (a[i][j]=='1') 
              d[i]+=1.0*c[j]/(b[j]-1);
           else
              d[i]+=1.0*(c[j]-1)/(b[j]-1);
        d[i]/=b[i];
    }
    for (i=0;i<n;i++)
    {
        e[i]=0;
        for (j=0;j<n;j++)
        if (a[i][j]!='.')
        {
           e[i]+=d[j];
        }
        printf("%.10lf\n",e[i]/b[i]*0.25+d[i]*0.5+0.25*c[i]/b[i]);
    }
    }
    return 0;
}
