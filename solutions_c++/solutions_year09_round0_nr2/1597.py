#include<iostream>
using namespace std;
#define myfor(i,c,d) for(i = (c);i<=(d);++i)
int walk[4][2] = {{-1,0},{0,-1},{0,+1},{1,0}};
const int H_size= 120;
const int W_size = 120;
int color[H_size][W_size];
int h,w;
int map[H_size][W_size];
bool flow_judge(int x,int y,int x1,int y1)//from x,y to x1,y1
{
    int i;
    int low,tx,ty,k;
    if(map[x][y]<=map[x1][y1]) return false;
    low = INT_MAX;
    myfor(i,0,3)
    {
        tx = x+walk[i][0];
        ty = y+walk[i][1];
        if( tx<=0||tx>h||ty<=0||ty>w||map[tx][ty]>=map[x][y]) continue;
        if( map[tx][ty]<low) {
            low = map[tx][ty];
            k = i;
        }
    }
    tx = x + walk[k][0];
    ty = y+ walk[k][1];
    if( tx == x1 && ty == y1) return true;
    else return false;
}
void dfs(int x,int y,int nc)
{
    int i,tx,ty;
    color[x][y] = nc;
    myfor(i,0,3)
    {
        tx = x+walk[i][0];
        ty = y+walk[i][1];
        if( tx<=0||tx>h||ty<=0||ty>w||color[tx][ty]) continue;
        if( flow_judge(x,y,tx,ty)||flow_judge(tx,ty,x,y)) dfs(tx,ty,nc);
    }
}
int main()
{
    int i,j,tcase,cc;
    int nc;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tcase);
    myfor(cc,1,tcase)
    {
        scanf("%d%d",&h,&w);
        myfor(i,1,h)
            myfor(j,1,w)
            scanf("%d",&map[i][j]);
        memset(color,0,sizeof(color));
        nc = 'a';
        myfor(i,1,h)
            myfor(j,1,w)
            if( color[i][j]==0)
            {
                dfs(i,j,nc);
                ++nc;
            }
            printf("Case #%d:\n",cc);
            myfor(i,1,h)
            {
                myfor(j,1,w)
                 if(j == w)printf("%c\n",color[i][j]);
                 else printf("%c ",color[i][j]);
            }
    }
}