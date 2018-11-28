//Copyright (c) Nguyen Nam
#pragma comment(linker, "/STACK:0x04000000")
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cassert>
#include <climits>
#include <ctime>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>

using namespace std;
typedef unsigned int uint;
typedef long long i64;
typedef unsigned long long ui64;
typedef long double ld;

bool IsAllTheSame(string str, char c) {
    for (int i = 0; i < 4; i++) {
        if (str[i] == 'T') {
            continue;
        }
        if (str[i] != c) {
            return false;
        }
    }
    return true;
}

string Sol(vector<string> game) {
    const string X = "X won";
    const string O = "O won";
    const string DRAW = "Draw";
    const string NOT_END = "Game has not completed";
    for (int i = 0; i < 4; i++) {
        string str;
        for (int j = 0; j < 4; j++) {
            str += game[i][j];
        }
        if (IsAllTheSame(str, 'X')) {
            return X;
        }
        if (IsAllTheSame(str, 'O')) {
            return O;
        }
        str = "";
        for (int j = 0; j < 4; j++) {
            str += game[j][i];
        }
        if (IsAllTheSame(str, 'X')) {
            return X;
        }
        if (IsAllTheSame(str, 'O')) {
            return O;
        }
    }
    string str = string() + game[0][0] + game[1][1] + game[2][2] + game[3][3];
    if (IsAllTheSame(str, 'X')) {
        return X;
    }
    if (IsAllTheSame(str, 'O')) {
        return O;
    }
    str = string() + game[0][3] + game[1][2] + game[2][1] + game[3][0];
    if (IsAllTheSame(str, 'X')) {
        return X;
    }
    if (IsAllTheSame(str, 'O')) {
        return O;
    }
    int empty_cells_counter = 0;
    for (int i = 0; i < 4; i++) {
        empty_cells_counter += count(game[i].begin(), game[i].end(), '.');
    }
    if (empty_cells_counter == 0) {
        return DRAW;
    }
    return NOT_END;
}

int main() {
#ifdef NOVACO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int i_t = 1; i_t <= t; i_t++) {
        vector<string> game(4);
        for (int i = 0; i < 4; i++) {
            cin >> game[i];
        }
        string res = Sol(game);
        cout << "Case #" << i_t << ": " << res << "\n";
    }
}