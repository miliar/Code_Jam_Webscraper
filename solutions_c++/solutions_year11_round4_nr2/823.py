#include<cstdio>

int main(){
    char ar[11][11];
    int tb[10][10];
    int r,c,d,t;

    scanf("%d",&t);

    for(int tt=0;tt<t;tt++)
    {

        scanf("%d %d %d",&r,&c,&d);
        for(int i=0;i<r;i++)
        {
            scanf("%s",ar[i]);
            for(int j=0;j<c;j++)
                tb[i][j]=ar[i][j]-'0'+d;
        }
/*
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                printf("%d ",tb[i][j]);
            }
            printf("\n");
        }
*/
        int max=0;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                for(int k=2;k<r-i&&k<c-j;k++)
                {
                    //if(i+k>=r||i+j>=c)
                    //    break;
                    double sumi=0,sumj=0;
                    double ci=(i+(1.0*k/2)),cj=(j+(1.0*k/2));
                    for(int ii=i;ii<=i+k;ii++)
                    {
                        for(int jj=j;jj<=j+k;jj++)
                        {
                            if((ii==i&&jj==j)||(ii==i&&jj==j+k)||(ii==i+k&&jj==j)||(ii==i+k&&jj==j+k))
                                continue;
                            sumi+=(1.0*ii-ci)*tb[ii][jj];
                            sumj+=(1.0*jj-cj)*tb[ii][jj];
                            //printf(". %d %d %d %lf %lf %lf %lf\n",ii,jj,k+1,sumi,sumj,ci,cj);
                        }
                    }
                    if(sumi<0)
                        sumi=-sumi;
                    if(sumj<0)
                        sumj=-sumj;
                    if(sumi<10E-6&&sumj<10E-6)
                    {
                        if(k+1>max)
                            max=k+1;
                    }
                    //printf("%d %d %d %lf %lf\n",i,j,k+1,sumi,sumj);
                }
            }
        }
        if(max!=0)
            printf("Case #%d: %d\n",tt+1,max);
        else
            printf("Case #%d: IMPOSSIBLE\n",tt+1);
    }

    return 0;
}

