#include <stdio.h>
#include <string.h>
int h,w;
int map[110][110];
int color[110][110];
const int move[4][2]={{-1,0},{0,-1},{0,+1},{+1,0}};
int colornum;
int next(int x,int y)
{
    int i;
    int high,k;
    high=map[x][y];
    
    for (i=0;i<4;i++)
    {        
        int a=x+move[i][0];
        int b=y+move[i][1];
        
        if (a<1 || a>h) continue;
        if (b<1 || b>w) continue;
        
        if (map[a][b]<high) 
        {
            high=map[a][b];
            k=i;
        }
    }
    if (high==map[x][y]) return -1;
    else return k;
}
void colorback(int x,int y,int ori,int newc)
{
    if (color[x][y]==ori) color[x][y]=newc;
    else return;
    int i;
    for (i=0;i<4;i++) 
    {
        int a=x+move[i][0];
        int b=y+move[i][1];
        if (a<1 || a>h) continue;
        if (b<1 || b>w) continue;
        
        if (color[a][b]==ori) colorback(a,b,ori,newc);
    }
}
void go(int x,int y,int c)
{
    if (color[x][y]==c) return;
    color[x][y]=c;
    int p = next(x,y);
    if (p==-1) return;
    int a,b;
    a=x+move[p][0];
    b=y+move[p][1];
    if (color[a][b]!=0 && color[a][b]!=c) {colornum--;colorback(x,y,c,color[a][b]);}
    else go(a,b,c);
}   
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int ccs;
    scanf("%d",&ccs);
    int cs;
    for (cs=1;cs<=ccs;cs++)
    {
        printf("Case #%d:\n",cs);
        scanf("%d%d",&h,&w);
        int i,j;
        for (i=1;i<=h;i++)
            for (j=1;j<=w;j++) scanf("%d",&map[i][j]);
        memset(color,0,sizeof(color));
        
        colornum=0;
        for (i=1;i<=h;i++)
            for (j=1;j<=w;j++)
            {
                if (color[i][j]==0) {colornum++;go(i,j,colornum);}
            }
        char ctoc[30];
        memset(ctoc,0,sizeof(ctoc));
        char c='a'-1;
        for (i=1;i<=h;i++)
        {
            for (j=1;j<=w;j++)
            {
                if (ctoc[color[i][j]]==0) 
                {
                    c++;
                    ctoc[color[i][j]]=c;
                }
                printf("%c ",ctoc[color[i][j]]);
            }
            putchar('\n');
        }
    }
    return 0;
}
