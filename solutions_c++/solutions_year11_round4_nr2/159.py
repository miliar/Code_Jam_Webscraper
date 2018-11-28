#include <stdio.h>
#include <string.h>

#define maxn 512

int sx[maxn][maxn];
int sy[maxn][maxn];
int vv[maxn][maxn];
int R,C,D,A;

char b[maxn][maxn];

int ok(int i,int j,int k){
    int sumx=sx[i+k][j+k]-sx[i+k][j]-sx[i][j+k]+sx[i][j]-(b[i+k-1][j]+b[i+k-1][j+k-1])*(i+k-1)-(b[i][j+k-1]+b[i][j])*i;
    int sumy=sy[i+k][j+k]-sy[i+k][j]-sy[i][j+k]+sy[i][j]-(b[i+k-1][j+k-1]+b[i][j+k-1])*(j+k-1)-(b[i+k-1][j]+b[i][j])*j;
    int sumv=vv[i+k][j+k]-vv[i+k][j]-vv[i][j+k]+vv[i][j]-b[i+k-1][j+k-1]-b[i+k-1][j]-b[i][j+k-1]-b[i][j];
    //printf("(%d,%d,%d)->(%d,%d,%d)\n",i,j,k,sumx,sumy,sumv);
    if (2*sumx != (i+i+k-1)*sumv) return 0;
    if (2*sumy != (j+j+k-1)*sumv) return 0;
    return 1;
}

void sol(int cas){
    int i,j,k;
    int ret;
    scanf("%d%d%d",&R,&C,&D);
    for (i=0;i<R;i++) scanf("%s",b[i]);
//    memset(sx,0,sizeof(sx));
//    memset(sy,0,sizeof(sy));
    if (R<C) A=R;
    else A=C;
    for (i=0;i<=R;i++) for (j=0;j<=C;j++){
        sx[i][j]=sy[i][j]=vv[i][j]=0;
        b[i][j]-='0';
    }
    for (i=0;i<R;i++) for (j=0;j<C;j++){
        sx[i+1][j+1]=b[i][j]*i;
        sy[i+1][j+1]=b[i][j]*j;
        vv[i+1][j+1]=b[i][j];
    }
    for (i=0;i<R;i++) for (j=0;j<=C;j++){
        sx[i+1][j]+=sx[i][j];
        sy[i+1][j]+=sy[i][j];
        vv[i+1][j]+=vv[i][j];
    }
    for (i=0;i<=R;i++) for (j=0;j<C;j++){
        sx[i][j+1]+=sx[i][j];
        sy[i][j+1]+=sy[i][j];
        vv[i][j+1]+=vv[i][j];
    }
    ret = -1;
    for (k=A;k>=3&&ret<0;k--){
        for (i=0;i<=R-k&&ret<0;i++) for (j=0;j<=C-k;j++){
            if (ok(i,j,k)){
                //printf("(%d,%d,%d)\n",i,j,k);
                ret=k;
                break;
            }
        }
    }
    if (ret==-1) printf("Case #%d: IMPOSSIBLE\n",cas);
    else printf("Case #%d: %d\n", cas, ret);
}

int main(){
    int t,cas;
    scanf("%d",&t);
    for (cas=1;cas<=t;cas++) sol(cas);
    return 0;
}

