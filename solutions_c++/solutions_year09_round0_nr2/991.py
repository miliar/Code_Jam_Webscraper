#include<iostream>

using namespace std;

int map[100][100],d[100][100],dx[4]={-1,0,0,1},dy[4]={0,-1,1,0},n,h,w;

int f(int x,int y){
    int &res=d[x][y];
    if(res<0){
        int a=map[x][y],k=4;
        for(int i=0;i<4;++i)
            if(x+dx[i]>=0&&x+dx[i]<h&&y+dy[i]>=0&&y+dy[i]<w)
                if(map[x+dx[i]][y+dy[i]]<a){
                    a=map[x+dx[i]][y+dy[i]];
                    k=i;
                }
        if(k==4)res=n++;
        else res=f(x+dx[k],y+dy[k]);
    }
    return res;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        n=0;
        scanf("%d %d",&h,&w);
        for(int i=0;i<h;++i)
            for(int j=0;j<w;++j)
                scanf("%d",&map[i][j]);
        memset(d,-1,sizeof(d));
        printf("Case #%d:\n",t);
        for(int i=0;i<h;++i,printf("\n"))
            for(int j=0;j<w;++j){
                if(j)putchar(' ');
                printf("%c",'a'+f(i,j));
            }
    }
    return 0;
}
