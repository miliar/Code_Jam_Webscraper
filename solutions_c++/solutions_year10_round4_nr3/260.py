#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int caseno=1; caseno<=cases; caseno++) {
        char b[330][330];
        char b2[330][330];
        
        for (int y=0; y<330; y++)
        for (int x=0; x<330; x++) {
            b[y][x] = 0;
        }

        int R;
        cin >> R;
        for (int i=0; i<R; i++) {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            for (int y=y1; y<=y2; y++) {
                for (int x=x1; x<=x2; x++) {
                    b[y][x] = 1;
                }
            }
        }

        int T = 0;
        while (1) {
            char r;
            bool live = false;
            for (int y=0; y<330; y++)
            for (int x=0; x<330; x++) {
                if (b[y][x] > 0) {
                    if (b[y-1][x] == 1 || b[y][x-1]) {
                        r = 1;
                    } else {
                        r = 0;
                    }
                } else {
                    if (b[y-1][x] == 1 && b[y][x-1]) {
                        r = 1;
                    } else {
                        r = 0;
                    }
                }
                b2[y][x] = r;
                if (r == 1) live = true;
            }
            T++;
            if (!live) break;

            for (int y=0; y<330; y++)
            for (int x=0; x<330; x++) {
                b[y][x] = b2[y][x];
            }

        }
        int res = T;
        cout << "Case #" << caseno << ": " << res << endl;
    }
}
