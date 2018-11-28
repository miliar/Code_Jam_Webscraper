#include <cstdio>
#include <iostream>
#include <memory>
#include <algorithm>
#define MAXM 80
#define MAXN 80
#define MAXP 6400
using namespace std;

const int dx[6]={-1,0,1,-1,0,1};
const int dy[6]={-1,-1,-1,1,1,1};
char board[MAXM+1][MAXN+1];
bool visited[MAXP+1];
int match[MAXP+1];
int m,n,p,maxmatch;

int DFS(int x,int y)
{
    int d,nx,ny;
    for(d=0;d<6;d++)
    {
        nx=x+dx[d];
        ny=y+dy[d];
        if((nx>=0)&&(nx<m)&&(ny>=0)&&(ny<n)&&(board[nx][ny]=='.')&&(visited[nx*n+ny]==false))
        {
            visited[nx*n+ny]=true;
            if((match[nx*n+ny]==-1)||(DFS(match[nx*n+ny]/n,match[nx*n+ny]%n)>0))
            {
                match[nx*n+ny]=x*n+y;
                match[x*n+y]=nx*n+ny;
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,k,t;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        scanf("%d %d",&m,&n);
        for(i=0;i<m;i++)
        {
            scanf("%s",board[i]);
        }
        memset(match,-1,sizeof(match));
        p=maxmatch=0;
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                if(board[i][j]=='.')
                {
                    p++;
                    if(((j&1)==0)&&(match[i*n+j]==-1))
                    {
                        memset(visited,0,sizeof(visited));
                        maxmatch=maxmatch+DFS(i,j);
                    }
                }
            }
        }
        printf("Case #%d: %d\n",k+1,p-maxmatch);
    }
    return 0;
}
