#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
using namespace std;



int main()
{
    int i, j, k, tt, n, m;
    cin >> tt;
    for (int test = 1; test <= tt; test++) {
        cin >> n >> m;
        vector<string> g(n, "");

        for (i = 0; i < n; i++) cin >> g[i];

        for (i = 0; i + 1 < n; i++)
            for (j = 0; j + 1 < m; j++)
                if (g[i][j] == '#') {
                    if (g[i][j + 1] == '#' && g[i + 1][j] == '#' && g[i + 1][j + 1] == '#') g[i][j] = g[i + 1][j + 1] = '/', g[i][j + 1] = g[i + 1][j] = '\\';
                }

        bool poss = true;

        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
                if (g[i][j] == '#') poss = false;

        cout << "Case #" << test << ":" << endl;
        if (poss) {
            for (i = 0; i < n; i++) cout << g[i] << endl;
        }
        else cout << "Impossible" << endl;
    }
    return 0;
}
