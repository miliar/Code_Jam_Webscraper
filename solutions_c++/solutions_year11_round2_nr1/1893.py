#include<iostream>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,i,j,k;
    double N,WIN[101],LOSS[101],c;
    double WP[101],OP[101],OWP[101],RPI[101],TWP,TOP;
    char str[105][105];
    scanf("%d",&T);
    for (i=1;i<=T;i++)
    {
        scanf("%lf\n",&N);
        for (j=0;j<N;j++)
        {
            WIN[j]=0;
            LOSS[j]=0;
        }
        for (j=0;j<N;j++)
        {
            gets(str[j]);
            for (k=0;k<N;k++)
            {
                if (str[j][k]=='0')
                   LOSS[j]++;
                else if (str[j][k]=='1')
                     WIN[j]++;
            }
        }
        TWP=0.0;
        for (j=0;j<N;j++)
        {
            if (WIN[j]+LOSS[j]>0.0)
               WP[j]=WIN[j]/(WIN[j]+LOSS[j]);
            else
                WP[j]=0.0;
        }
        TOP=0.0;
        for (j=0;j<N;j++)
        {
            OP[j]=0.0;
            c=0.0;
            for (k=0;k<N;k++)
            {
                if (str[j][k]!='.')
                {
                    if (str[k][j]=='0' && (WIN[k]+LOSS[k]-1.0)>0.0)
                       OP[j]+=(WIN[k])/(WIN[k]+LOSS[k]-1.0);
                    else if (str[k][j]=='1' && WIN[k]-1.0>0.0 && (WIN[k]+LOSS[k]-1.0)>0.0)
                         OP[j]+=(WIN[k]-1.0)/(WIN[k]+LOSS[k]-1.0);
                    else if (str[k][j]=='.' && (WIN[k]+LOSS[k])>0.0)
                         OP[j]+=(WIN[k])/(WIN[k]+LOSS[k]);
                         c++;
                }
            }
            OP[j]=(OP[j])/(c);
        }
        for (j=0;j<N;j++)
        {
            OWP[j]=0.0;
            c=0.0;
            for (k=0;k<N;k++)
            {
                if (str[j][k]!='.')
                {
                   OWP[j]+=OP[k];
                   c++;
                }
            }
            OWP[j]=(OWP[j])/(c);
        }
        for (j=0;j<N;j++)
            RPI[j]=0.25 * WP[j] + 0.50 * OP[j] + 0.25 * OWP[j];
        printf("Case #%d:\n",i);
        for (j=0;j<N;j++)
        {
            printf("%.6lf\n",RPI[j]);
        }
    }
}
