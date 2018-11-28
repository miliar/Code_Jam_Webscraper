#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;
const int N = 106,M=260,INF = 1<<28;
int D,I,m,n;
int a[N];
int f[N][M];
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T,K=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d%d",&D,&I,&m,&n);
        //if(K==65)printf("%d %d %d %d\n",D,I,m,n);
        for(int i=1;i<=n;++i)
        {
            a[i]=INF;
        }
        for(int i=1;i<=n;++i)
        {
            scanf("%d",a+i);
            //if(K==65)printf("%d ",a[i]);
        } //if(K==65)puts("");
        for(int i=0;i<M;++i)
            f[0][i]=0;
        for(int i=1;i<=n;++i)
        {
            for(int j=0;j<M;++j)
            {
                f[i][j]=INF;
            }
        }
        for(int i=1;i<=n;++i)
        {
            for(int j=0;j<M;++j)
            {
                //if(f[i-1][j]>=INF)continue;
                for(int k=0;k<M;++k)
                {
                    if(abs(j-k)<=m)
                    {
                        //if(k==a[i])f[i][k]=min(f[i][k],f[i-1][j]);
                        if(k==j)f[i][k]=min(f[i][k],f[i-1][j]+D);
                        f[i][k]=min(f[i][k],f[i-1][j]+abs(a[i]-k));

                       // if(f[i][k]<=20)printf("%d,%d,%d=%d\n",i,j,k,f[i][k]);
                    }
                    if(m&&abs(a[i]-j)<=m)
                        {
                           // printf("M: %d,%d,%d,%d\n",m,a[i],i,j,k);
                            int count = abs(a[i]-k)/m;
                            if(abs(a[i]-k)%m)++count;
                            //if(k==46)printf("xx :%d,%d,%d=%d %d %d\n",i,j,k,f[i][k],f[i-1][j],count);

                            f[i][k]=min(f[i][k],f[i-1][j]+count*I);
                        }
                    if(m&&abs(a[i]-j)>m)
                    {

                            //if(k==46)printf("xx :%d,%d,%d=%d %d %d\n",i,j,k,f[i][k],f[i-1][j],count);
                        for(int xx=max(j-m,0);xx<=min(M-1,j+m);++xx)
                        {
                            int count = abs(xx-k)/m;
                            if(abs(xx-k)%m)++count;
                            f[i][k]=min(f[i][k],f[i-1][j]+count*I+abs(a[i]-xx));
                        }
                    }
//                    if(m)
//                    {
//                        int count = abs(j-k)/m;
//                        if(abs(j-k)%m)++count;
//                        f[i][k]=min(f[i][k],f[i-1][j]+count*I+D);
//                        if(f[i][k]<=20)printf("%d,%d,%d=%d\n",i,j,k,f[i][k]);
//                    }
                }
            }
        }
        int ans = INF;
        for(int i=0;i<M;++i)
        {
           // if(f[n][i]<=20)printf("%d a\n",f[n][i]);
            ans=min(ans,f[n][i]);
        }
        if(ans==INF)printf("Impossible");
        if(ans>n*D)printf("Impossible");

        //if(n==0)puts("0000");
        printf("Case #%d: %d\n",K++,ans);
    }
    return 0;
}
