#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
using namespace std;
const int MaxN=100+5;
const int MaxM=1000+5;
int T,t,S,Q,i,j,k,Ans;
char Name[MaxN][MaxN];
char Cur[MaxN];
char c;
int DP[MaxN][MaxM];
FILE *In=fopen("A-large.in","r");
FILE *Out=fopen("A-large.out","w");
int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
        memset(Name,0,sizeof(Name));
        fscanf(In,"%d\n",&S);
        for(i=0;i<S;i++)
        {
            j=0;
            while (fscanf(In,"%c",&c)!=EOF)
            {
                if (c==10) break;
                Name[i][j++]=c;
            }
        }
        fscanf(In,"%d\n",&Q);
        memset(DP,63,sizeof(DP));
        for(i=0;i<S;i++)
            DP[i][0]=0;
        for(i=0;i<Q;i++)
        {
            memset(Cur,0,sizeof(Cur));
            j=0;
            while (fscanf(In,"%c",&c)!=EOF)
            {
                if (c==10) break;
                Cur[j++]=c;
            }
            for(j=0;j<S;j++)
                if (strcmp(Name[j],Cur)==0)
                {
                    for(k=0;k<S;k++)
                        if (k!=j)
                            DP[k][i+1]<?=DP[j][i]+1;
                }
                else
                    DP[j][i+1]<?=DP[j][i];
        }
        Ans=1000000000;
        for(i=0;i<S;i++)
            Ans<?=DP[i][Q];
        fprintf(Out,"Case #%d: %d\n",t,Ans);
    }
    return 0;
}
