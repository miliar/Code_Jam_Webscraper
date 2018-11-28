#include <stdio.h>
#include <limits.h>
#include <string.h>
const int xmv[4]={-1,0,0,1},ymv[4]={0,-1,1,0};
char visited[110][110],isdir[110][110][4],tch;
void recur(int x,int y)
{
    if(!visited[x][y])
    {
        visited[x][y]=tch;
        for(int i=0;i<4;i++)
            if(isdir[x][y][i])
                recur(x-xmv[i],y-ymv[i]);
    }
}
int main()
{
    freopen("codejam.in","r",stdin);
    freopen("codejam.out","w",stdout);
    int tc,c,i,j,k,x,y,alt[110][110],IsSink[110][110],m,d;
    char chmap[26];
    scanf("%d",&tc);
    for(c=0;c<tc;c++)
    {
        scanf("%d%d",&x,&y);
        for(i=0;i<=x+1;i++)
        {
            alt[i][0]=INT_MAX;
            alt[i][y+1]=INT_MAX;
        }
        for(i=0;i<=y+1;i++)
        {
            alt[0][i]=INT_MAX;
            alt[x+1][i]=INT_MAX;
        }
        for(i=1;i<=x;i++)
            for(j=1;j<=y;j++)
            {
                IsSink[i][j]=0;
                visited[i][j]=0;
                isdir[i][j][0]=0;
                isdir[i][j][1]=0;
                isdir[i][j][2]=0;
                isdir[i][j][3]=0;
                scanf("%d",&alt[i][j]);
            }
        for(i=1;i<=x;i++)
            for(j=1;j<=y;j++)
            {
                m=INT_MAX;
                for(k=0;k<4;k++)
                {
                    if(alt[i+xmv[k]][j+ymv[k]]<m)
                    {
                        m=alt[i+xmv[k]][j+ymv[k]];
                        d=k;
                    }
                }
                if(alt[i+xmv[d]][j+ymv[d]]<alt[i][j])
                    isdir[i+xmv[d]][j+ymv[d]][d]=1;
                else
                    IsSink[i][j]=1;
            }
        tch=0;
        for(i=1;i<=x;i++)
            for(j=1;j<=y;j++)
            {
                if(IsSink[i][j])
                {
                    recur(i,j);
                    tch++;
                }
            }
        printf("Case #%d:\n",c+1);
        tch='a';
        memset(chmap,0,26);
        for(i=1;i<=x;i++)
            for(j=1;j<=y;j++)
                if(!chmap[visited[i][j]])
                    chmap[visited[i][j]]=tch++;
        for(i=1;i<=x;i++)
        {
            for(j=1;j<=y;j++)
            {
                if(j!=1)
                    printf(" ");
                printf("%c",chmap[visited[i][j]]);
            }
            printf("\n");
        }
    }
    return 0;
}
