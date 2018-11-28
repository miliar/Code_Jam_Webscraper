/*
TASK: House of Kittens
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int N,M,T;
int st[2010],ed[2010];
bool g[23][23];
int cycle[1024][10],num_c[1024];
int ans[10],idx;
int use[10],cy;
void commu(int x,int num,int Mc)
{
    if(num==Mc)
    {
        use[Mc]=use[0];
        for(int i=0;i<Mc;i++)
            if(g[use[i]][use[i+1]]!=1)
                return;
        for(int i=0;i<Mc;i++)
            cycle[idx][i]=use[i];
        num_c[idx]=Mc;
        cy=min(cy,Mc);
        idx++;
        return;
    }
    for(int i=x;i<=N;i++)
    {
        use[num]=i;
        commu(i+1,num+1,Mc);
    }
}
bool ok=false;
bool co_color[12];
void gen_color(int x)
{
    if(x==N+1)
    {
        int co_it,i,j;
        for(i=0;i<idx;i++)
        {
            co_it=0;
            for(j=1;j<=cy;j++)
                co_color[j]=0;
            for(j=0;j<num_c[i];j++)
            {
                if(!co_color[ans[cycle[i][j]]])
                    co_it++;
                co_color[ans[cycle[i][j]]]=true;
            }
            if(co_it<cy)
                return;
        }
        ok=true;
        return;
    }
    for(int i=1;i<=cy;i++)
    {
        ans[x]=i;
        gen_color(x+1);
        if(ok)
            break;
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int i,j,k,tt=0;
    scanf("%d",&T);
    while(T--)
    {
        tt++;
        scanf("%d%d",&N,&M);
        for(i=1;i<N;i++)
        {
            g[i][i+1]=1;
            g[i+1][i]=1;
        }
        g[N][1]=1;
        g[1][N]=1;
        idx=0;
        for(i=1;i<=M;i++)
            scanf("%d",&st[i]);
        for(i=1;i<=M;i++)
            scanf("%d",&ed[i]);
        for(i=1;i<=M;i++)
        {
            g[st[i]][ed[i]]=1;
            g[ed[i]][st[i]]=1;
        }
/*
        for(i=1;i<=N;i++)
        {
            for(j=1;j<=N;j++)
                printf("%d ",g[i][j]);
            printf("\n");
        }
//*/
        idx=0;
        cy=127;
        for(i=3;i<=N;i++)
            commu(1,0,i);
/*
        for(i=0;i<idx;i++)
        {
            for(j=0;j<num_c[i];j++)
                printf("%d ",cycle[i][j]);
            printf("\n");
        }
//*/
        //----- find color
        ok=false;
        gen_color(1);
        printf("Case #%d: %d\n",tt,cy);
        printf("%d",ans[1]);
        for(i=2;i<=N;i++)
            printf(" %d",ans[i]);
        printf("\n");
        for(i=1;i<=N;i++)
            for(j=1;j<=N;j++)
                g[i][j]=0;
        for(i=1;i<=1000;i++)
            for(j=1;j<=8;j++)
                cycle[i][j]=0;
    }
}
