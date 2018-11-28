#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
using namespace std;

int t,a[105][105],b[105][105],now,h,w;
int dx[]={-1,0,0,1},dy[]={0,-1,1,0};

void fill (int x,int y) {
    //printf("%d %d\n",x,y);
    int sx=x,sy=y;
    for (int i=0; i<4; i++) {
        int nx=x+dx[i],ny=y+dy[i];
        if (nx>=0 && nx<h && ny>=0 && ny<w && a[nx][ny]<a[sx][sy]) {
           sx=nx; sy=ny;
           }
        }
    if (sx!=x || sy!=y) {
       if (b[sx][sy]==-1) fill(sx,sy);
       b[x][y]=b[sx][sy];
       return;
       }    
    //printf("ass: %d %d  %d\n",x,y,now);
    b[x][y]=now;
    now++;
}    

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        now=0;
        scanf("%d%d",&h,&w);
        memset(a,0,sizeof(a));
        memset(b,-1,sizeof(b));
        for (int j=0; j<h; j++)
            for (int k=0; k<w; k++) 
                scanf("%d",&a[j][k]);
        for (int j=0; j<h; j++)
            for (int k=0; k<w; k++)
                if (b[j][k]==-1) {
                   fill(j,k);
                   }
        /*
        for (int j=0; j<h; j++) {
            for (int k=0; k<w; k++)
                printf("%d ",b[j][k]);
            printf("\n");
            }
        */
        printf("Case #%d:\n",i+1);
        for (int j=0; j<h; j++) {
            printf("%c",b[j][0]+'a');
            for (int k=1; k<w; k++)
                printf(" %c",b[j][k]+'a');
            printf("%\n");
            }
        }
    
}
