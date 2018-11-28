#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solve(int n, int m, vector< vector<char> >& field)
{
    int rem = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            rem += field[i][j];
        }
    }

    int result = 0;
    vector< vector<char> > nfield = field;
    while (rem) {
        ++result;
        for (int i = 0; i < n; ++i) {
            char prev = 0;
            for (int j = 0; j < m; ++j) {
                if (field[i][j] && !prev) {
                    if (i == 0 || field[i-1][j] == 0) {
                        nfield[i][j] = 0;
                        --rem;
                    }
                }
                if (!field[i][j] && prev) {
                    if (i != 0 && field[i-1][j] == 1) {
                        nfield[i][j] = 1;
                        ++rem;
                    }
                }
                prev = field[i][j];
            }
        }
        field = nfield;
    }
    return result;
}

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int r;
        cin >> r;
        int maxx = 0, maxy = 0;
        vector<int> x1s(r), y1s(r), x2s(r), y2s(r);
        for (int i = 0; i < r; ++i) {
            cin >> x1s[i] >> y1s[i] >> x2s[i] >> y2s[i];
            if (x2s[i] > maxx) maxx = x2s[i];
            if (y2s[i] > maxy) maxy = y2s[i];
        }
        //vector< vector<char> > field(maxy, vector<char>(maxx));
        vector< vector<char> > field(300, vector<char>(300));
        for (int i = 0; i < r; ++i) {
            int x1 = x1s[i], y1 = y1s[i], x2 = x2s[i], y2 = y2s[i];
            for (int j = y1-1; j < y2; ++j) {
                for (int k = x1-1; k < x2; ++k) {
                    field[j][k] = 1;
                }
            }
        }
        int result = solve(300, 300, field);
        //int result = solve(maxy, maxx, field);
        cout << "Case #" << (test + 1) << ": " << result << endl;
    }
}
