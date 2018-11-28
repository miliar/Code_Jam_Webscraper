#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int G[110][110];
char T[110][110];
char R[110][110];

struct Path {
    int x, y;
    char c;
    Path(int x, int y, char c) : x(x), y(y), c(c) {}
};

int main() {
    int t, tt=0, h, w;
    cin >> t;


    while(tt++<t) {
        cin >> h >> w;
        memset(R, 0, sizeof(R));

        for(int i=0; i<h; i++)
            for(int j=0; j<w; j++)
                cin >> G[i][j];

        for(int i=0; i<h; i++) {
            for(int j=0; j<w; j++) {
                int minn = G[i][j];
                char dir = '0';
                if (i>0 && G[i-1][j] < minn) {
                    minn = G[i-1][j]; dir = 'N';
                }

                if (j>0 && G[i][j-1] < minn) {
                    minn = G[i][j-1]; dir = 'W';
                }

                if (j<w-1 && G[i][j+1] < minn) {
                    minn = G[i][j+1]; dir = 'E';
                }

                if (i<h-1 && G[i+1][j] < minn) {
                    minn = G[i+1][j]; dir = 'S';
                }

                T[i][j] = dir;

              // cout << T[i][j];
            }
           // cout << endl;
        }

        char current = 'A';
        queue<Path> q;
        for(int i=0; i<h; i++) {
            for(int j=0;j<w;j++) {
                if (T[i][j]=='0')
                    q.push(Path(i,j,current++));

                while(!q.empty()) {
                    Path p = q.front(); q.pop();
                    //cout << p.x << " " << p.y << " " << p.c << endl;

                    if (R[p.x][p.y]) continue;

                    R[p.x][p.y] = p.c;

                    if (p.x > 0 && T[p.x-1][p.y] == 'S')
                        q.push(Path(p.x-1, p.y, p.c));
                    if (p.x < h-1 && T[p.x+1][p.y] == 'N')
                        q.push(Path(p.x+1, p.y, p.c));
                    if (p.y > 0 && T[p.x][p.y-1] == 'E')
                        q.push(Path(p.x, p.y-1, p.c));
                    if (p.y < w-1 && T[p.x][p.y+1] == 'W')
                        q.push(Path(p.x, p.y+1, p.c));
                }
            }
        }

        current = 'a';
        char working;
        for(int i=0; i<h; i++) {
            for(int j=0;j<w;j++) {
                if (R[i][j]>='A' && R[i][j]<='Z')
                    q.push(Path(i,j,current++));
                working = R[i][j];

                 while(!q.empty()) {
                    Path p = q.front(); q.pop();
                    //cout << p.x << " " << p.y << " " << p.c << endl;

                    if (R[p.x][p.y]>='a' && R[p.x][p.y]<='z') continue;

                    R[p.x][p.y] = p.c;

                    if (p.x > 0 && R[p.x-1][p.y] == working)
                        q.push(Path(p.x-1, p.y, p.c));
                    if (p.x < h-1 && R[p.x+1][p.y] == working)
                        q.push(Path(p.x+1, p.y, p.c));
                    if (p.y > 0 && R[p.x][p.y-1] == working)
                        q.push(Path(p.x, p.y-1, p.c));
                    if (p.y < w-1 && R[p.x][p.y+1] == working)
                        q.push(Path(p.x, p.y+1, p.c));
                }

            }
        }

        cout << "Case #" << tt << ":" << endl;
         for(int i=0; i<h; i++) {
            for(int j=0;j<w;j++) {
                cout << (j>0?" ":"") << R[i][j];
            }
            cout << endl;
         }

    }
}
