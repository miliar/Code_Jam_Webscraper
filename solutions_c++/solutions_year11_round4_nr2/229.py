#include<iostream>
using namespace std;
#define maxn 510
long a[maxn][maxn];
bool b[maxn][maxn];
long c[maxn],d[maxn];
long si[maxn][maxn],sj[maxn][maxn];
long cas,tst,n,m,dd,i,j,k,l,s,w;
char cc[maxn];
int main()
{
    freopen("B.in","r",stdin);
    freopen("out.txt","w",stdout);
    for (scanf("%ld",&cas),tst=1;tst<=cas;tst++)
    {
        scanf("%ld%ld%ld",&n,&m,&dd);
        for (i=1;i<=n;i++)
        {
            scanf("%s",cc);
            for (j=0;j<m;j++) a[i][j+1]=cc[j]-'0';
        }
        for (i=1;i<=n;i++)
        {
            si[i][0]=0;
            for (j=1;j<=m;j++) si[i][j]=si[i][j-1]+a[i][j];
        }
        for (j=1;j<=m;j++)
        {
            sj[0][j]=0;
            for (i=1;i<=n;i++) sj[i][j]=sj[i-1][j]+a[i][j];
        }
        for (k=min(n,m)-1;k>=2;k--)
        {
            memset(b,0,sizeof(b));
            for (i=1;i+k<=n;i++)
            {
                for (j=1;j<=m;j++) c[j]=sj[i+k][j]-sj[i-1][j],d[j]=sj[i+k-1][j]-sj[i][j];
//                for (j=1;j<=m;j++) cout<<c[j]<<" ";cout<<endl;
//                for (j=1;j<=m;j++) cout<<d[j]<<" ";cout<<endl;
                s=0;
                s+=d[1];
                s+=d[k+1];
                for (j=2;j<=k;j++) s+=c[j];
                w=0;
                w+=d[1]*1;
                w+=d[k+1]*(k+1);
                for (j=2;j<=k;j++) w+=c[j]*j;
//                cout<<s<<" "<<w<<endl;
                if (s*(k+2)==w*2) b[i][1]=1;
//                cout<<s<<" "<<w<<endl;
                for (j=k+2;j<=m;j++)
                {
                    s=s-d[j-k-1]-c[j-k]+d[j-k];
                    s=s-d[j-1]+c[j-1]+d[j];
                    w=w-d[j-k-1]*(j-k-1)-c[j-k]*(j-k)+d[j-k]*(j-k);
                    w=w-d[j-1]*(j-1)+c[j-1]*(j-1)+d[j]*j;
                    if (s*(j+j-k)==w*2) b[i][j-k]=1;
                }
            }
//            for (j=1;j<=m;j++) cout<<b[i][j]<<" ";
//            cout<<endl;
            for (j=1;j+k<=m;j++)
            {
                for (i=1;i<=n;i++) c[i]=si[i][j+k]-si[i][j-1],d[i]=si[i][j+k-1]-si[i][j];
                s=0;
                s+=d[1];
                s+=d[k+1];
                for (i=2;i<=k;i++) s+=c[i];
                w=0;
                w+=d[1]*1;
                w+=d[k+1]*(k+1);
                for (i=2;i<=k;i++) w+=c[i]*i;
                if (s*(k+2)==w*2 && b[1][j]) goto yes;
                for (i=k+2;i<=m;i++)
                {
                    s=s-d[i-k-1]-c[i-k]+d[i-k];
                    s=s-d[i-1]+c[i-1]+d[i];
                    w=w-d[i-k-1]*(i-k-1)-c[i-k]*(i-k)+d[i-k]*(i-k);
                    w=w-d[i-1]*(i-1)+c[i-1]*(i-1)+d[i]*i;
                    if (s*(i+i-k)==w*2 && b[i-k][j]) goto yes;
                }
            }
        }
        printf("Case #%ld: IMPOSSIBLE\n",tst);
        continue;
        yes:
        printf("Case #%ld: %ld\n",tst,k+1);
    }
    return 0;
}
