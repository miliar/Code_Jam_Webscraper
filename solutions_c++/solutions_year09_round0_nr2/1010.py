#include<stdio.h>
const int dx[10]={-1,0,0,1};
const int dy[10]={0,-1,1,0};
int r,c,map[110][110],visit[110][110],tag;
int dfs(int x,int y)
{
    if(visit[x][y]) return visit[x][y];
    int low=999999,i,best;
    for(i=0;i<4;i++)
    {
        if(map[x+dx[i]][y+dy[i]]<low)
        {
            low=map[x+dx[i]][y+dy[i]];
            best=i;
        }
    }
    if(low<map[x][y])
    {
        visit[x][y]=dfs(x+dx[best],y+dy[best]);
    }
    else
    {
        if(visit[x][y]) return visit[x][y];
        tag++;
        visit[x][y]=tag;
        return visit[x][y];
    }
    
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int ncase,nc,i,j;
    scanf("%d",&ncase);
    for(nc=1;nc<=ncase;nc++)
    {
        scanf("%d%d",&r,&c);
        for(i=0;i<=r+1;i++) for(j=0;j<=c+1;j++) map[i][j]=999999;
        for(i=1;i<=r;i++) 
            for(j=1;j<=c;j++)scanf("%d",&map[i][j]);
        tag=0;
        for(i=1;i<=r;i++)
            for(j=1;j<=c;j++) visit[i][j]=0;
        //printf("%d\n",visit[1][1]);
        for(i=1;i<=r;i++)
            for(j=1;j<=c;j++)
            if(!visit[i][j])
            {
                dfs(i,j);
            }
        printf("Case #%d:\n",nc);
        //printf("%d\n",visit[1][1]);
        for(i=1;i<=r;i++)
        {            
            printf("%c",visit[i][1]-1+'a');
            for(j=2;j<=c;j++) printf(" %c",visit[i][j]-1+'a');
            printf("\n");
        }
    }
    return 0;
}
