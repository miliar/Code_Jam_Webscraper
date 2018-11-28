#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <cassert>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdexcept>

using namespace std;

bool isX(vector<string> a) {
    for(int i = 0; i < a.size(); i++) {
        for(int j = 0; j < a[i].size(); j++) {
            if(a[i][j] == 'T') {
                a[i][j] = 'X';
                break;
            }
        }
    }
    // check rows
    for(int i = 0; i < a.size(); i++) {
        int c = 0;
        for(int j = 0; j < a[i].size(); j++) {
            if(a[i][j] == 'X') {
                c++;
            }
        }
        if(c == 4) {
            return true;
        }
    }
    // check columns
    for(int i = 0; i < a.size(); i++) {
        int c = 0;
        for(int j = 0; j < a[i].size(); j++) {
            if(a[j][i] == 'X') {
                c++;
            }
        }
        if(c == 4) {
            return true;
        }
    }
    //check diagonals
    if(a[0][0] == 'X' && a[1][1] == 'X' && a[2][2] == 'X' && a[3][3] == 'X') {
        return true;
    }
    else if(a[0][3] == 'X' && a[1][2] == 'X' && a[2][1] == 'X' && a[3][0] == 'X') {
        return true;
    }

    return false;
}

bool isO(vector<string> a) {
    for(int i = 0; i < a.size(); i++) {
        for(int j = 0; j < a[i].size(); j++) {
            if(a[i][j] == 'T') {
                a[i][j] = 'O';
                break;
            }
        }
    }
    // check rows
    for(int i = 0; i < a.size(); i++) {
        int c = 0;
        for(int j = 0; j < a[i].size(); j++) {
            if(a[i][j] == 'O') {
                c++;
            }
        }
        if(c == 4) {
            return true;
        }
    }
    // check columns
    for(int i = 0; i < a.size(); i++) {
        int c = 0;
        for(int j = 0; j < a[i].size(); j++) {
            if(a[j][i] == 'O') {
                c++;
            }
        }
        if(c == 4) {
            return true;
        }
    }
    //check diagonals
    if(a[0][0] == 'O' && a[1][1] == 'O' && a[2][2] == 'O' && a[3][3] == 'O') {
        return true;
    }
    else if(a[0][3] == 'O' && a[1][2] == 'O' && a[2][1] == 'O' && a[3][0] == 'O') {
        return true;
    }

    return false;
}

bool isC(vector<string> a) {
    int c = 0;
    for(int i = 0; i < a.size(); i++) {
        for(int j = 0; j < a[i].size(); j++) {
            if(a[i][j] != '.') {
                c++;
            }
        }
    }

    if(c == 16) {
        return true;
    }

    return false;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int c = 1; c < T+1; c++) {
        vector<string> a;
        for(int i = 0; i < 4; i++) {
            string s;
            cin >> s;
            a.push_back(s);
        }
        bool x = isX(a), o = isO(a), com = isC(a);

        if(x) {
            cout << "Case #" << c << ": X won" << endl;
        }
        else if(o) {
            cout << "Case #" << c << ": O won" << endl;
        }
        else if(!x && !o && com) {
            cout << "Case #" << c << ": Draw" << endl;
        }
        else {
            cout << "Case #" << c << ": Game has not completed" << endl;
        }
    }

    return 0;
}

