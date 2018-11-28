#include <iostream>

using namespace std;

int t,n,c,i,j,k,l;
double C[45][45];
double ex[45][45][45];
double tmp;

void prec()
{
    C[0][0]=1.0;
    for(i=1;i<=40;i++)
    {
        C[i][0]=1.0;
        for(j=1;j<=40;j++)
        {
            C[i][j]=C[i-1][j]+C[i-1][j-1];
        }
    }
}

void precompute()
{
    for(i=1;i<=40;i++)
    {
        for(j=1;j<=i;j++)
        {
            ex[i][j][0]=0.0;
            for(k=1;k<=i;k++)
            {
                tmp=0.00;
                for(l=1;l<=k&&l<=j;l++)
                {
                    tmp+=((ex[i][j][k-l]*C[i-k][j-l]/C[i][j])*C[k][l]);
                }
                tmp+=1.00;
                ex[i][j][k]=tmp/(1-(C[i-k][j]/C[i][j]));
            }
        }
    }
}

int main()
{
    scanf("%d",&t);
    prec();
    precompute();
    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&c);
        printf("Case #%d: %lf\n",i,ex[n][c][n]);
    }
    scanf(" ");
    return 0;
}
