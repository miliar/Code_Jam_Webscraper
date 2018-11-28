#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int i, x, y, z;
    int T;
    int N, K;
    char mat_a[100][100];
    char mat_b[100][100];
    int k, xx, yy;
    int dir;
    int dx[] = {0, -1, -1, -1};
    int dy[] = {1,  1, -1,  0};
    bool red, blue;


    cin >> T;

    for(i=1;i<=T;i++) {
        cin >> N >> K;
        for(x=0;x<N;x++) {
            string s;
            cin >> s;
            for(y=0;y<N;y++) {
                mat_b[x][y] = s[y];
            }
        }
        memset(mat_a, '.', sizeof(mat_a));
        for(x=0;x<N;x++) {
            z = 0;
            for(y=N-1;y>=0;y--) {
                if (mat_b[x][y] != '.') {
                    mat_a[N-1-z][N-1-x] = mat_b[x][y];
                    z++;
                }
            }
        }
//          for(x=0;x<N;x++) {
//              for(y=0;y<N;y++) {
//                  cout << mat_a[x][y];
//              }
//              cout << endl;
//          }

         
        red = blue = false;

        for(dir=0;dir<4;dir++) {
            for(x=0;x<N;x++) {
                for(y=0;y<N;y++) {
                    if (mat_a[x][y] == '.')
                        continue;
                    if ((y + dy[dir]*(K-1)) >= N)
                        continue;
                    if ((y + dy[dir]*(K-1)) < 0)
                        continue;
                    if ((x + dx[dir]*(K-1)) >= N)
                        continue;
                    if ((x + dx[dir]*(K-1)) < 0)
                        continue;

                    xx = x - dx[dir];
                    yy = y - dy[dir];

                    if ((0 <= xx  && xx < N) && (0 <= yy  && yy < N)) {
                        if (mat_a[xx][yy] == mat_a[x][y]) {
                            continue;
                        }
                    }
                    
                    xx = x;
                    yy = y;
                    for(k=1;k<K;k++) {
                        xx += dx[dir];
                        yy += dy[dir];
                        if (mat_a[xx][yy] != mat_a[x][y]) {
                            break;
                        }
                        if (k == (K-1)) {
                            xx += dx[dir];
                            yy += dy[dir];
                            if (mat_a[x][y] == 'R') {
                                red = true;
                            } else {
                                blue = true;
                            }
                            //                            cout << x << "," << y << "," << dir << "," << K << endl;
                        }
                    }
                }
            }
        }

        cout << "Case #" << i << ": " << ((blue && red) ? "Both" : (blue) ? "Blue" : (red) ? "Red" : "Neither") << endl;
    }
    
    return 0;
}
