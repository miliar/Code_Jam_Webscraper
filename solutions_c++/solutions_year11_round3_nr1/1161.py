#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

char pole[100][100];

int n, m;

bool fill(int i, int j) {
        if (i >= n - 1 || j >= m - 1)
                return false;
        else
                if (pole[i][j + 1] == '#' && pole[i + 1][j] == '#' && pole[i + 1][j + 1] == '#') {
                        pole[i][j] = pole[i + 1][j + 1] = '/';
                        pole[i][j + 1] = pole[i + 1][j] = '\\';
                        return true;
                } else 
                        return false;
}

int main() {
        int t;
        cin >> t;
        for (int test = 1; test <= t; test++) {
                cin >> n >> m;
                for (int i = 0; i < n; i++) {
                        string s;
                        cin >> s;
                        for (int j = 0; j < m; j++)
                                pole[i][j] = s[j];
                }
                bool answer = true;
                int i = 0, j = 0;
                while (answer && (i < n && j < m)) {
                        if (pole[i][j] == '#')
                                answer = answer && fill(i, j);
                        if (j < m - 1)
                                j++;
                        else {
                                j = 0;
                                i++;
                        }
                }
                cout << "Case #" << test << ":" << endl;
                if (!answer)
                        cout << "Impossible" << endl;
                else
                        for (int i = 0; i < n; i++) {
                                for (int j = 0; j < m; j++)
                                        cout << pole[i][j];
                                cout << endl;
                        }
        }
}
