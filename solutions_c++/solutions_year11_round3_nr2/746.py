#include<cstdio>
#include<cstring>
#define abs(x) ((x)<0?-(x):(x))
#define min(x,y) (x<y?x:y)
#define clr(a,b) memset(a,b,sizeof(a))
#define maxn 2000

using namespace std;

long long T,l,n,c;
double m;
double d[maxn];
double f[maxn][maxn];

void init()
{
    long long p;
    scanf("%d%lld%d%d",&l,&p,&n,&c);
    m=(double)p;
    for (int i=0;i<c;i++)
        scanf("%lf",&d[i]);
    for (int i=0;i<n;i++)
        d[i]=d[i%c];
//    for (int i=0;i<c;i++)
//        printf("!%0.0f ",d[i]);
}

double work()
{
    for (int i=0;i<=n;i++)
        for (int j=0;j<=l;j++)
            f[i][j]=-1;
    f[0][0]=0;
    for (int i=0;i<n;i++)
        for (int j=0;j<=l;j++)
            if (f[i][j]>=0){
                if (f[i+1][j]>=0)
                    f[i+1][j]=min(f[i+1][j],f[i][j]+d[i]*2);
                else
                    f[i+1][j]=f[i][j]+d[i]*2;
                if (m>f[i][j]){
                    if (d[i]+(m-f[i][j])*0.5<d[i]*2)
                        if (f[i+1][j+1]>=0)
                            f[i+1][j+1]=min(f[i+1][j+1],f[i][j]+d[i]+(m-f[i][j])*0.5);
                        else
                            f[i+1][j+1]=f[i][j]+d[i]+(m-f[i][j])*0.5;
                }else{
                    if (f[i+1][j+1]>=0)
                        f[i+1][j+1]=min(f[i+1][j+1],f[i][j]+d[i]);
                    else
                        f[i+1][j+1]=f[i][j]+d[i];
                }
            }
/*
    for (int i=0;i<=n;i++){
        for (int j=0;j<=l;j++)
            printf("%0.1f ",f[i][j]);
        printf("\n");
    }
*/    double r=1000000000;
    r*=r;
    for (int j=0;j<=l;j++)
        if (f[n][j]!=-1)
            r=min(f[n][j],r);
    return r;
}

int main()
{
    FILE *tin=freopen("B-small-attempt1.in", "r", stdin);
    FILE *cin=freopen("b.txt", "w", stdout);
    scanf("%d",&T);
    for (int tnum=1;tnum<=T;tnum++){
        init();
        printf("Case #%d: %lld\n",tnum,(long long)work());

    }
}
