#include <iostream>
#include <fstream>
#include <array>
#include <utility>

using namespace std;

typedef std::array<char, 16> ttt;

enum result { NONE, XWIN, OWIN };

#define I(x,y) ((y)*4+(x))

char getmove(const ttt& arr, int x, int y) {
    if (x < 0 || x > 3 || y < 0 || y > 3) return '?';
    return arr[I(x,y)];
}

result checkline(const ttt& arr, int x, int y, int dx, int dy) {
    char cur = 0;
    int left = 0;

    while (cur != '?') {
        char c = getmove(arr, x, y);
        if (!cur && c == 'T') {
            cur = 'T';
        } else if (cur != c && c != 'T') {
            left = (cur == 'T' ? 2 : 3); cur = c;
        }
        else {
            left--;
        }
        if (left == 0 && (cur == 'X' || cur == 'O')) {
            return cur == 'X' ? XWIN : OWIN;
        }
        x += dx; y += dy;
    }

    return NONE;
}

struct line { int x, y, dx, dy; };

int main(int argc, char **argv) {
    if (argc < 2) {
        cout << "Expected argument\n";
        exit(1);
    }

    ifstream file(argv[1]);
    int ncases;
    file >> ncases;
    for (int i = 0; i < ncases; i++) {
        int j = 0;
        bool draw = true;
        cout << "Case #" << i + 1 << ": ";
        ttt game; 
        while (j < 16) {
            char move;
            file >> move;
            if (move == '.') draw = false;
            if (move == '\n' || move == '\r') continue;
            game[j++] = move;
        }

        // Check rows
        line lines[] = {
            { 0, 0, 1, 0 },
            { 0, 1, 1, 0 },
            { 0, 2, 1, 0 },
            { 0, 3, 1, 0 },
            { 0, 0, 0, 1 },
            { 1, 0, 0, 1 },
            { 2, 0, 0, 1 },
            { 3, 0, 0, 1 },
            { 4, 0, 0, 1 },
            { 0, 0, 1, 1 },
            { 1, 0, 1, 1 },
            { 0, 1, 1, 1 },
            { 0, 3, 1, -1 },
            { 0, 2, 1, -1 },
            { 1, 3, 1, -1 }
        };
        for (line l : lines) {
            result r = checkline(game, l.x, l.y, l.dx, l.dy);
            if (r == XWIN) {
                cout << "X won";
                goto won;
            } else if (r == OWIN) {
                cout << "O won";
                goto won;
            }
        }

        if (draw) {
            cout << "Draw";
        } else {
            cout << "Game has not completed";
        }
won:
        std::cout << "\n";
    }
}
