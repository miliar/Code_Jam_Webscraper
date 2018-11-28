#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

int R, C;
char A[32][32];
int portal[32][32][4][2];
int nportal[32][32];

void read_one()
{
    int i, j;

    cin >> R >> C;

    for (i = 1; i <= R; i++) {
        scanf ("%s", A[i] + 1);
        A[i][0] = A[i][C + 1] = '#';
    }
    memset(A[0], '#', 32);
    memset(A[R + 1], '#', 32);
    R ++; C ++;
}

int SX, SY, EX, EY;

int viz[17*17*17*17*17*17];

struct conf {
    int x, y;
    int ax, ay;
    int bx, by;

    int id() {
        return (((((x*17 + y) * 17 + ax) * 17 + ay) * 17 + bx) * 17 + by);
    }
};

int dirs[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

void solve_one()
{
    int i, j, k, l;

    memset (portal, 0, sizeof(portal));
    memset (nportal, 0, sizeof(portal));
    memset (viz, 0, sizeof(viz));

    for (i = 1; i < R; i++)
    for (j = 1; j < C; j++) {
        if (A[i][j] == 'O') {
            SX = i; SY = j;
        }
        if (A[i][j] == 'X') {
            EX = i; EY = j;
        }
        if (A[i][j] != '#') {
            for (k = j; A[i][k] != '#'; k++);
            portal[i][j][0][0] = i;
            portal[i][j][0][1] = k - 1;
            for (k = j; A[i][k] != '#'; k--);
            portal[i][j][1][0] = i;
            portal[i][j][1][1] = k + 1;
            for (k = i; A[k][j] != '#'; k++);
            portal[i][j][2][0] = k - 1;
            portal[i][j][2][1] = j;
            for (k = i; A[k][j] != '#'; k--);
            portal[i][j][3][0] = k + 1;
            portal[i][j][3][1] = j;
        }
    }

    deque<conf> q0;
    conf start;
    start.x = SX; start.y = SY;
    start.ax = start.ay = start.bx = start.by = 0;

    viz[start.id()] = 1;
    q0.push_front(start);
    
    //cerr << "------" << endl;
        for (; ! q0.empty();) {
            conf cur = q0.front(); q0.pop_front();

            //cerr << viz[cur.id()] << " --  " << cur.x << " " << cur.y << "_ " << cur.ax << " " << cur.ay << " __ " << cur.bx <<  " " <<  cur.by << endl;

            if (cur.x == EX && cur.y == EY) {
                cout << viz[cur.id()] - 1;
                return;
            }
            // shoot a portal
            for (k = 0; k < 4; k++) {
                conf nxt = cur;
                nxt.ax = portal[cur.x][cur.y][k][0];
                nxt.ay = portal[cur.x][cur.y][k][1];
                if (viz[nxt.id()] == 0) {
                    viz[nxt.id()] = viz[cur.id()];
                    q0.push_front(nxt);
                }
                nxt = cur;
                nxt.bx = portal[cur.x][cur.y][k][0];
                nxt.by = portal[cur.x][cur.y][k][1];
                if (viz[nxt.id()] == 0) {
                    viz[nxt.id()] = viz[cur.id()];
                    q0.push_front(nxt);
                }
            }
            // move
            for (k = 0; k < 4; k++) {
                conf nxt = cur;
                nxt.x += dirs[k][0]; nxt.y += dirs[k][1];
                if (A[nxt.x][nxt.y] == '#')
                    continue;
                if (viz[nxt.id()] == 0) {
                    viz[nxt.id()] = viz[cur.id()] + 1;
                    q0.push_back(nxt);
                }
            }
            
            // move through portal
            if (cur.x == cur.ax && cur.y == cur.ay && cur.bx) {
                conf nxt = cur;
                nxt.x = nxt.bx;
                nxt.y = nxt.by;
                if (viz[nxt.id()] == 0) {
                    viz[nxt.id()] = viz[cur.id()] + 1;
                    q0.push_back(nxt);
                }
            }
            if (cur.x == cur.bx && cur.y == cur.by && cur.ax) {
                conf nxt =  cur;
                nxt.x = nxt.ax;
                nxt.y = nxt.ay;
                if (viz[nxt.id()] == 0) {
                    viz[nxt.id()] = viz[cur.id()] + 1;
                    q0.push_back(nxt);
                }
            } 
        }

    cout << "THE CAKE IS A LIE";
}

int main(void)
{
    int T, i;

    for(scanf("%d\n", &T), i = 1; i <= T; i++) {
        read_one();
        printf ("Case #%d: ", i);
        solve_one();
        printf ("\n");
    }
}

