/*
TASK: A-boolean
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#define MAXX(X,Y) ((X)>(Y)?(X):(Y))
#define MINN(X,Y) ((X)<(Y)?(X):(Y))
#define INFINI 1234567


int n,m,t;
int a[50010];
int g[50010];
int c[50010];
int d[50010];
int ans[2][50010]={0};
FILE *fin,*fout;

int main()
{
    int sss,ss;
    int i;
    fin = fopen("A-large.in","r");
    fout = fopen("A-large.out","w");
    fscanf(fin,"%d",&sss);
    for(ss=1;ss<=sss;ss++)
    {
        printf("--%d--\n",ss);
        fscanf(fin,"%d %d",&n,&t);
        for(i=1;i<=(n-1)/2;i++)
        {
            fscanf(fin,"%d %d",&g[i],&c[i]);
        }
        for(i=(n+1)/2;i<=n;i++)
        {
            fscanf(fin,"%d",&d[i]);
            ans[d[i]][i] = 0;
            ans[1-d[i]][i] = INFINI;
        }
        for(i=(n-1)/2;i>=1;i--)
        {
            //unchangable
            {
                if(g[i]) //and
                {
                    if(ans[1][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                        ans[1][i] = ans[1][2*i]+ans[1][2*i+1];
                    else ans[1][i] = INFINI;
                    ans[0][i] = INFINI;
                    if(ans[1][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                        ans[0][i] = MINN(ans[0][i],ans[1][2*i]+ans[0][2*i+1]);
                    if(ans[0][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                        ans[0][i] = MINN(ans[0][i],ans[0][2*i]+ans[1][2*i+1]);
                    if(ans[0][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                        ans[0][i] = MINN(ans[0][i],ans[0][2*i]+ans[0][2*i+1]);
                }
                else
                {
                    if(ans[0][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                        ans[0][i] = ans[0][2*i]+ans[0][2*i+1];
                    else ans[0][i] = INFINI;
                    ans[1][i] = INFINI;
                    if(ans[0][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                        ans[1][i] = MINN(ans[1][i],ans[0][2*i]+ans[1][2*i+1]);
                    if(ans[1][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                        ans[1][i] = MINN(ans[1][i],ans[1][2*i]+ans[0][2*i+1]);
                    if(ans[1][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                        ans[1][i] = MINN(ans[1][i],ans[1][2*i]+ans[1][2*i+1]);
                }
            }
            if(!c[i]) continue;
            if(g[i]) //and change to or
            {
                if(ans[0][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                    ans[0][i] = MINN(ans[0][i],ans[0][2*i]+ans[0][2*i+1]+1);
                if(ans[0][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                    ans[1][i] = MINN(ans[1][i],ans[0][2*i]+ans[1][2*i+1]+1);
                if(ans[1][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                    ans[1][i] = MINN(ans[1][i],ans[1][2*i]+ans[0][2*i+1]+1);
                if(ans[1][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                    ans[1][i] = MINN(ans[1][i],ans[1][2*i]+ans[1][2*i+1]+1);
            }
            else
            {
                if(ans[1][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                    ans[1][i] = MINN(ans[1][i],ans[1][2*i]+ans[1][2*i+1]+1);
                if(ans[1][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                    ans[0][i] = MINN(ans[0][i],ans[1][2*i]+ans[0][2*i+1]+1);
                if(ans[0][2*i]!=INFINI && ans[1][2*i+1]!=INFINI)
                    ans[0][i] = MINN(ans[0][i],ans[0][2*i]+ans[1][2*i+1]+1);
                if(ans[0][2*i]!=INFINI && ans[0][2*i+1]!=INFINI)
                    ans[0][i] = MINN(ans[0][i],ans[0][2*i]+ans[0][2*i+1]+1);
            }
        }
        if(ans[t][1]!=INFINI) fprintf(fout,"Case #%d: %d\n",ss,ans[t][1]);
        else fprintf(fout,"Case #%d: IMPOSSIBLE\n",ss);
    }
    system("PAUSE");
    return 0;
}
