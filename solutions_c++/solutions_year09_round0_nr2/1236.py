#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

#define SENT 12321

int T, H, W, map[102][102], basins[102][102], G[102][102];
int di[] = {-1, 0, 0, 1}, dj[] = {0, -1, 1, 0};

void dfs(int i, int j, int ind)
{
    basins[i][j] = ind;
    for(int k = 0; k < 4; k++){
        if(((G[i][j] >> k) & 1) && !basins[i + di[k]][j + dj[k]]){
            dfs(i + di[k], j + dj[k], ind);
        }
    }
}

void get()
{
    memset(G, 0, sizeof(G));
    memset(basins, 0, sizeof(basins));
    for(int i = 1; i <= H; i++){
        for(int j = 1; j <= W; j++){
            int best = SENT, ind;
            for(int k = 0; k < 4; k++){
                if(best > map[i + di[k]][j + dj[k]]){
                    best = map[i + di[k]][j + dj[k]];
                    ind = k;
                }
            }
            if(best < map[i][j]){
                G[i][j] |= (1 << ind);
                G[i + di[ind]][j + dj[ind]] |= (1 << (3 - ind));
            }
        }
    }
    int ind = 1;
    for(int i = 1; i <= H; i++){
        for(int j = 1; j <= W; j++){
            if(!basins[i][j]){
                dfs(i, j, ind++);
            }
        }
    }
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    fin >> T;
    for(int test = 1; test <= T; test++){
        fin >> H >> W;
        for(int i = 0; i <= H + 1; i++){
            for(int j = 0; j <= W + 1; j++){
                if(i && i <= H && j && j <= W){
                    fin >> map[i][j];
                }
                else{
                    map[i][j] = SENT;
                }
            }
        }
        get();
        fout << "Case #" << test << ":" << endl;
        for(int i = 1; i <= H; i++){
            for(int j = 1; j <= W; j++){
                fout << (char)(basins[i][j] + 'a' - 1) << (j == W ? "" : " ");
            }
            fout << endl;
        }
    }
}
