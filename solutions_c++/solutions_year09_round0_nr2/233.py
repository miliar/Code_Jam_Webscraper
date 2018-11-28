#include<iostream>
using namespace std;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
const int maxw=110;
const int maxn=maxw*maxw;
int cases,tt,h,w,tot,edge,col[30],ck[maxw][maxw],a[maxw][maxw],num[maxw][maxw],ans[maxn],head[maxn],ptr[maxn],next[maxn];
void init()
{
     scanf("%d%d",&h,&w);
     int i,j;
     tot=0;
     memset(head,0,sizeof(head));
     edge=0;
     for (i=0;i<h;i++)
         for (j=0;j<w;j++)
         {
             scanf("%d",&a[i][j]);     
             num[i][j]=tot;
             tot++;
         }
}

void dfs(int x)
{
     ans[x]=tot;
     int i;
     for (i=head[x];i;i=next[i])
     dfs(ptr[i]);
}

void adde(int x,int y)
{
     edge++;
     next[edge]=head[x];
     head[x]=edge;
     ptr[edge]=y;
}

void work()
{
     int i,j,k,i1,j1,i2,j2;
     memset(ck,0,sizeof(ck));
     for (i=0;i<h;i++)
         for (j=0;j<w;j++)
         {
             i2=-1;
             for (k=0;k<4;k++)
             {
                 i1=i+dx[k];
                 j1=j+dy[k];
                 if ((i1>=0)&&(i1<h)&&(j1>=0)&&(j1<w)&&(a[i][j]>a[i1][j1])) 
                    if ((i2==-1)||(a[i2][j2]>a[i1][j1]))
                    {
                       i2=i1;
                       j2=j1;
                    }
             }
             if (i2==-1) ck[i][j]=1;
             else adde(num[i2][j2],num[i][j]);
         }
     tot=0;
     for (i=0;i<h;i++)
         for (j=0;j<w;j++)
         if (ck[i][j])
         {
            dfs(num[i][j]);
            tot++;
         }
     memset(col,-1,sizeof(col));
     tot=0;
     for (i=0;i<h;i++)
         for (j=0;j<w;j++)
         if (col[ans[num[i][j]]]==-1)
         {
            col[ans[num[i][j]]]=tot;
            tot++;
         }
}

void print()
{
     printf("Case #%d:\n",tt+1);
     int i,j;
     for (i=0;i<h;i++)
         for (j=0;j<w;j++)
             printf("%c%c",col[ans[num[i][j]]]+'a',j==(w-1)?'\n':' ');
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        init();
        work();
        print();
    }
    return 0;
}
