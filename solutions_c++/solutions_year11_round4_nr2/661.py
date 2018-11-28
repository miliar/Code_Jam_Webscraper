#include<stdio.h>

char _grid[501][501];
int grid[500][500];

int main() {
    double i1,j1,k1,x,y;
    int c,cnt,d,i,ii,j,jj,k,kk,ok,ok1,r,t;
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++) {
        scanf("%d %d %d",&r,&c,&d);
        for(i=0;i<r;i++)scanf("%s",&_grid[i]);
        for(i=0;i<r;i++)for(j=0;j<c;j++)_grid[i][j]-='0';
        for(i=0;i<r;i++)for(j=0;j<c;j++)grid[i][j]=_grid[i][j]+d;
        k=r;if(c<r)k=c;
        ok=0;
        for(kk=k;kk>=3;kk--) {
            for(i=0;i<=r-kk;i++) {
                for(j=0;j<=c-kk;j++) {
                    x=0.0;
                    y=0.0;
                    k1=kk;k1/=2.0;k1-=0.5;
                    for(ii=0;ii<kk;ii++) {
                        for(jj=0;jj<kk;jj++) {
                            ok1=0;
                            if((ii==0)||(ii==(kk-1)))ok1++;
                            if((jj==0)||(jj==(kk-1)))ok1++;
                            if(ok1<2) {
                                i1=ii;i1-=k1;x+=(i1*grid[i+ii][j+jj]);
                                j1=jj;j1-=k1;y+=(j1*grid[i+ii][j+jj]);
                            }
                        }
                    }
                    if(x<0.0)x=-x;if(y<0.0)y=-y;
                    if((x<1e-6)&&(y<1e-6)){ok=kk;break;}
                }
                if(ok)break;
            }
            if(ok)break;
        }
        if(ok)printf("Case #%d: %d\n",cnt,ok);
        else printf("Case #%d: IMPOSSIBLE\n",cnt);
    }
    return 0;
}
