#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
    freopen("codejam.in","r",stdin);
    freopen("codejam.out","w",stdout);
    double *array=(double*)calloc(100,sizeof(double));
    double *array2=(double*)calloc(100,sizeof(double));
    double *tpt;
    double sum=0.;
    int binomial[50][50]={{1}};
    int cn,cnt,n,c;
    int i,j,k;
    scanf("%d",&cnt);
    for(cn=0;cn<cnt;cn++)
    {
        sum=0.;
        scanf("%d%d",&n,&c);
        for(i=1;i<50;i++)
        {
            binomial[i][0]=1;
            for(j=1;j<=i;j++)
                binomial[i][j]=binomial[i-1][j]+binomial[i-1][j-1];
        }
        array[0]=1.;
        for(i=1;i<=n;i++)
            array[i]=0.;
        for(i=0;i<100000;i++)
        {
            for(j=0;j<=n;j++)
                array2[j]=0.;
            for(j=0;j<n;j++)
            {
                for(k=0;j+k<=n && c-k>=0;k++)
                {
                    array2[k+j]+=binomial[j][c-k]*binomial[n-j][k]*array[j]/binomial[n][c];
                }
            }
            sum+=array2[n]*(i+1);
            tpt=array;
            array=array2;
            array2=tpt;
        }
        printf("Case #%d: %.6lf\n",cn+1,sum);
    }
    return 0;
}
