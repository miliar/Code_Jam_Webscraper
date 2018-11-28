#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<vector<char> > desk(4);

char pl[] = {'X', 'O'};

bool test(int x, int y, int dx, int dy, char c) 
{
    int count = 0;
    for (int i = 0; i < 4; ++i) {
        if (desk[x][y] == c || desk[x][y] == 'T') {
            ++count;
        }
        x += dx;
        y += dy;
    }
    return count == 4;
}

string solve() 
{
    int count = 0;
    char c;
    for (int i = 0; i < 4; ++i) {
        desk[i] = vector<char>(4);
        for (int j = 0; j < 4; ++j) {
            cin >> desk[i][j];
            if (desk[i][j] != '.') {
                ++count;
            }
        }
    }

    for (int p = 0; p < 2; ++p) {
        for (int i = 0; i < 4; ++i) {
            if (test(0, i, 1, 0, pl[p]) || test(i, 0, 0, 1, pl[p])) {
                return pl[p] + string(" won");
            }
        }
        if (test(0, 0, 1, 1, pl[p]) || test(3, 0, -1, 1, pl[p])) {
            return pl[p] + string(" won");
        }        
    }
    if (count == 16) {
        return "Draw";
    }

    return "Game has not completed";
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
	return 0;
}

