#include <cstdio>
#include <algorithm>
#include <vector>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_H = 104;
const int dirX[] = {-1, 0, 0, 1};
const int dirY[] = {0, -1, 1, 0};

int T, H, W;
int data[MAX_H][MAX_H];
char d[MAX_H][MAX_H];

void fun(int cs) {
    scanf("%d %d", &H, &W);
    REP(i, H) REP(j, W) scanf("%d", &data[i][j]);
    REP(i, H) REP(j, W) d[i][j] = '-';

    char cur_base = 'a';
    REP(i, H) REP(j, W) {
        if ( d[i][j] != '-' ) continue;
        
        vector< pair<int, int> > path;
        path.push_back( make_pair(i, j) );

        char base = cur_base;
        while ( true ) {
            int x = path.back().first;
            int y = path.back().second;

            if ( d[x][y] != '-' ) {
                base = d[x][y];
                break;
            }

            int best = data[x][y];
            int bestDir = -1;
            REP(dir, 4) {
                int nx = x + dirX[dir];
                int ny = y + dirY[dir];
                if ( nx < 0 or ny < 0 or nx >= H or ny >= W ) continue;

                if ( data[nx][ny] < best ) {
                    best = data[nx][ny];
                    bestDir = dir;
                }
            }

            if ( bestDir == -1 ) {
                break;
            } else {
                int nx = x + dirX[bestDir];
                int ny = y + dirY[bestDir];

                path.push_back( make_pair(nx, ny) );
            }
        }

        if ( cur_base == base ) cur_base++;
        REP(i, path.size()) {
            d[path[i].first][path[i].second] = base;
        }
    }

    printf("Case #%d:\n", cs);
    REP(i, H) {
        REP(j, W) printf("%c ", d[i][j]);
        printf("\n");
    }
}

int main() {
    scanf("%d", &T);

    REP(i, T) {
        fun(i+1);
    }

    return 0;
}
