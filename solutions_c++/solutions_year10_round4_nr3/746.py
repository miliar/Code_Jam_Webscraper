#include<stdio.h>
#include<stdlib.h>
int map[200][200];
int main(){
    int c;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&c);
    for(int time=1;time<=c;time++){
        int r;
        scanf("%d",&r);
        for(int i=0;i<100;i++)
        for(int j=0;j<100;j++)map[i][j]=0;
        int c=0;
        for(int i=0;i<r;i++){
            int x1,x2,y1,y2;
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);

            for(int x=x1;x<=x2;x++){
                for(int y=y1;y<=y2;y++){
                    if(map[x][y]==0){
                        map[x][y]=1;
                        c++;
                    }
                }
            }
        }
        int ans=0;
        while(c>0){
            ans++;
            for(int x=100;x>0;x--){
                for(int y=100;y>0;y--){
                    if(map[x][y]==1){
                        if(map[x-1][y]==0&&map[x][y-1]==0){
                            map[x][y]=0;
                            c--;
                        }
                    }
                    else{
                        if(map[x-1][y]==1&&map[x][y-1]==1){
                            map[x][y]=1;
                            c++;
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n",time,ans);
    }
}
