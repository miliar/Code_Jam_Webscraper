#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<map>

using namespace std;

int result[(1<<17)][4][4];
int initial;
int r;
int c;
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int dfs (int mask, int kx, int ky){
    //printf("%d %d %d\n", mask, kx, ky);
    if (result[mask][kx][ky] != -1) return result[mask][kx][ky];
    int resp = 1;
    int i;
    int x, y;
    for (i=0; i<8; i++) {
        x = kx + dx[i];
        y = ky + dy[i];
        if (x < 0 || x >= r) continue;
        if (y < 0 || y >= c) continue;
        if ((mask & (1<<(x*4+y))) != 0) continue;
        if (dfs((mask | (1<<(x*4+y))), x, y) == 1) resp = 0;
    }
    result[mask][kx][ky] = resp;
    return resp;
}

int main(){
    int teste;
    int n;
    int i, j, k;
    int kx, ky;
    char leitor[1000];
    scanf("%d", &n);
    for (teste=0;teste<n;teste++) {
        initial = 0;
        for (i=0; i<(1<<17); i++) {
            for (j=0; j<4; j++) {
                for (k=0; k<4; k++) {
                    result[i][j][k] = -1;
                }
            }
        }
        scanf("%d %d", &r, &c);
        for (i=0; i<r; i++){
            scanf("%s", leitor);
            for (j=0; j<c; j++) {
                if (leitor[j] == 'K') {
                    kx = i;
                    ky = j;
                    initial = initial | (1<<(i*4+j));
                }
                else if (leitor[j] == '#'){
                    initial = initial | (1<<(i*4+j));
                }
            }
        }
        if (dfs(initial, kx, ky) == 0) {        
            printf("Case #%d: A\n", teste+1);
        } else {
            printf("Case #%d: B\n", teste+1);            
        }
    }
    return 0;
}
