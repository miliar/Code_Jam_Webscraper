#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

enum Direction {
    NONE, NORTH, WEST, EAST, SOUTH
};

struct Land {
    size_t altitude;
    enum Direction direction;
};

bool operator<(const Land &a, const Land &b) {
    if (a.altitude == b.altitude)
        return a.direction < b.direction;
    return a.altitude < b.altitude;
}

void dfs_mark(const vector< vector<Land> > &map, const size_t &H, const size_t &W, const size_t &i, const size_t &j, const char &mark, vector< vector<char> > &answer) {
    if (i != 0 && map[i - 1][j].direction == SOUTH) {
        answer[i - 1][j] = mark;
        dfs_mark(map, H, W, i - 1, j, mark, answer);
    }
    if (j != 0 && map[i][j - 1].direction == EAST) {
        answer[i][j - 1] = mark;
        dfs_mark(map, H, W, i, j - 1, mark, answer);
    }
    if (i != H - 1 && map[i + 1][j].direction == NORTH) {
        answer[i + 1][j] = mark;
        dfs_mark(map, H, W, i + 1, j, mark, answer);
    }
    if (j != W - 1 && map[i][j + 1].direction == WEST) {
        answer[i][j + 1] = mark;
        dfs_mark(map, H, W, i, j + 1, mark, answer);
    }
}

int main() {
    size_t T;
    cin >> T;
    for (size_t cases = 1; cases <= T; ++cases) {
        size_t H, W;
        cin >> H >> W;
        vector< vector<Land> > map(H, vector<Land>(W));
        for (size_t i = 0; i < H; ++i) {
            for (size_t j = 0; j < W; ++j) {
                cin >> map[i][j].altitude;
            }
        }
        for (size_t i = 0; i < H; ++i) {
            for (size_t j = 0; j < W; ++j) {
                vector<Land> judge;
                Land none = {map[i][j].altitude, NONE};
                judge.push_back(none);
                if (i != 0) {
                    Land north = {map[i - 1][j].altitude, NORTH};
                    judge.push_back(north);
                }
                if (j != 0) {
                    Land east = {map[i][j - 1].altitude, WEST};
                    judge.push_back(east);
                }
                if (i != H - 1) {
                    Land south = {map[i + 1][j].altitude, SOUTH};
                    judge.push_back(south);
                }
                if (j != W - 1) {
                    Land west = {map[i][j + 1].altitude, EAST};
                    judge.push_back(west);
                }
                sort(judge.begin(), judge.end());
                map[i][j].direction = judge.front().direction;
            }
        }
        vector< vector<char> > answer(H, vector<char>(W));
        char mark = 'a';
        for (size_t i = 0; i < H; ++i) {
            for (size_t j = 0; j < W; ++j) {
                if (answer[i][j] != '\0')
                    continue;
                size_t root_i = i, root_j = j;
                while (map[root_i][root_j].direction != NONE) {
                    switch (map[root_i][root_j].direction) {
                        case NORTH:
                            --root_i;
                            break;
                        case WEST:
                            --root_j;
                            break;
                        case EAST:
                            ++root_j;
                            break;
                        case SOUTH:
                            ++root_i;
                            break;
                    }
                }
                answer[root_i][root_j] = mark;
                dfs_mark(map, H, W, root_i, root_j, mark, answer);
                ++mark;
            }
        }
        cout << "Case #" << cases << ": " << endl;
        for (size_t i = 0; i < H; ++i) {
            for (size_t j = 0; j < W; ++j) {
                if (j != 0)
                    cout << ' ';
                cout << answer[i][j];
            }
            cout << endl;
        }
    }
}
