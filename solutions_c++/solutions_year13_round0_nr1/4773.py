
#include <iostream>
#include <string>
#include <cassert>
#include <vector>
using namespace std;

typedef pair<int, char> info_t;

string check(const string& s)
{
    int t_count = 0, x_count = 0, o_count = 0;
    assert(s.size() == 4);
    for (int i = 0; i < 4; ++i) {
        switch (s[i]) {
        case 'O': o_count++; break;
        case 'X': x_count++; break;
        case 'T': t_count++; break;
        }
    }
    if (o_count + t_count == 4) return "O won";
    if (x_count + t_count == 4) return "X won";
    return "";
}

string solve(const vector<string>& b)
{
    info_t row_info[4], col_info[4];
    for (int i = 0; i < 4; ++i) {
        row_info[i] = make_pair(0, '?');
        col_info[i] = make_pair(0, '?');
    }

    string ret;
    int empty_count = 0;
    string diag1_s, diag2_s;
    for (int i = 0; i < 4; ++i) {
        diag1_s.push_back(b[i][i]);
        diag2_s.push_back(b[3-i][i]);
        string row_s, col_s;
        for (int j = 0; j < 4; ++j) {
            if (b[i][j] == '.') {
                empty_count++;
            }
            row_s.push_back(b[i][j]);
            col_s.push_back(b[j][i]);
        }
        ret = check(row_s);
        if (ret != "") return ret;
        ret = check(col_s);
        if (ret != "") return ret;
    }
    ret = check(diag1_s);
    if (ret != "") return ret;
    ret = check(diag2_s);
    if (ret != "") return ret;

    if (empty_count == 0) {
        return "Draw";
    } else {
        return "Game has not completed";
    }
}

int main()
{
    int T;
    cin >> T;
    string s;
    getline(cin, s); // skip endline

    for (int f = 0; f < T; ++f) {
        vector<string> b;
        for (int i = 0; i < 4; ++i) {
            getline(cin, s);
            assert(s.size() == 4);
            b.push_back(s);
        }
        getline(cin, s); // skip empty line
        std::cout << "Case #" << f+1 << ": " << solve(b) << std::endl;

    }
}

