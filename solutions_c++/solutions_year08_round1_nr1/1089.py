#include <cstdio>
#include <cstdlib>
#include <cstring>
#define MAXN 810

int T,n;
int k=1;

int a[810],b[810];
int w[810][810];
int result,min;
bool marka[810],markb[810];

void solve(int m,int p)
{
    if(m==n)
    {
        if(p<min)
            min=p;
        return ;
    }
    marka[m+1]=true;
    int i;
    for(i=1;i<=n;i++)
    {
        if(!markb[i])
        {
            markb[i]=true;
            solve(m+1,p+w[m+1][i]);
            markb[i]=false;
        }
    }
}

int main()
{
    int i,j;

    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        memset(w,0,sizeof(w));
        memset(marka,0,sizeof(marka));
        memset(markb,0,sizeof(markb));
        scanf("%d",&n);
        for(i=1;i<=n;i++)
            scanf("%d",&a[i]);
        for(i=1;i<=n;i++)
            scanf("%d",&b[i]);
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
            {
                w[i][j]=a[i]*b[j];
            }
        min=0x7fffffff;
        marka[1]=true;
        for(i=1;i<=n;i++)
        {
            markb[i]=true;
            solve(1,w[1][i]);
            markb[i]=false;
        }
        printf("Case #%d: %d\n",k,min);
        k++;
    }
    return 0;
}
