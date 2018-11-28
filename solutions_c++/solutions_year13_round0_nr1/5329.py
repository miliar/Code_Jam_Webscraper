    #include <cstdio>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, casen = 0, x, y;
    char grid[5][5], vencedor,acabou;
    scanf("%d", &t);
    while (casen < t) {
        acabou = 1;
        for (x = 0; x < 4; x++) {
            scanf("%s", grid[x]);
            for (y = 0; y < 4; y++) if (grid[x][y] == '.') {
                acabou = 0;
                break;
            }
        }
        for (x = 0; x < 4; x++) {
            vencedor = 0;
            if (grid[x][0] != '.') {
                if (grid[x][0] == 'T' && grid[x][1] != '.') {
                    vencedor = grid[x][1];
for (y = 2; y < 4; y++) if (grid[x][y] != grid[x][1]) break;
                } else {
                    vencedor = grid[x][0];
                    for (y = 1; y < 4; y++) if (grid[x][y] != grid[x][0] && grid[x][y] != 'T') break;
                }
                if (y == 4) {
                    //printf("A ");
                    break;
                }
            }
            vencedor = 0;
            if (grid[0][x] != '.') {
                if (grid[0][x] == 'T' && grid[1][x] != '.') {
                    vencedor = grid[1][x];
for (y = 2; y < 4; y++) if (grid[y][x] != grid[1][x]) break;
                } else {
                    vencedor = grid[0][x];
                    for (y = 1; y < 4; y++) if (grid[y][x] != grid[0][x] && grid[y][x] != 'T') break;
                }
                if (y == 4) {
                    //printf("B ");
                    break;
                }
                vencedor = 0;
            }
        }
        if (!vencedor) {
                        if (grid[0][0] != '.') {
                if (grid[0][0] == 'T') {
                    if (grid[1][1] != '.') {
                    //printf("1 ");
                    vencedor = grid[1][1];
for (y = 2; y < 4; y++) if (grid[y][y] != grid[1][1]) break;
                    }
                } else {
                    //printf("2 ");
                    vencedor = grid[0][0];
                    for (y = 1; y < 4; y++) if (grid[y][y] != grid[0][0] && grid[y][y] != 'T') break;
                }
                if (y < 4) vencedor = 0;
                //else printf("C ");
            }
        }
        if (!vencedor) {
                        if (grid[3][0] != '.') {
                if (grid[3][0] == 'T') {
                    if (grid[2][1] != '.') {
                    vencedor = grid[2][1];
for (y = 2; y < 4; y++) if (grid[3-y][y] != grid[2][1]) break;
                }
                } else {
                    vencedor = grid[3][0];
                    for (y = 1; y < 4; y++) if (grid[3-y][y] != grid[3][0] && grid[3-y][y] != 'T') break;
                }
                if (y < 4) vencedor = 0;
                //else printf("D ");
            }
        }
        if (vencedor) {
            printf("Case #%d: %c won\n", ++casen, vencedor);
        } else printf("Case #%d: %s\n",++casen, acabou? "Draw": "Game has not completed");
    }
    return 0;
}

