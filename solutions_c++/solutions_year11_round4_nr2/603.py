#include<stdio.h>
#include<stdlib.h>
double abs(double x){
    if(x<-0.01)return -1.0*x;
    return x;
}
int row[510][510],col[510][510];
void solve(int test){
    printf("Case #%d: ",test);
    int r,c,d;
    scanf("%d %d %d",&r,&c,&d);
    char board[r][c];
    int ans=2;

    for(int i=0;i<r;i++)scanf("%s",board[i]);
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            board[i][j]-='0';
            row[i][j]=board[i][j];
            col[i][j]=board[i][j];
        }
    }
    for(int i=1;i<r;i++){
        for(int j=0;j<c;j++){
            col[i][j]+=col[i-1][j];
        }
    }
    for(int i=0;i<r;i++){
        for(int j=1;j<c;j++)row[i][j]+=row[i][j-1];
    }
    for(int x=0;x<r;x++){
        for(int y=0;y<c;y++){
            for(int s=ans+1;;s++){
                if(x+s>r||y+s>c)break;
                double mx=1.0*x+(s-1)/2.0;
                double my=1.0*y+(s-1)/2.0;
                double sx=0.0,sy=0.0;
                sx+=(mx-x)*(row[x][y]-row[x][y+s-2]);
                sx+=(mx-(x+s-1))*(row[x+s-1][y]-row[x+s-1][y+s-2]);
                sy+=(my-y)*(col[x][y]-col[x+s-2][y]);
                sy+=(my-(y+s-1))*(col[x][y+s-1]-col[x+s-2][y+s-1]);
                for(int d=1;d+1<s;d++){
                    sx+=(mx-(x+d))*( (y>0?row[x+d][y-1]:0)-row[x+d][y+s-1]);
                    sy+=(my-(y+d))*( (x>0?col[x-1][y+d]:0)-col[x+s-1][y+d]);
                }
                if(sx>=(-1.0)*(1e-2)&&sy>=(-1.0)*(1e-2)&&sx<=1e-2&&sy<=1e-2&&ans<s)ans=s;
            }
        }
    }

    /*for(int x=0;x<r;x++){
        for(int y=0;y<c;y++){
            for(int s=ans+1;;s++){
                if(x+s>r||y+s>c)break;
                double mx=x+(s-1)/2.0;
                double my=y+(s-1)/2.0;
                //printf("mid = %lf %lf\n",mx,my);
                double sx=0.0,sy=0.0;
                for(int dx=0;dx<s;dx++){
                    for(int dy=0;dy<s;dy++){
                        if(dx==0&&dy==0||dx==0&&dy+1==s||dy==0&&dx+1==s||dx+1==s&&dy+1==s)continue;
                        sx+=(mx-(x+dx))*(board[x+dx][y+dy]-'0');
                        sy+=(my-(y+dy))*(board[x+dx][y+dy]-'0');
                    }
                }
                //printf("%d %d %d %lf %lf\n",x,y,s,sx,sy);
                if(sx>=(-1.0)*(1e-2)&&sy>=(-1.0)*(1e-2)&&sx<=1e-2&&sy<=1e-2&&ans<s)ans=s;
            }
        }
    }*/
    if(ans==2)printf("IMPOSSIBLE\n");
    else printf("%d\n",ans);
}
int main(){
    int n;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        solve(i);
    }
}
