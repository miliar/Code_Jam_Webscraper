#include<stdio.h>
#include<string.h>

int h , w , map[102][102];
char mp[101][101] , c;
int dx[] = {-1 , 0 , 0 , 1};
int dy[] = {0 , -1 , 1 , 0};

char dfs(int x , int y){
    if(mp[x][y] != '-') return mp[x][y];

    int i , nx , ny , d = 0 , mn = 100000 , tx , ty;
    for(i = 0;i<4;i++){
        nx = x+dx[i];
        ny = y+dy[i];
        if(nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
        if(map[nx][ny] < map[x][y]){
            if(map[nx][ny] < mn){
                mn = map[nx][ny];
                tx = nx;ty = ny;
                d = 1;
            }
        }
    }
    if(d == 0) return mp[x][y] = c++;
    char p = dfs(tx , ty);
    return mp[x][y] = p;
}

int main(){
    freopen("B-large.in" , "r" , stdin);
    freopen("B-large.out" , "w" , stdout);
    int tst , i  , j , kase = 1;
    scanf("%d" , &tst);
    while(tst--){
        scanf("%d%d" , &h , &w);
        for(i = 0;i<h;i++)
            for(j = 0;j<w;j++)
                scanf("%d" , &map[i][j]);
        memset(mp , '-' , sizeof(mp));
        c = 'a';
        for(i = 0;i<h;i++)
            for(j = 0;j<w;j++){
                if(mp[i][j] == '-')
                    dfs(i , j);
            }
        printf("Case #%d:\n" , kase++);
        for(i = 0;i<h;i++){
            for(j = 0;j<w;j++){
                if(j) printf(" ");
                printf("%c" , mp[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
