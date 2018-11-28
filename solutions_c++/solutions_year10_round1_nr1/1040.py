#include <iostream>
#include <cstring>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
using namespace std;

int T;

class Game {
public:
    int N, K;
    char board[50 + 2][50 + 2]; // including sentry.
    Game() {
        N = K = 0;
        memset(board, 0, sizeof(board));
    }
    void getProblem() {
        cin >> N >> K;
        REP(i, N) {
            cin >> &(board[i+1][1]);
        }
        REP(i, N+2) { board[0][i] = '*'; }
        REP(i, N+2) { board[N + 1][i] = '*'; }
        REP(i, N+2) { board[i][0] = '*'; }
        REP(i, N+2) { board[i][N + 1] = '*'; }
    }
    void dump() {
        cout << N << ':' << K << endl;
        REP(i, N + 2) {
            REP(j, N + 2) {
                cout << board[i][j];
            }
            cout << endl;
        }
    }
    void rotate() {
        for (int i = N-1 + 1; i >= 0 + 1; i--) {
            for (int j = N-1 + 1; j >= 0 + 1; j--) {
                if (board[i][j] == '.') {
                    bool flag = false;
                    for (int k = j-1; k > 0; k--) {
                        if (board[i][k] != '.') {
                            board[i][j] = board[i][k];
                            board[i][k] = '.';
                            flag = true;
                            break;
                        }
                    }
                    if (!flag) { break; }
                }
            }
        }
    }
};

const int dx[8] = { 0,  1,  0, -1,  1,  1, -1, -1};
const int dy[8] = { 1,  0, -1,  0,  1, -1,  1, -1};

class Solver {
private:
public:
    Game *g;
    Solver() { g = NULL; }
    void setGame(Game *game) {
        g = game;
    }
    bool subSearch(int x, int y, int dir, char color) {
        REP(i, (g->K)) {
            if (y + (i*dy[dir]) > g->N || y + (i*dy[dir]) < 1) {
                return false;
            }
            if (x + (i*dx[dir]) > g->N || x + (i*dx[dir]) < 1) {
                return false;
            }
            if (g->board[y + (i*dy[dir])][x + (i*dx[dir])] != color) {
                return false;
            }
        }
        return true;
    }
    bool search(const char color) {
        for (int i = 1; i < g->N + 1; i++) {
            for (int j = 1; j < g->N + 1; j++) {
                //cout << color << endl;
                if (g->board[i][j] == color) {
                    REP(k, 8) {
                        if (subSearch(j, i, k, color)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
};

int main(void) {
    cin >> T;
    getchar();
    REP(i, T) {
        Game g;
        Solver s;
        g.getProblem();
        //g.dump();
        g.rotate();
        //g.dump();
        s.setGame(&g);
        bool bf, rf;
        cout << "Case #" << i + 1 << ": ";
        bf = s.search('B');
        rf = s.search('R');
        if (bf && rf) { cout << "Both" << endl; }
        else if (bf)  { cout << "Blue" << endl; }
        else if (rf)  { cout << "Red" << endl; }
        else          { cout << "Neither" << endl; }
    }
    return 0;
}
