#include <iostream>
#include <cstring>

using namespace std;

char set_id;
class xy {
    public:
        short x, y;
        char  id;
        xy(short _x = -1, short _y = -1, char _id = -1) {
            x = _x;
            y = _y;
            id = _id;
        }
        bool operator == (const xy &other) const {
            return (x == other.x && y == other.y);
        }
        bool operator != (const xy &other) const {
            return !(*this == other);
        }
        bool is_null() const {
            return (x == -1 && y == -1);
        }
};

short map[100][100];
xy    set[100][100];

xy find(short h, short w) {
    if (set[h][w].is_null() || set[h][w] == xy(w, h)) {
        return set[h][w].is_null()? xy(w,h) : set[h][w];
    } else {
        return set[h][w] = find(set[h][w].y, set[h][w].x);
    }
}
void join(short h1, short w1, short h2, short w2) {
    //~ cout << 'D' << set[h2][w2].is_null() << endl;
         //~ << set_a.x << ',' << set_a.y << ' '
         //~ << set_b.x << ',' << set_b.y << endl;

    set[h1][w1] = find(h2, w2);

    //~ cout << 'd' << set[h1][w1].x << ',' << set[h1][w1].y << endl;
}

int main()
{
    int case_count;
    cin >> case_count;

    short H, W, min;
    char dir;
    char name_set_map[26];

    for (int _c = 0; _c < case_count; ++_c) {

        cin >> H >> W;

        for (short h = 0; h < H; ++h) {
            for (short w = 0; w < W; ++w) {
                cin >> map[h][w];
                set[h][w] = xy();
            }
        }
        set_id = 'a';

        for (short h = 0; h < H; ++h) {
            for (short w = 0; w < W; ++w) {
                dir = 'o'; min = map[h][w];
                if (h - 1 >= 0 && map[h-1][w] < min) {
                    min = map[h-1][w];
                    dir = 'n';
                }
                if (w - 1 >= 0 && map[h][w-1] < min) {
                    min = map[h][w-1];
                    dir = 'w';
                }
                if (w + 1 < W && map[h][w+1] < min) {
                    min = map[h][w+1];
                    dir = 'e';
                }
                if (h + 1 < H && map[h+1][w] < min) {
                    min = map[h+1][w];
                    dir = 's';
                }

                //~ cout << dir << endl;
                switch (dir) {
                    case 'n': join(h, w, h-1, w); break;
                    case 'w': join(h, w, h, w-1); break;
                    case 'e': join(h, w, h, w+1); break;
                    case 's': join(h, w, h+1, w); break;
                    case 'o': set[h][w] = xy(w, h, set_id++); break;
                }
            }
        }

        memset(name_set_map, -1, sizeof(name_set_map));
        char o = 'a';
        cout << "Case #" << _c + 1 << ':' << endl;
        for (short h = 0; h < H; ++h) {
            for (short w = 0; w < W; ++w) {
                if (name_set_map[find(h, w).id - 'a'] == -1) {
                    name_set_map[find(h, w).id - 'a'] = o++;
                }
                cout << name_set_map[find(h, w).id - 'a'];
                if (w < W-1) cout << ' ';
            } cout << endl;
        }
    }
    return 0;
}
