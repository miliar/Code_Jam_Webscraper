#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

typedef unsigned long long ull;

int T, R, C;
string maps[100];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        cin >> R >> C;

        for (int i = 0; i < R; ++i)
            cin >> maps[i];

        while (true)
        {
            bool ch = false;

            for (int i = 0; i + 1 < R; ++i)
                for (int j = 0; j + 1 < C; ++j)
                    if (maps[i][j] == '#' && maps[i+1][j] == '#' && maps[i+1][j+1] == '#' && maps[i][j+1] == '#')
                    {
                        maps[i][j] = '/';
                        maps[i][j+1] = '\\';
                        maps[i+1][j] = '\\';
                        maps[i+1][j+1] = '/';
                        ch = true;
                    }
            if (!ch)
                break;
        }

        bool good = true;
        for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (maps[i][j] == '#')
                good = false;

        cout << "Case #" << t << ":\n";

        if (!good) {
            cout << "Impossible\n";
        }
        else
        {
            for (int i = 0; i < R; ++i)
                cout << maps[i] << endl;
        }
    }

    return 0;
}
