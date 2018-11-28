#include <iostream>
#include <vector>

using namespace std;

const int MAX = 128;

char comb[MAX][MAX], oppo[MAX][MAX];

void clear()
{
    for (int i = 0; i < MAX; i++)
        for (int j = 0; j < MAX; j++)
            comb[i][j] = oppo[i][j] = 0;
}

void solve(int t)
{
    int n, c, d;
    char x, y, z;
    vector<char> list;

    cin >> c;
    for (int i = 0; i < c; i++) {
        cin >> x >> y >> z;
        comb[x][y] = comb[y][x] = z;
    }

    cin >> d;
    for (int i = 0; i < d; i++) {
        cin >> x >> y;
        oppo[x][y] = oppo[y][x] = 1;
    }

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if (list.empty())
            list.push_back(x);
        else {
            y = list.back();
            z = comb[x][y];
            if (z) {
                list.pop_back(); // y
                list.push_back(z);
            } else {
                bool opposite = false;
                for (int i = 0; i < list.size(); i++)
                    if (oppo[x][list[i]])
                        opposite = true;
                if (opposite)
                    list.clear();
                else
                    list.push_back(x);
            }
        }
    }

    cout << "Case #" << t << ": [";
    for (int i = 0; i < list.size(); i++) {
        if (i) cout << ", ";
        cout << list[i];
    }
    cout << "]" << endl;
}

int main()
{
    int t; // number of tests
    cin >> t;
    for (int i = 0; i < t; i++) {
        clear();
        solve(i + 1);
    }
    return 0;
}
