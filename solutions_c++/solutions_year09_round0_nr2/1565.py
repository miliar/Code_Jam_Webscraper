#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define INF 1000000
#define FOR(A, B, C) for(int A = (int)B; A < (int)C; A++)

int rows, cols;
int mapa[110][110];
int basin[110][110];

const int dr[] = {-1, 0, 0, 1};
const int dc[] = {0, -1, 1, 0};

bool valid(int r, int c)
{
    return (r >= 0 && c >= 0 && r < rows && c < cols);
}

int fillbasin(int row, int col, int c)
{
    int low = INF;
    int cc, rr;

    if(basin[row][col] != -1)
        return basin[row][col];
    
    FOR(i, 0, 4){
        int nr = row + dr[i], nc = col + dc[i];
        if(valid(nr, nc)){
            if(mapa[nr][nc] < mapa[row][col] && mapa[nr][nc] < low){
                low = mapa[nr][nc];
                rr = nr;
                cc = nc;
            }
        }
    }


    if(low == INF){
        return (basin[row][col] = c);
    }

    return (basin[row][col] = fillbasin(rr, cc, c));

}

int main()
{
    int t;
    scanf("%d", &t);
    for(int caso = 0; caso < t; caso++){
        scanf("%d %d", &rows, &cols);
        memset(basin, -1, sizeof(basin));
        FOR(i, 0, rows)
            FOR(j, 0, cols){
                scanf("%d", &mapa[i][j]);
            }
        int b = 0;
        FOR(i, 0, rows)
            FOR(j, 0, cols)
                if(basin[i][j] == -1)
                    if(fillbasin(i, j, b) == b) b++;
        
        int hash[1000];
        memset(hash, 0, sizeof(hash));
        int lbl = -1;
        FOR(i, 0, rows)
            FOR(j, 0, cols)
                if(basin[i][j] >= 0){
                    if(hash[basin[i][j]] == 0)
                        hash[basin[i][j]] = lbl--;
                    //relabel(i, j, hash[basin[i][j]]);
                    basin[i][j] = hash[basin[i][j]];
                }

        printf("Case #%d:\n", caso + 1);
        FOR(i, 0, rows){
            FOR(j, 0, cols){
                if(j > 0) printf(" ");
                printf("%c", ('a' - 1) + -1*(basin[i][j]));
            }
            printf("\n");
        }       
    }
    return 0;
}

