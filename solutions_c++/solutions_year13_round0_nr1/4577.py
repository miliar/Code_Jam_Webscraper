/* 
 * File:   main.cpp
 * Author: Anton Boytsov
 *
 * Created on 13 Апрель 2013 г., 19:42
 */

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int n;
string s[4];

bool isend() {

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (s[i][j] == '.') {
                return false;
            }
        }
    }
    return true;

}

int check_left() {
    
    int x = 0, o = 0, t = 0;
    for (int i = 0; i < 4; i++) {
        if (s[i][i] == 'X')
            x++;
        else if (s[i][i] == 'O')
            o++;
        else if (s[i][i] == 'T')
            t++;
    }
    
    if (x + t == 4)
        return 1;
    
    if (o + t == 4)
        return 2;
    
    return 0;
    
}

int check_right() {
    
    int x = 0, o = 0, t = 0;
    for (int i = 0; i < 4; i++) {
        if (s[i][3 - i] == 'X')
            x++;
        else if (s[i][3 - i] == 'O')
            o++;
        else if (s[i][3 - i] == 'T')
            t++;
    }
    
    if (x + t == 4)
        return 1;
    
    if (o + t == 4)
        return 2;
    
    return 0;
    
}

int check_col(int j) {
    
    int x = 0, o = 0, t = 0;
    for (int i = 0; i < 4; i++) {
        if (s[j][i] == 'X')
            x++;
        else if (s[j][i] == 'O')
            o++;
        else if (s[j][i] == 'T')
            t++;
    }
    
    if (x + t == 4)
        return 1;
    
    if (o + t == 4)
        return 2;
    
    return 0;
    
}

int check_row(int j) {
    
    int x = 0, o = 0, t = 0;
    for (int i = 0; i < 4; i++) {
        if (s[i][j] == 'X')
            x++;
        else if (s[i][j] == 'O')
            o++;
        else if (s[i][j] == 'T')
            t++;
    }
    
    if (x + t == 4)
        return 1;
    
    if (o + t == 4)
        return 2;
    
    return 0;
    
}

int main() {

    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;

    for (int i = 0; i < n; i++) {

        cin >> s[0] >> s[1] >> s[2] >> s[3];

        bool isEnd = isend();
        bool isOk = false;

        for (int j = 0; j < 4; j++) {
            int r = check_col(j);
            if (r == 1) {
                cout << "Case #" << i + 1 << ": X won\n";
                isOk = true;
                break;
            } else if (r == 2) {
                cout << "Case #" << i + 1 << ": O won\n";
                isOk = true;
                break;
            }
            r = check_row(j);
            if (r == 1) {
                cout << "Case #" << i + 1 << ": X won\n";
                isOk = true;
                break;
            } else if (r == 2) {
                cout << "Case #" << i + 1 << ": O won\n";
                isOk = true;
                break;
            }
        }
        
        if (isOk) {
            continue;
        }

        int r = check_left();
        if (r == 1) {
            cout << "Case #" << i + 1 << ": X won\n";
            continue;
        } else if (r == 2) {
            cout << "Case #" << i + 1 << ": O won\n";
            continue;
        }
        r = check_right();
        if (r == 1) {
            cout << "Case #" << i + 1 << ": X won\n";
            continue;
        } else if (r == 2) {
            cout << "Case #" << i + 1 << ": O won\n";
            continue;
        }
        
        if (isEnd) {
            cout << "Case #" << i + 1 << ": Draw\n";
        } else {
            cout << "Case #" << i + 1 << ": Game has not completed\n";
        }




    }

    return 0;
}