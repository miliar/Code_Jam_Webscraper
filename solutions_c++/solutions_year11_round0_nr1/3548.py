#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int n;
struct C
{
    char t;
    int p;
}c[1005];
int dist[105][105][105];
int queue[2000000][3];
int front,back;
void update(int p,int x,int y,int key)
{
    if(dist[p][x][y]==-1)
    {
        queue[back][0]=p,queue[back][1]=x,queue[back][2]=y;
        dist[p][x][y]=key;
        back++;
    }
}
int min (int x,int y)
{
    if(x<y) return x;
    return y;
}
int bfs(int p,int x,int y)
{
    int i,j;
    int pp,xx,yy;
    front=0,back=1;
    queue[0][0]=0,queue[0][1]=x,queue[0][2]=y;
    dist[p][x][y]=0;
    int ans=999999999;
    while(front<back)
    {
        pp=queue[front][0],xx=queue[front][1],yy=queue[front][2];
        int key=dist[pp][xx][yy];
        front++;
        if(pp==n) ans=min(ans,key);
        //if(pp==3&&xx==4)
            //printf("%d %d\n",xx,yy);
        for(i=-1;i<=1;i++)
            for(j=-1;j<=1;j++)
            {
                if(xx+i>0&&xx+i<=100&&yy+j>0&&yy+j<=100)
                    update(pp,xx+i,yy+j,key+1);
            }
        if(c[pp].t=='O'&&c[pp].p==xx)
        {
            for(j=-1;j<=1;j++)
            {
                if(yy+j>0&&yy+j<=100)
                    update(pp+1,xx,yy+j,key+1);
            }
        }
        if(c[pp].t=='B'&&c[pp].p==yy)
        {
            for(i=-1;i<=1;i++)
            {
                if(xx+i>0&&xx+i<=100)
                    update(pp+1,xx+i,yy,key+1);
            }
        }
    }
    return ans;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int i,j,k;
    int T;
    scanf("%d",&T);
    int case_cnt=0;
    while(T--)
    {

        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            c[i].t=getchar();
            while(c[i].t>'Z'||c[i].t<'A') c[i].t=getchar();
            scanf("%d",&c[i].p);
        }
        memset(dist,-1,sizeof(dist));
        printf("Case #%d: %d\n",++case_cnt,bfs(0,1,1));
    }
}
