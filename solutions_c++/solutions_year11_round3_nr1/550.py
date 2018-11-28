#include<stdio.h>

int main() {
    char xc[100][100];
    int c,cnt,i,j,ok,r,t,x[100][100],x1[100][100];
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++) {
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++) {
            scanf("%s",&xc[i]);
            for(j=0;j<c;j++) {
                if(xc[i][j]=='#')x[i][j]=1;
                else x[i][j]=0;
            }
        }
        for(i=0;i<=r;i++)for(j=0;j<=c;j++)x1[i][j]=0;
        for(i=0;i<r;i++)for(j=0;j<c;j++)x1[i][j]=x[i][j];
        ok=1;
        for(i=0;i<r;i++) {
            //check for uncovered blue, if they are contiguous for 2x2
            for(j=0;j<c;j++) {
                if(x1[i][j]==1) {
                    if((x1[i][j+1]==1)&&(x1[i+1][j]==1)&&(x1[i+1][j+1]==1)) {
                        x1[i][j]=2;x1[i][j+1]=3;
                        x1[i+1][j]=3;x1[i+1][j+1]=2;
                    }
                    else ok=0;
                }
                if(!ok)break;
            }
            if(!ok)break;
        }
        printf("Case #%d:\n",cnt);
        if(!ok)printf("Impossible\n");
        else {
            for(i=0;i<r;i++) {
                for(j=0;j<c;j++) {
                    switch(x1[i][j]) {
                        case 0:printf(".");break;
                        case 1:printf("#");break;
                        case 2:printf("/");break;
                        case 3:printf("\\");break;
                    }
                }
                printf("\n");
            }
        }
    }
    return 0;
}
