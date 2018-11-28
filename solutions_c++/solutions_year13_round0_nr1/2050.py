#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

bool test(const vector<string>& v, char c)
{
    for (int i = 0; i < v.size(); ++i) {
        if (count(v[i].begin(), v[i].end(), c) == 4)
            return true;
    }
    for (int i = 0; i < v[0].size(); ++i) {
        bool f = 1;
        for (int j = 0; j < v.size(); ++j) {
            if (v[j][i] != c) {
                f = 0;
                break;
            }
        }
        if (f)
            return true;
    }
    bool f = 1;
    for (int i = 0; i < v.size(); ++i) {
        if (v[i][i] != c) {
            f = 0;
        }
    }
    if (f)
        return true;
    f = 1;
    for (int i = 0; i < v.size(); ++i) {
        if (v[i][v.size() - i - 1] != c) {
            f = 0;
        }
    }
    if (f)
        return true;
    return false;
}

string result(vector<string>& v)
{
    const string res1("X won");
    const string res2("O won");
    const string res3("Draw");
    const string res4("Game has not completed");

    int x = -1, y = -1;
    bool f = 0;
    for (int i = 0; i < v.size(); ++i) {
        int pos;
        if ((pos = v[i].find('T')) != -1) {
            x = pos;
            y = i;
        }
        if (v[i].find('.') != -1)
            f = 1;
    }

    if (x + y >= 0)
        v[y][x] = 'X';
    if (test(v, 'X'))
        return res1;
    if (x + y >= 0)
        v[y][x] = 'O';
    if (test(v, 'O'))
        return res2;
    return f ? res4 : res3;
}

int main()
{
    ifstream cin("test.in");
    ofstream cout("test.out");
    //cout.precision(6);
    //cout.setf(ios::fixed,ios::floatfield);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        vector<string> v(4);
        for (int j = 0; j < 4; ++j)
            cin >> v[j];
        /*string s;
        cin >> s; // skipping*/
        /*for (int j = 0; j < 4; ++j)
            cout << v[j] << endl;
        cout << endl;*/
        cout << "Case #" << i << ": " << result(v) << endl;
    }
    return 0;
}
