#define maxn 110
#include<iostream>
using namespace std;
struct Tqueue{
    int x,y;
};
int c, H, W;
int height[maxn][maxn];
char sign[maxn][maxn];
Tqueue q[maxn *maxn];
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};


void init(){
    scanf("%d%d",&H,&W);
    for (int i=0;i<H;i++)
        for (int j=0;j<W;j++)
            scanf("%d",&height[i][j]);
}

bool flow(int x,int y,int &fx,int &fy){
    int mi = height[x][y];
    for (int i=0;i<4;i++) {
        int xx = x + dx[i];
        int yy = y + dy[i];
        if (xx<0 || xx>=H || yy<0 || yy>=W) continue;
        if (height[xx][yy]<mi) {
            fx = xx;
            fy = yy;
            mi = height[xx][yy];
        }
    }
    return (mi!=height[x][y]);
}

void process(int sx,int sy,char bash){
    int head = 0, tail = 0;
    sign[sx][sy]=bash;
    q[head].x=sx;
    q[head].y=sy;
    while (head<=tail) {
        int xx = 0, yy = 0;
        if (flow(q[head].x, q[head].y, xx, yy) && sign[xx][yy]==0){
            tail++;
            q[tail].x = xx;
            q[tail].y = yy;
            sign[xx][yy]=bash;
        }
        for (int i=0;i<4;i++) {
            int x = q[head].x+dx[i];
            int y = q[head].y+dy[i];
            if (x<0 || x>=H || y<0 || y>=W) continue;
            if (sign[x][y]!=0) continue;
            if (flow(x,y,xx,yy) && xx==q[head].x && yy==q[head].y){
                tail++;
                q[tail].x = x;
                q[tail].y = y;
                sign[x][y]=bash;
            }
        }
        head++;
    }
}

void print(){
    for (int i=0;i<H;i++){
        for (int j=0;j<W-1;j++) printf("%c ",sign[i][j]);
        printf("%c\n",sign[i][W-1]);
    }
}

int main(){
    scanf("%d",&c);
    for (int cs = 1;cs<=c;cs++){
        init();
/*        cout<<"2 1";
        int xxx,yyy;
        flow(2,1,xxx,yyy);
        cout<<" -> "<<xxx<<" "<<yyy<<endl;
*/
        memset(sign, 0, sizeof sign);
        char bash='a';
        for (int i=0;i<H;i++)
            for (int j=0;j<W;j++){
                if (sign[i][j]!=0) continue;
                process(i, j, bash);
                bash++;
            }
        printf("Case #%d:\n",cs);
        print();
    }
}

