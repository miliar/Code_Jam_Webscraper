#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXH 100
#define MAXW 100
#define MAXP 10000
#define INF 1000000000
using namespace std;

const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
int board[MAXH+1][MAXW+1];
int parent[MAXP+1],color[MAXP+1];
char label[MAXP+1];
int h,w,hw;

int uf_find(int x)
{
    if(parent[x]==x)
    {
        return parent[x];
    }
    else
    {
        parent[x]=uf_find(parent[x]);
        return parent[x];
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,t,x,y,d,minv,minx,miny;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        scanf("%d %d",&h,&w);
        hw=h*w;
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                scanf("%d",&board[i][j]);
                parent[i*w+j]=i*w+j;
            }
        }
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                minv=INF;
                for(d=0;d<4;d++)
                {
                    x=i+dx[d];
                    y=j+dy[d];
                    if((x>=0)&&(x<h)&&(y>=0)&&(y<w)&&(board[x][y]<board[i][j])&&(minv>board[x][y]))
                    {
                        minv=board[x][y];
                        minx=x;
                        miny=y;
                    }
                }
                if(minv<INF)
                {
                    parent[i*w+j]=minx*w+miny;
                }
            }
        }
        memset(color,-1,sizeof(color));
        j=0;
        for(i=0;i<hw;i++)
        {
            parent[i]=uf_find(i);
            if(color[parent[i]]==-1)
            {
                color[parent[i]]=j++;
            }
            label[i]=(char)(color[parent[i]]+'a');
        }
        printf("Case #%d:\n",k+1);
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                if(j>0)
                {
                    printf(" %c",label[parent[i*w+j]]);
                }
                else
                {
                    printf("%c",label[parent[i*w+j]]);
                }
            }
            printf("\n");
        }
    }
    return 0;
}
