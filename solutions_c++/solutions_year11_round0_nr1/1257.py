#include <cstdio>
#include <iostream>
using namespace std;
//#define max(a,b) ((a)>(b))?(a):(b)

int wh[200],pos[200];
int f[200][200];
int n;

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
        {
            getchar();
            char ch=getchar();
            if (ch=='O') wh[i]=0;
            else wh[i]=1;
            scanf("%d",&pos[i]);
        }
        memset(f,0x7f,sizeof(f));
        for (int i=1;i<=100;i++)
            f[1][i]=max(pos[1],i-1);
        for (int i=1;i<n;i++)
            for (int j=1;j<=100;j++)
            {
                int a[2];
                a[wh[i]]=pos[i];
                a[wh[i]^1]=j;
                for (int k=1;k<=100;k++)
                    f[i+1][k]<?=f[i][j]+max(abs(pos[i+1]-a[wh[i+1]])+1,abs(k-a[wh[i+1]^1]));
            }
        int ans=2147483647;
        for (int i=1;i<=100;i++)
            ans<?=f[n][i];
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
        
