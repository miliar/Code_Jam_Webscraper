#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef double TYPE;
const TYPE EPS = 1e-9, INF = 1e9;

inline int sgn(TYPE a) { return a > EPS ? 1 : (a < -EPS ? -1 : 0); }
inline int cmp(TYPE a, TYPE b) { return sgn(a - b); }

int K;
int di[4] = {1, 0, 1, 1};
int dj[4] = {0, 1, 1, -1};
bool check(vector<string>& board, char c) {
    for(int i = 0; i < board.size(); i++)
        for(int j = 0; j < board[0].size(); j++)
            for(int d = 0; d < 4; d++) {
                bool ok = true;

                int ci = i, cj = j;
                for(int k = 0; k < K; k++) {
                    if(ci < 0 || cj < 0 || ci >= board.size() || cj >= board[0].size() ||
                       board[ci][cj] != c) {
                        ok = false;
                        break;
                    }

                    ci += di[d];
                    cj += dj[d];
                }

                if(ok)
                    return true;
            }

    return false;
}

int main() {
    int t;
    cin >> t;

    for(int z = 0; z < t; z++) {
        int n;
        cin >> n >> K;

        vector<string> old_board(n), new_board(n, string(n, ' '));
        for(int i = 0; i < n; i++)
            cin >> old_board[i];

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                new_board[j][n-1-i] = old_board[i][j];

        for(int j = 0; j < n; j++) {
            int cnt = n - 1;
            for(int i = n - 1; i >= 0; i--)
                if(new_board[i][j] != '.') {
                    new_board[cnt][j] = new_board[i][j];
                    cnt--;
                }

            while(cnt >= 0)
                new_board[cnt--][j] = '.';
        }

        bool red = check(new_board, 'R');
        bool blue = check(new_board, 'B');

        cout << "Case #" << z + 1 << ": ";
        if(red && blue) cout << "Both";
        else if(red) cout << "Red";
        else if(blue) cout << "Blue";
        else cout << "Neither";
        cout << endl;
    }
}
