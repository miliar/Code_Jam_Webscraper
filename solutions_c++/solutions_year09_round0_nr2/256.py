#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

struct Item {
    int altitude;
    int destination;
};

int Sink(vector< Item >& map, int cell)
{
    if (map[cell].destination != cell) {
        return map[cell].destination = Sink(map, map[cell].destination);
    } else {
        return cell;
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int H, W;
        cin >> H >> W;
        vector< Item > map(H * W);
        queue< int > active;
        for (int j = 0; j < H * W; ++j) {
            cin >> map[j].altitude;
            map[j].destination = j;
            active.push(j);
        }
        while (!active.empty()) {
            int cell = active.front();
            active.pop();
            int x = cell % W, y = cell / W, out = cell;
            if (y >= 1 && map[cell - W].altitude < map[out].altitude) {
                out = cell - W;
            }
            if (x >= 1 && map[cell - 1].altitude < map[out].altitude) {
                out = cell - 1;
            }
            if (x <= W - 2 && map[cell + 1].altitude < map[out].altitude) {
                out = cell + 1;
            }
            if (y <= H - 2 && map[cell + W].altitude < map[out].altitude) {
                out = cell + W;
            }
            if (out != cell) {
                map[cell].destination = Sink(map, out);
            }
        }
        cout << "Case #" << i + 1 << ":\n";
        std::map< int, char > sofar;
        char ch = 'a';
        for (int y = 0; y < H; ++y) {
            for (int x = 0; x < W; ++x) {
                int sink = Sink(map, y * W + x);
                std::map< int, char >::iterator it = sofar.find(sink);
                char tag;
                if (it == sofar.end()) {
                    tag = sofar[sink] = ch++;
                } else {
                    tag = it->second;
                }
                cout << tag;
                if (x != W - 1) {
                    cout << " ";
                } else {
                    cout << "\n";
                }
            }
        }
    }
}

