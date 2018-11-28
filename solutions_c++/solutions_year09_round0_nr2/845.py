#include <cstdio>
#include <queue>
using namespace std;
struct cell{
    int x, y;
};
int mat[128][128], n, m, used[128][128], dused[128][128];
int dx[4] = {-1,  0, 0, 1}; 
int dy[4] = {0 , -1, 1, 0};
cell small(int i, int j){
    cell rez;
    rez.x = i; rez.y = j;
    int mn = mat[i][j];
    for ( int k = 0; k < 4; ++k ){
        int ti = i + dx[k], tj= j + dy[k];
        if ( ti < 0 || tj < 0 || tj >= m || ti >= n ) continue;
        if ( mat[ti][tj] <  mn ) { rez.x = ti; rez.y = tj; mn = mat[ti][tj];}
    }
    return rez;
}
cell dfs(int i, int j){
    dused[i][j] = 1;
    cell rez, t;
    rez.x = i; rez.y = j;
    t = small(i, j);
    if ( !dused[t.x][t.y] ) return dfs(t.x, t.y);
    return rez;
}
void bfs(int i, int j, int col){
    cell t;
    queue <cell> q;
    used[i][j] = col;
    t.x = i; t.y = j;
    q.push(t);
    while(!q.empty()){
        t = q.front();
        q.pop();
        i = t.x; j = t.y;
        for ( int k = 0; k < 4; ++k ){
            int ti = i + dx[k], tj = j + dy[k];
            if ( ti < 0 || tj < 0 || tj >= m || ti >= n ) continue;
            if ( used[ti][tj] ) continue;
            t = small(ti, tj);
            if ( t.x == i && t.y == j ) {
                 t.x += dx[k];
                 t.y += dy[k];
                 q.push(t);
                 used[ti][tj] = col; }
        }
    }
}
void workcell(int i, int j, int col){
    for ( int k = 0; k < 128; ++k )
    memset(dused[k], 0, sizeof(dused[k]));
    cell t = dfs(i, j);
    bfs(t.x, t.y, col);
}
void solve(int q){
    for ( int i = 0; i < 128; ++i ) 
        memset(used[i], 0, sizeof(used[i]));
    scanf("%d%d", &n, &m);
    for ( int i = 0; i < n; ++i )
        for ( int j = 0; j < m; ++j )
            scanf("%d", &mat[i][j]);
    int br = 0;
    for ( int i = 0; i < n; ++i )
        for ( int j = 0; j < m; ++j )
            if ( !used[i][j] ) workcell(i,j, ++br);
    printf("Case #%d:\n", q);
    for ( int i = 0; i < n; ++i ){
        for ( int j = 0; j < m; ++j )
            printf("%c ", (char)(used[i][j] + 'a' - 1) );
        printf("\n");
    }
}
int main(){
    int T;
    scanf("%d", &T);
    for ( int i = 0; i < T; ++i )
        solve(i + 1);
}
