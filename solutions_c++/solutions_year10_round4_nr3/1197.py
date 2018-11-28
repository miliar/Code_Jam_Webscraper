#include <iostream>
using namespace std;

bool grid[100][100];
bool copyy[100][100];

bool alive(bool bacteria[100][100]) {
    for (int x = 0; x < 100; ++x) {
        for (int y = 0; y < 100; ++y) {
            if (bacteria[x][y]) return true;
        }
    }
    return false;
}

void display() {
    for (int x = 0; x < 5; ++x) {
        for (int y = 0; y < 5; ++y) {
            cout << (grid[x][y]? 'x' : '.');
        }
        cout << endl;
    }
    cout << endl;
}

void step() {
    for (int x = 0; x < 100; ++x) {
        for (int y = 0; y < 100; ++y) {
            if (grid[x][y]) {
                if (x > 0 && grid[x - 1][y]) {
                    copyy[x][y] = true;
                } else if (y > 0 && grid[x][y - 1]) {
                    copyy[x][y] = true;
                } else {
                    copyy[x][y] = false;
                }                
            } else {
                copyy[x][y] = (x > 0 && grid[x - 1][y] && y > 0 && grid[x][y - 1]);
            }
        }
    }
    
    for (int x = 0; x < 100; ++x) {
        for (int y = 0; y < 100; ++y) {
            grid[x][y] = copyy[x][y];
        }
    }
}

int main() {
    int C;
    cin >> C;
    for (int c = 0; c < C; ++c) {
        int R;
        cin >> R;
        
        for (int x = 0; x < 100; ++x) {
            for (int y = 0; y < 100; ++y) {
                grid[x][y] = false;
            }
        }
        
        for (int r = 0; r < R; ++r) {
            int x1, x2, y1, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            //cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
            for (int x = x1 - 1; x < x2; ++x) {
                for (int y = y1 - 1; y < y2; ++y) {
                    //display();
                    grid[x][y] = true;
                }
            }
        }
        
        long life;
        for (life = 0; alive(grid); ++life) {
            //display();
            step();
        }
        
        printf("Case #%d: %ld\n", (c + 1), life);
    }

    return 0;
}