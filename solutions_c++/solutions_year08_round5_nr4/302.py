#include <cstdio>
#include <string>
#define prime 10007
using namespace std;

const int dx[]={2,1};
const int dy[]={1,2};
int opt[105][105],tot,h,w,n,x,y;
bool visit[105][105];

int main(){
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d%d%d",&h,&w,&n);
        memset(visit,false,sizeof(visit));
        for (int i=0;i<n;++i){
            scanf("%d%d",&x,&y);
            visit[x][y]=true;
        }
        memset(opt,0,sizeof(opt));
        opt[1][1]=1;
        for (int i=1;i<=h;++i)
            for (int j=1;j<=w;++j){
                if (visit[i][j]) continue;
                for (int des=0;des<2;++des){
                    int nx=i+dx[des];
                    int ny=j+dy[des];
                    if (visit[nx][ny]) continue;
                    (opt[nx][ny]+=opt[i][j])%=prime;
                }
            }
        printf("Case #%d: %d\n",cases+1,opt[h][w]);
    }
    return 0;
}
