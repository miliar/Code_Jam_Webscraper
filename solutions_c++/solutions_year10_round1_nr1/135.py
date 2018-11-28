#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <numeric>
#include <cctype>
#include <list>
#include <functional>
#include <stack>
#include <fstream>
#include <sstream>
#include <cstring>
#include <cstdlib>

#define size(c) (int)c.size()
using namespace std;

typedef pair<int, int> edge;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef map<string, int> msi;
typedef pair<int, int> pii;

string board[100];
int N, K, T;
int dx[] = {0, 1, 1, 1};
int dy[] = {1, 0, -1, 1};
bool valid (int x, int y) {
    return  x >= 0 && x < N && y >= 0 && y < N;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    int cases = 0;
    while(T--) {
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; ++ i)
            cin >> board[i];
        for (int i = 0; i < N; ++ i) {
            int end = N - 1;
            for (int j = N - 1; j >= 0; j --) {
                if (board[i][j] != '.') {
                    swap(board[i][j], board[i][end]);
                    end --;
                }
            }
        }
//        for (int i = 0; i < N; ++ i)
//            cout << board[i] << endl;
        bool ok[2] = {false}; ok[1] = ok[0] = false;
        for (int i = 0; i < N; ++ i) {
            for (int j = 0; j < N; ++ j) {
                if (board[i][j] != '.') {
                    for (int d = 0; d < 4; ++ d) {
                        int ex = i + (K - 1) * dx[d];
                        int ey = j + (K - 1) * dy[d];
                        if (valid(ex, ey)) {
                            bool flag = true;
                            for (int t = 0; t < K; ++ t) {
                                int nx = i + t * dx[d];
                                int ny = j + t * dy[d];
                                if (board[nx][ny] != board[i][j]) flag = false;
                            }
                            if (flag) ok[board[i][j] == 'R'] = true;
                        }
                    }
                }
            }
        }
        cout << "Case #" << ++ cases << ": ";
        if (ok[1] && !ok[0]) cout << "Red" << endl;
        if (!ok[1] && ok[0]) cout << "Blue" << endl;
        if (ok[1] && ok[0]) cout << "Both" << endl;
        if (!ok[1] && !ok[0]) cout << "Neither" << endl;
    }
    return 0;
}
