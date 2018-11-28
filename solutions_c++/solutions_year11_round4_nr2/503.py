#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const int MaxN = 505;
const double eps = 1e-7;
int N,M,X;
int g[MaxN][MaxN], A[MaxN][MaxN], B[MaxN][MaxN], C[MaxN][MaxN];
double Dx[MaxN][MaxN], Dy[MaxN][MaxN];
char s[MaxN];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&N,&M,&X);
        for(int i = 0; i < N; i++)
        {
            scanf("%s",s);
            for(int j = 0; j < M; j++)g[i][j]=s[j]-'0';
        }
        int L;
        for(L = min(N,M); L>=3; L--)
        {
            bool find = 0;
            for(int i = 0; i < N; i++)
            {
                A[i][0] = 0;
                for(int j = 0; j < L; j++)A[i][0]+=g[i][j];
                for(int j = 1; j+L-1 < M; j++)
                    A[i][j] = A[i][j-1]-g[i][j-1]+g[i][j+L-1];
            }
            for(int i = 0; i < M; i++)
            {
                B[0][i] = 0;
                for(int j = 0; j < L; j++)B[0][i]+=g[j][i];
                for(int j = 1; j+L-1 < N; j++)
                    B[j][i] = B[j-1][i]-g[j-1][i]+g[j+L-1][i];
            }
            for(int i = 0; i+L-1 < N; i++)
            {
                C[i][0] = 0;
                for(int j = 0; j < L; j++)C[i][0]+=B[i][j];
                for(int j = 1; j+L-1 < M; j++)
                    C[i][j] = C[i][j-1]-B[i][j-1]+B[i][j+L-1];
            }
            double x = (L-1)/2.0;
            for(int i = 0; i+L-1 < N; i++)
            {
                Dx[i][0] = 0;
                for(int j = 0; j < L; j++)Dx[i][0]+=B[i][j]*(j-x);
                for(int j = 1; j+L-1 < M; j++)
                    Dx[i][j] = (Dx[i][j-1]-B[i][j-1]*(-x))
                              -(C[i][j-1]-B[i][j-1])+B[i][j+L-1]*x;
            }
            for(int i = 0; i+L-1 < M; i++)
            {
                Dy[0][i] = 0;
                for(int j = 0; j < L; j++)Dy[0][i]+=A[j][i]*(j-x);
                for(int j = 1; j+L-1 < N; j++)
                    Dy[j][i] = (Dy[j-1][i]-A[j-1][i]*(-x))
                              -(C[j-1][i]-A[j-1][i])+A[j+L-1][i]*x;
            }
            for(int i = 0; i+L-1 < N; i++)
                for(int j = 0; j+L-1 < M; j++)
                {
                    Dx[i][j]-=g[i][j]*(-x)+g[i][j+L-1]*x
                            + g[i+L-1][j]*(-x)+g[i+L-1][j+L-1]*x;
                    Dy[i][j]-=g[i][j]*(-x)+g[i][j+L-1]*(-x)
                            + g[i+L-1][j]*x+g[i+L-1][j+L-1]*x;
                    if(fabs(Dx[i][j])<eps && fabs(Dy[i][j])<eps)find = 1;
                }
/*
            for(int i = 0; i+L-1 < N; i++)
                for(int j = 0; j+L-1 < M; j++)
                {
                    double tx = 0, ty = 0;
                    for(int k = 0; k < L; k++)
                        for(int p = 0; p < L; p++)
                        {
                            if((k==0&&p==0)||(k==0&&p==L-1)
                               ||(k==L-1&&p==0)||(k==L-1&&p==L-1))
                               continue;
                            tx += g[i+k][j+p]*(k-(L-1)/2.0);
                            ty += g[i+k][j+p]*(p-(L-1)/2.0);
                        }
                    if(fabs(tx)<eps && fabs(ty)<eps)find = 1;
                }*/
            if(find)break;
        }
        printf("Case #%d: ",++cas);
        if(L>=3)printf("%d\n",L);
        else puts("IMPOSSIBLE");
    }

    return 0;
}
