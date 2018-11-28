#include <iostream>

using namespace std;

const int NMAX = 1024;
int map[NMAX][NMAX];
int H,W;

bool valid(int row, int col){
    return (row >= 0 && row < H && col >= 0 && col < W);
}

int drow[]={-1,0,0,1};
int dcol[]={0,-1,1,0};

bool was[NMAX][NMAX];
char color[NMAX][NMAX];

bool isMin(int row, int col, int row1, int col1){
    if (map[row1][col1] >= map[row][col])
        return false;
    int best = (1 << 30);
    int best_r=-1,best_c=-1;
    for (int i = 0; i < 4; i++){
        int r = row + drow[i];
        int c = col + dcol[i];
        if (valid(r,c) && map[r][c] < best){
            best = map[r][c];
            best_r = r; best_c = c;            
        }
    }
    return (row1 == best_r && col1 == best_c);
}

void dfs(int row, int col, char ch){
    if (was[row][col])
        return;
    was[row][col] = true;
    color[row][col] = ch;    
    for (int i = 0; i < 4; i++){
        int r = row + drow[i];
        int c = col + dcol[i];
        if (valid(r,c) && isMin(row,col,r,c) || isMin(r,c,row,col)){
            dfs(r,c,ch);
        }
    }    
}

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    int T;
    scanf("%d",&T);
    for (int i = 0; i < T; i++){
        scanf("%d%d",&H,&W);
        for (int r = 0; r < H; r++)
            for (int c = 0; c < W; c++)
                scanf("%d",&map[r][c]);
        memset(was,0,sizeof(was));
        char cur = 'a';
        for (int row = 0; row < H; row++)
            for (int col = 0; col < W; col++){
                if (!was[row][col]){
                    dfs(row,col,cur);
                    cur++;
                }                
            }
        printf("Case #%d:\n",i+1);
        for (int row = 0; row < H; row++){
            for (int col = 0; col < W; col++){
                printf("%c ",color[row][col]);
            }
            printf("\n");
        }
    }

    return 0;
}