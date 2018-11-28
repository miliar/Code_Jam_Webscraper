#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxN 200
int T,t,N,M,R,i,j,x,y;
int A[MaxN][MaxN];
int DP[MaxN][MaxN];
FILE *In=fopen("D-small.in","r");
FILE *Out=fopen("D-small.out","w");
int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
        memset(A,0,sizeof(A));
        fscanf(In,"%d%d%d",&N,&M,&R);
        for(i=0;i<R;i++)
        {
            fscanf(In,"%d%d",&x,&y);
            x--;y--;
            A[x][y]=1;
        }
        memset(DP,0,sizeof(DP));
        DP[0][0]=1;
        for(i=0;i<N;i++)
            for(j=0;j<M;j++)
            {
                if (i+1<N && j+2<M && !A[i+1][j+2]) DP[i+1][j+2]=(DP[i][j]+DP[i+1][j+2])%10007;
                if (i+2<N && j+1<M && !A[i+2][j+1]) DP[i+2][j+1]=(DP[i][j]+DP[i+2][j+1])%10007;
            }
        fprintf(Out,"Case #%d: %d\n",t,DP[N-1][M-1]);
    }
    return 0;
}
