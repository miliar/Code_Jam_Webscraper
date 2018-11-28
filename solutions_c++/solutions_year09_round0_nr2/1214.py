#include <iostream>

using namespace std;

const int H_MAX = 128, W_MAX = 128;

struct cell {
    char code;
    int altitude;
    cell *sink;
};

cell map[H_MAX][W_MAX];
char current_code;

char code_of (cell *c) {
    if (!c->code) {
        if (c->sink == c)
            c->code = current_code++;
        else
            c->code = code_of(c->sink);
    }
    return c->code;
}

int main (int argc, char const* argv[]) {
    int set, sets_no, h, w, r, c;
    cell *current;
    cin >> sets_no;
    for (set = 0; set < sets_no; set++) {
        current_code = 'a';
        cin >> h >> w;
        for (r = 0; r < h; r++) {
            for (c = 0; c < w; c++) {
                current = &map[r][c];
                cin >> current->altitude;
                current->code = '\0';
                current->sink = current;
            }
        }
        for (r = 0; r < h; r++) {
            for (c = 0; c < w; c++) {
                current = &map[r][c];
                if (r > 0 && map[r-1][c].altitude < current->sink->altitude)
                    current->sink = &map[r-1][c];
                if (c > 0 && map[r][c-1].altitude < current->sink->altitude)
                    current->sink = &map[r][c-1];
                if (c < w-1 && map[r][c+1].altitude < current->sink->altitude)
                    current->sink = &map[r][c+1];
                if (r < h-1 && map[r+1][c].altitude < current->sink->altitude)
                    current->sink = &map[r+1][c];
            }
        }
        cout << "Case #" << set + 1 << ":\n";
        for (r = 0; r < h; r++)
            for (c = 0; c < w; c++)
                cout << code_of(&map[r][c]) << (c < w-1 ? ' ' : '\n');
    }
}

