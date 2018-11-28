#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <utility>
#include <iomanip>

using namespace std;

typedef long long LL;
template<typename T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template<typename T> inline T Sqr(const T& x) { return x * x; }

const int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
const int dy[] = {1, 0, -1, -1, -1, 0, 1, 1};


void Solution() {
    vector<string> s(4);
    bool ended = true;
    bool X = false, O = false;
    for (int i = 0; i < 4; ++i) {
        cin >> s[i];
        for (int j = 0; j < 4; ++j) {
            if (s[i][j] == '.') {
                ended = false;
            }
        }
    }
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 8; ++k) {
                map<char, int> mp;
                for (int d = 0; d < 4; ++d) {
                    if (i + dy[k] * d >= 0 && i + dy[k] * d < 4 && j + dx[k] * d >= 0 && j + dx[k] * d < 4) {
                        mp[s[i + dy[k] * d][j + dx[k] * d]]++;
                    }
                }
                if (mp['X'] + mp['T'] == 4) {
                    X = true;
                }
                if (mp['O'] + mp['T'] == 4) {
                    O = true;
                }
            }
        }
    }
    if (X && !O) {
        cout << "X won" << endl;
    } else if (O && !X) {
        cout << "O won" << endl;
    } else if (!ended) {
        cout << "Game has not completed" << endl;
    } else {
        cout << "Draw" << endl;
    }
}


struct Timer {
    map<string, float> starts;
    void Tic(const string& name) { starts[name] = clock(); }
    float Toc(const string& name) { return (clock() - starts[name]) / CLOCKS_PER_SEC; }
} timer;

int main(int argc, char* argv[]) {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    timer.Tic("global");
    int testsNumber;
    cin >> testsNumber;
    for (int curTest = 1; curTest <= testsNumber; ++curTest) {
        cout << "Case #" << curTest << ": ";
        cerr << "Case #" << setw(2) << setfill('0') << curTest << ": running...";
        timer.Tic("test");
        Solution();
        cerr << "done! Elapsed time is " << setprecision(3) << timer.Toc("test") << endl;
    }
    cerr << endl << "Total elapsed time is " << setprecision(3) << timer.Toc("global") << endl;

    return 0;
}
