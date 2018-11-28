/* 2009 Google Code Jam Qualification Round
 * Problem B: Watersheds
 *
 * Coded by Lapro
 * Sep. 3, 2009
 */

#include <iostream>
using namespace std;
const int maxMat = 110;
const int dr[4] = {-1, 0, 0, 1};
const int dc[4] = {0, -1, 1, 0};
int R, C, mat[maxMat][maxMat];
pair<int, int> concate[maxMat][maxMat];
char color[maxMat][maxMat];

bool inside(int r, int c){
    return r < R && r >= 0 && c < C && c >= 0;
}

pair<int, int> dowith(int r, int c){
    if (concate[r][c].first == -1){
        int curdepth = mat[r][c], curr = r, curc = c;
        for(int i = 0; i < 4; ++ i){
            if (inside(r + dr[i], c + dc[i]) && mat[r + dr[i]][c + dc[i]] < curdepth){
                curdepth = mat[r + dr[i]][c + dc[i]];
                curr = r + dr[i];
                curc = c + dc[i];
            }
        }
        if (curr != r || curc != c)
            concate[r][c] = dowith(curr, curc);
        else concate[r][c] = make_pair(r, c);
    }
    return concate[r][c];
}
void calc(){
    cin >> R >> C;
    for(int i = 0; i < R; ++ i)
        for(int j = 0; j < C; ++ j)
            cin >> mat[i][j];
    memset(concate, -1, sizeof(concate));
    memset(color, 0, sizeof(color));
    char nextcolor = 'a';
    for(int i = 0; i < R; ++ i){
        for(int j = 0; j < C; ++ j){
            concate[i][j] = dowith(i, j);
            if (color[concate[i][j].first][concate[i][j].second] == 0)
                color[concate[i][j].first][concate[i][j].second] = nextcolor++;
            color[i][j] = color[concate[i][j].first][concate[i][j].second];
            if (j) cout << ' ' << color[i][j];
            else cout << color[i][j];
        }
        cout << endl;
    }
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w+", stdout);
    int N;
    cin >> N;
    for(int i = 1; i <= N; ++ i){
        printf("Case #%d:\n", i);
        calc();
    }
    return 0;
}
