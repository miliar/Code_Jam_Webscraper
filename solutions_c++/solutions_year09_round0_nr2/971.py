#include <stdio.h>
#include <algorithm>
#include <stdlib.h>

using namespace std;

const int max_size = 100 + 10;
const int max_int = 0x7fffffff;
const int dist[4][2] = {{-1,0}, {0,-1}, {0,1}, {1,0}};

int data[max_size][max_size];
int maze[max_size][max_size];
int w, h;
int cur;

int dfs(int, int);

int main(){
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int nCase;
    
    scanf("%d", &nCase); 
    
    for (int t=1; t<=nCase; t++){
        printf("Case #%d:\n", t);
        
        scanf("%d%d", &w, &h);
        
        for (int i=0; i<w; i++)
            for (int j=0; j<h; j++)
                scanf("%d", &data[i][j]);
        
        memset(maze, -1, sizeof(maze));
        cur = 0;
        
        for (int i=0; i<w; i++)                
            for (int j=0; j<h; j++)
                if (maze[i][j] == -1) maze[i][j] = dfs(i, j);
                
        for (int i=0; i<w; i++){
            for (int j=0; j+1 < h; j++)
                printf("%c ", maze[i][j] + 'a');
            printf("%c\n", maze[i][h - 1] + 'a');
        }
    }
    
    return 0;
}

int dfs(int x, int y){
    
    if (maze[x][y] != -1) return maze[x][y];
   /* printf("%d %d\n", x, y);
    system("pause");*/
    int low = max_int, low_pos = -1;
    for (int i=0; i<4; i++){
        int t_x = dist[i][0] + x, t_y = dist[i][1] + y;
        
        if (t_x >=0 && t_x < w && t_y >=0 && t_y < h)
            if (low > data[t_x][t_y]){
                low = data[t_x][t_y];
                low_pos = i;
            }
    }
    
    if (low >= data[x][y]){
        if (maze[x][y] == -1){
            maze[x][y] = cur;
            cur++;
        }
        
       // printf("%d %d %d %d\n", x, y, maze[x][y], cur);
     /*   for (int i=0; i<w; i++){
            for (int j=0; j+1 < h; j++)
                printf("%c ", maze[i][j] + 'a');
            printf("%c\n", maze[i][h - 1] + 'a');
        }
        system("pause");*/
        return maze[x][y];
    }
    else{
        maze[x][y] = dfs(x + dist[low_pos][0], y + dist[low_pos][1]);
      /*  printf("----- %d %d %d %d\n", x, y, maze[x][y], maze[x + dist[low_pos][0]][y + dist[low_pos][1]]);
        for (int i=0; i<w; i++){
            for (int j=0; j+1 < h; j++)
                printf("%c ", maze[i][j] + 'a');
            printf("%c\n", maze[i][h - 1] + 'a');
        }
        
        system("pause");*/
        return maze[x][y];
    }
}
