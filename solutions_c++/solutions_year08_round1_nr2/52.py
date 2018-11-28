#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;
const int MaxN=200+5;
const int MaxM=40000;
int C,c,N,M,i,j,k,ans,sum,set,count;
int A[MaxN][MaxN][2];
int B[MaxN];
int map[MaxN];
bool flag;
FILE *In=fopen("B-small.in","r");
FILE *Out=fopen("B-small.out","w");
int main()
{
    fscanf(In,"%d",&C);
    for(c=1;c<=C;c++)
    {
        fscanf(In,"%d",&N);
        fscanf(In,"%d",&M);
        for(i=0;i<M;i++)
        {
            fscanf(In,"%d",&B[i]);
            for(j=0;j<B[i];j++)
                fscanf(In,"%d%d",&A[i][j][0],&A[i][j][1]);
        }
        ans=-1;
        for(i=0;i<(1<<N);i++)
        {
            memset(map,0,sizeof(map));
            j=count=0;
            set=i;
            while (set>0)
            {
                if (set&1)
                {
                    map[j]=1;
                    count++;
                }
                set>>=1;
                j++;
            }
            for(j=0;j<M;j++)
            {
                flag=0;
                for(k=0;k<B[j];k++)
                    if (map[A[j][k][0]-1]==A[j][k][1])
                        flag=1;
                if (!flag) break;
            }
            if (flag)
            {
                if (ans==-1)
                {
                    ans=i;
                    sum=count;
                }
                else
                {
                    if (count<sum)
                    {
                        ans=i;
                        sum=count;
                    }
                }
            }
        }
        fprintf(Out,"Case #%d: ",c);
        if (ans==-1)
            fprintf(Out,"IMPOSSIBLE\n");
        else
        {
            for(i=0;i<N;i++)
            {
                if (i<N-1)
                    fprintf(Out,"%d ",ans%2);
                else
                    fprintf(Out,"%d\n",ans%2);
                ans>>=1;
            }
        }
    }
    return 0;
}
