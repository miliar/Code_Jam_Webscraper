#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <complex>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>

using namespace std;


vector<string> getLineFields(istream& stream) {
    string line;
    getline(stream, line);
    stringstream str;
    str << line;
    vector<string> fields;
    string temp;
    while(str>>temp)
    {
        fields.push_back(temp);
    }
    return fields;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        vector<string> f(4);
        cin >> f[0];
        cin >> f[1];
        cin >> f[2];
        cin >> f[3];
        
        vector<int> rowsX(4, 0);
        vector<int> rowsO(4, 0);
        vector<int> colsX(4, 0);
        vector<int> colsO(4, 0);

        vector<int> diagX(2, 0);
        vector<int> diagO(2, 0);
        
        bool draw = true;
        
        for (int i = 0; i < f.size(); ++i) {
            for (int j = 0; j < f[i].size(); ++j) {
                if (f[i][j] == '.') draw = false;
                if (f[i][j] == 'X' || f[i][j] == 'T') {
                    rowsX[i]++;
                    colsX[j]++;
                    if (i == j)
                        diagX[0]++;
                    if (i == 3 - j)
                        diagX[1]++;
                }
                if (f[i][j] == 'O' || f[i][j] == 'T') {
                    rowsO[i]++;
                    colsO[j]++;
                    if (i == j)
                        diagO[0]++;
                    if (i == 3 - j)
                        diagO[1]++;
                }
            }
        }
        
        bool done = false;
        
        for (int i = 0; i < 4; ++i) {
            if (rowsX[i] == 4 || colsX[i] == 4 || (i < 2 && diagX[i] == 4)) {
                cout << "Case #" << t + 1 << ": " << "X won" << endl;
                done = true;
                break;
            }
            if (colsO[i] == 4 || colsO[i] == 4 || (i < 2 && diagO[i] == 4)) {
                cout << "Case #" << t + 1 << ": " << "O won" << endl;
                done = true;
                break;
            }
        }
        
        if (done) continue;
        
        if (draw) {
            cout << "Case #" << t + 1 << ": " << "Draw" << endl;
        }
        else {
            cout << "Case #" << t + 1 << ": " << "Game has not completed" << endl;
        }

    }
}
