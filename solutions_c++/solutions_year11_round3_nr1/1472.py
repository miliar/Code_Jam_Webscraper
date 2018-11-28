// Google Code Jam - Candy Splitting.cpp : main project file.

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;
    cin >> cases;

    for (int i=0; i<cases; i++)
    {
        int r, c;
        vector<string> lines;
        string line;

        cin >> r;
        cin >> c;

        lines.reserve(r);
        getline(cin, line);

        for (int j=0; j<r; j++)
        {
            getline(cin, line);
            lines.push_back(line);
        }

        for (int x=0; x<r-1; x++)
        {
            for (int y=0; y<c-1; y++)
            {
                if (lines[x][y] == '#' &&
                    lines[x][y+1] == '#' &&
                    lines[x+1][y] == '#' &&
                    lines[x+1][y+1] == '#')
                {
                    lines[x][y] = '/';
                    lines[x][y+1] = '\\';
                    lines[x+1][y] = '\\';
                    lines[x+1][y+1] = '/';
                }
            }
        }

        cout << "Case #" << (i+1) << ":" << endl;

        bool impos = false;
        for (int x=0; x<r; x++)
        {
            for (int y=0; y<c; y++)
            {
                if (lines[x][y] == '#')
                {
                    impos = true;
                    cout << "Impossible" << endl;
                    break;
                }
            }

            if (impos) break;
        }

        if (!impos)
        {
            for (int x=0; x<r; x++)
            {
                cout << lines[x] << endl;
            }
        }
    }

    return 0;
}
