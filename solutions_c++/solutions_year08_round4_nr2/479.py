#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int T,t,N,M,A,i,j,k,l;
bool flag;
FILE *In=fopen("B-small.in","r");
FILE *Out=fopen("B-small.out","w");
int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
        fscanf(In,"%d%d%d",&N,&M,&A);
        flag=0;
        fprintf(Out,"Case #%d: ",t);
        for(i=0;i<=N;i++)
        {
            for(j=0;j<=M;j++)
            {
                for(k=0;k<=N;k++)
                {
                    for(l=0;l<=M;l++)
                    {
                        if (abs(i*l-j*k)==A)
                        {
                            fprintf(Out,"0 0 %d %d %d %d\n",i,j,k,l);
                            flag=1;
                            break;
                        }
                    }
                    if (flag) break;
                }
                if (flag) break;
            }
            if (flag) break;
        }
        if (!flag)
            fprintf(Out,"IMPOSSIBLE\n");
    }
    return 0;
}
