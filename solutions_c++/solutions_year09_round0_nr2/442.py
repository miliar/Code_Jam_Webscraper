#include <stdio.h>
#include <cstring>

const int diri[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int H, W;
int alti[128][128], fill[128][128], q[10010];
bool map[128][128][4];

inline bool valid(int x, int y){
    return (x >= 0 && y >= 0 && x < H && y < W);
}

int find(){
    for(int i = 0;i < H;i++)
        for(int j = 0;j < W;j++)
            if(fill[i][j] < 0)
                return (i * W + j);
    return -1;
}

int main(){
    int testnum, fillch, head, tail, temp, tmpalti, tdir, x, y, nx, ny;

    scanf("%d", &testnum);
    for(int test = 1;test <= testnum;test++){
        memset(map, false, sizeof(map));
        memset(fill, 0xff, sizeof(fill));
        scanf("%d%d", &H, &W);
        for(int i = 0;i < H;i++)
            for(int j = 0;j < W;j++)
                scanf("%d", &alti[i][j]);
        for(int i = 0;i < H;i++){
            for(int j = 0;j < W;j++){
                tmpalti = alti[i][j];tdir = -1;
                for(int dir = 0;dir < 4;dir++){
                    x = i + diri[dir][0];y = j + diri[dir][1];
                    if(valid(x, y) && alti[x][y] < tmpalti){
                        tmpalti = alti[x][y];
                        tdir = dir;
                    }
                }
                if(tmpalti < alti[i][j]){
                    map[i][j][tdir] = true;
                    map[i+diri[tdir][0]][j+diri[tdir][1]][3-tdir]=true;
                }
            }
        }
        fillch = 0;
        while((temp = find()) >= 0){
            head = 0;tail = 1;
            q[0] = temp;
            fill[temp / W][temp % W] = fillch;
            while(head < tail){
                temp = q[head++];
                x = temp / W;y = temp % W;
                for(int dir = 0;dir < 4;dir++)
                    if(map[x][y][dir]){
                        nx = x + diri[dir][0];ny = y + diri[dir][1];
                        if(valid(nx, ny) && fill[nx][ny] < 0){
                            fill[nx][ny] = fillch;
                            q[tail++] = nx * W + ny;
                        }
                    }
            }
            fillch++;
        }
        printf("Case #%d:\n", test);
        for(int i = 0;i < H;i++){
            for(int j = 0;j < W;j++){
                if(j) putchar(' ');
                putchar('a' + fill[i][j]);
            }
            puts("");
        }
    }
    return 0;
}
