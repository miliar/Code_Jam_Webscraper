#include<stdio.h>
#include<string.h>
const int size1 = 110;
int fx[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
//int fx[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};

int num;
int n;
int h,w;
int now;

int map[size1][size1];
int out[size1][size1];
int temp[size1*size1][2];
void fz(int flag);

void dfs(int x , int y){
    num++;
    temp[num][0] = x;
    temp[num][1] = y;
    int min_x = 9999999;
    int dx = -1 , dy = -1;
    for(int i = 0 ; i < 4 ; i++ ){
        int nx = x+fx[i][0];
        int ny = y+fx[i][1];
        if(nx>=1 && nx<= h && ny >= 1 && ny <= w ){
            if(map[nx][ny]<map[x][y] && map[nx][ny] < min_x){
                min_x = map[nx][ny];
                dx = nx;
                dy = ny;
            }
        }
    }
    //if(x == 2 && y == 3) printf("???%d %d\n",dx,dy);
    if(min_x > map[x][y]){
            now++;
            fz(now);
    }
    else{
        if(out[dx][dy]!=0){
            fz(out[dx][dy]);
        }
        else{
            dfs(dx,dy);
        }
    }
}

void fz(int flag){
    for(int i = 1 ; i<=num ;i++){
        out[temp[i][0]][temp[i][1]] = flag;
    }
}

int main(){
    //freopen("B-small.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    scanf("%d",&n);
    for(int _case = 1 ; _case <= n ; _case++ ){
        scanf("%d%d",&h,&w);
        for(int i = 1 ; i<= h ; i++ ){
            for(int j = 1 ; j<=w; j++){
                scanf("%d",&map[i][j]);
            }
        }
        memset(out,0,sizeof(out));
        now = 0;
        for(int i = 1 ; i<= h ; i++ ){
            for(int j = 1 ; j<=w; j++){
                if(out[i][j]==0){
                    memset(temp,-1,sizeof(temp));
                    num = 0;
                    dfs(i,j);
                }
            }
        }
        printf("Case #%d:\n",_case);
        for(int i = 1 ; i<=h ; i++){
            for(int j = 1 ; j <= w ; j++){
                if(j!=w)
                printf("%c ",out[i][j]+'a'-1);
                else
                printf("%c\n",out[i][j]+'a'-1);
            }
        }
    }
    return 0;
}
