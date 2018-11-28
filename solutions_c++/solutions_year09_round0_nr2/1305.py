#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int main()
{
    int T;
    cin >> T;
    cin.get();

    int dx[] = {-1, 0, 0, 1};
    int dy[] = {0, -1, 1, 0};

    char ret[100][100][100];
    int heights[100];
    int widths[100];
    memset(ret, 0, sizeof(ret));
    for (int n = 0; n < T; n++) {
        int H, W;
        cin >> H >> W;
        cin.get();
        heights[n] = H;
        widths[n] = W;

        int M[100][100];
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++)
                cin >> M[i][j];
            cin.get();
        }

        vector< pair<int, int> > D[100][100];  // dependencies
        pair <int, int> P[100][100];
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++) {
                int lowest = 10000, neighbor = -1;
                for (int k = 0; k < 4; k++) {
                    int x = i + dx[k];
                    int y = j + dy[k];
                    if (x >= 0 && x < H && y >= 0 && y < W && M[x][y] < lowest) {
                        lowest = M[x][y];
                        neighbor = k;
                    }
                }
                if (lowest < M[i][j]) {
                    int x = i + dx[neighbor];
                    int y = j + dy[neighbor];
                    D[x][y].push_back(make_pair(i, j));
                    P[i][j] = make_pair(x, y);
                } else {
                    P[i][j] = make_pair(-1, -1);
                }
            }

        char basin = 'a';
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++) if (! ret[n][i][j]) {
                int tx = i, ty = j;
                while (P[tx][ty].first != -1) {
                    pair<int, int> parent = P[tx][ty];
                    tx = parent.first;
                    ty = parent.second;
                }
                queue < pair<int, int> > Q;
                Q.push(make_pair(tx, ty));
                ret[n][tx][ty] = basin;

                while (! Q.empty()) {
                    int cx = Q.front().first;
                    int cy = Q.front().second;
                    Q.pop();

                    for (int k = 0; k < D[cx][cy].size(); k++) {
                        int nx = D[cx][cy][k].first;
                        int ny = D[cx][cy][k].second;
                        if (! ret[n][nx][ny]) {
                            ret[n][nx][ny] = basin;
                            Q.push(make_pair(nx, ny));
                        }
                    }
                }

                basin++;
            }
    }

    for (int n = 0; n < T; n++) {
        cout << "Case #" << n+1 << ":" << endl;
        for (int i = 0; i < heights[n]; i++) {
            for (int j = 0; j < widths[n]; j++) {
                cout << ret[n][i][j];
                if (j+1 == widths[n]) cout << endl;
                else cout << ' ';
            }
        }
    }
}
