#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;
int T,t,N;
int ans[2][2];
int tmp[2][2];
int matrix[2][2];
FILE *In=fopen("C-large.in","r");
FILE *Out=fopen("C-large.out","w");
void solve(int N)
{
    int i,j,k;
    while (N>0)
    {
        if(N&1)
        {
            memset(tmp,0,sizeof(tmp));
            for(i=0;i<2;i++)
                for(j=0;j<2;j++)
                    for(k=0;k<2;k++)
                    {
                        tmp[i][k]+=ans[i][j]*matrix[j][k]+1000000;
                        tmp[i][k]%=1000;
                    }
            memcpy(ans,tmp,sizeof(tmp));
        }
        memset(tmp,0,sizeof(tmp));
        for(i=0;i<2;i++)
            for(j=0;j<2;j++)
                for(k=0;k<2;k++)
                {
                    tmp[i][k]+=matrix[i][j]*matrix[j][k]+1000000;
                    tmp[i][k]%=1000;
                }
        memcpy(matrix,tmp,sizeof(tmp));
        N>>=1;
    }
}

int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
        ans[0][0]=6;
        ans[0][1]=28;
        matrix[0][0]=0;
        matrix[0][1]=-4;
        matrix[1][0]=1;
        matrix[1][1]=6;
        fscanf(In,"%d",&N);
        fprintf(Out,"Case #%d: ",t);
        solve(N-1);
        ans[0][0]+=1000000;
        ans[0][0]%=1000;
        ans[0][0]--;
        ans[0][0]+=1000000;
        ans[0][0]%=1000;
        if (ans[0][0]<1) fprintf(Out,"000\n");
        else if (ans[0][0]<10) fprintf(Out,"00%d\n",ans[0][0]);
        else if (ans[0][0]<100) fprintf(Out,"0%d\n",ans[0][0]);
        else fprintf(Out,"%d\n",ans[0][0]);
    }
    return 0;
}
