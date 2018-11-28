#include<iostream>
using namespace std;
const int maxn=20;
int a[maxn][maxn],n,m;
int check(int x)
{
    int i,j,i1,j1,sx,sy;
    for (i=0;i+x<=n;i++)
        for (j=0;j+x<=m;j++)
        {
            sx=0;
            sy=0;
            for (i1=i;i1<i+x;i1++)
                for (j1=j;j1<j+x;j1++)
                {
                    if ((i1==i||i1==i+x-1)&&(j1==j||j1==j+x-1)) continue;
                    sx+=(i1*2-i-(i+x-1))*a[i1][j1];
                    sy+=(j1*2-j-(j+x-1))*a[i1][j1];
                }
            if (sx==0&&sy==0) return 1;
        }
    return 0;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int d,i,j,tt,cases;
    char ch;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%d%d%d",&n,&m,&d);
        for (i=0;i<n;i++)
        {
            getchar();
            for (j=0;j<m;j++)
            {
                ch=getchar();
                a[i][j]=ch-'0';
            }
        }
        printf("Case #%d: ",tt+1);
        for (i=min(n,m);i>2;i--)
        if (check(i)) break;
        if (i==2) puts("IMPOSSIBLE");
        else printf("%d\n",i);
    }
    return 0;
}
